"""실습 07: 회귀·분류 비교표와 모델을 생성합니다. 실습08은 restore.py로 이어갑니다."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE / "data/requests.csv").set_index("request_id")
# 이 표는 전날의 분할 소속과 각 분할 내부의 행 순서(position)를 함께 보존합니다.
split = pd.read_csv(HERE / "data/split_manifest.csv")
train_ids = split.loc[split["split"] == "train"].sort_values("position")["request_id"]
valid_ids = split.loc[split["split"] == "valid"].sort_values("position")["request_id"]
train = raw.loc[train_ids]
valid = raw.loc[valid_ids]
features = ["input_chars", "allowed_tools", "task_type", "priority"]
X_train = train[features]
X_valid = valid[features]
# test의 ID는 분할표에만 남겨 둡니다. test 입력·정답을 모델에 전달하지 않습니다.

import json
import joblib
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from preprocessing import build_model
from evaluate import regression_metrics, classification_metrics
from search import compare_k

# 주 지표는 실행 전 고정: 회귀 RMSE 최소, 분류 F1 최대. 동점은 표에 먼저 적힌 후보.
search = compare_k(train, valid)
best_c = search[search["task"] == "classification"].sort_values(["valid_score", "K"], ascending=[False, True]).iloc[0]
best_r = search[search["task"] == "regression"].sort_values(["valid_score", "K"]).iloc[0]
k_class, k_reg = int(best_c["K"]), int(best_r["K"])
specifications = {
    "regression": [("Dummy", DummyRegressor()), ("Linear", LinearRegression()),
                   (f"KNN{k_reg}", KNeighborsRegressor(n_neighbors=k_reg))],
    "classification": [("Dummy", DummyClassifier(strategy="most_frequent")),
                       ("Logistic", LogisticRegression(C=1.0, max_iter=1000)),
                       (f"KNN{k_class}", KNeighborsClassifier(n_neighbors=k_class))],
}
out = HERE / "outputs"
out.mkdir(exist_ok=True)

predictions = []
selection = {}
chosen_models = {}
for task, candidates in specifications.items():
    target = "elapsed_ms" if task == "regression" else "failed"
    rows = []
    fitted = {}
    for name, estimator in candidates:
        model = build_model(estimator)
        # TODO H07fit: 해당 target으로 학습하고 valid 예측을 구하세요.
        # 힌트: 두 문제의 정답 열은 target에 들어 있습니다.
        pass
        prediction = None
        metric = regression_metrics(valid[target], prediction) if task == "regression" else classification_metrics(valid[target], prediction)
        rows.append({"model": name, "scale": "standard", **metric})
        # index=False로 저장하므로 요청 ID를 별도 열로 기록합니다.
        predictions.append(pd.DataFrame({"request_id": valid.index, "task": task, "model": name,
            "actual": valid[target].to_numpy(), "predicted": prediction}))
        fitted[name] = model
    table = pd.DataFrame(rows)
    table.to_csv(out / f"{task}_comparison.csv", index=False, encoding="utf-8-sig")
    best = table.loc[table["RMSE_ms"].idxmin()] if task == "regression" else table.loc[table["F1"].idxmax()]
    selection[task] = best["model"]
    chosen_models[task] = fitted[best["model"]]
    print(task, "/ valid 20건")
    print(table.round(3).to_string(index=False))

search.to_csv(out / "knn_search.csv", index=False, encoding="utf-8-sig")
pd.concat(predictions, ignore_index=True).to_csv(out / "validation_predictions.csv", index=False, encoding="utf-8-sig")
(out / "selection.json").write_text(json.dumps(selection, ensure_ascii=False, indent=2), encoding="utf-8")
# 본인이 여기서 생성한 모델만 다음 restore.py에서 복원합니다. 모델은 배포 ZIP에 넣지 않습니다.
joblib.dump(chosen_models, out / "models.joblib")
print("선택 모델:", selection)
print("선택 K / 분류:", k_class, "회귀:", k_reg)
print("outputs에 비교표·탐색표·예측·선택 기록·모델을 저장했습니다.")
print("test는 보관만 했으며 모델에 전달하지 않았습니다.")
