"""실습 05 심화: 예측 전후 학습 통계를 함께 관찰합니다."""
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

import numpy as np
from preprocessing import build_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

rows = []
for scale in ["none", "standard", "minmax"]:
    # TODO H05: 전처리에 반복 변수 scale을 전달하세요.
    # 힌트: build_model의 두 번째 인자는 스케일링 이름입니다.
    model = build_model(KNeighborsClassifier(n_neighbors=5), scale="standard")
    model.fit(X_train, train["failed"])
    imputer = model["pre"].named_transformers_["num"]["imputer"]
    before = imputer.statistics_.copy()
    prediction = model.predict(X_valid)
    rows.append({"scale": scale, "K": 5,
        "train_F1": f1_score(train["failed"], model.predict(X_train), zero_division=0),
        "valid_F1": f1_score(valid["failed"], prediction, zero_division=0),
        "median_unchanged": np.array_equal(before, imputer.statistics_)})
comparison = pd.DataFrame(rows)
out = HERE / "outputs"
out.mkdir(exist_ok=True)

comparison.to_csv(out / "scaling_comparison.csv", index=False, encoding="utf-8-sig")
print(comparison.round(3).to_string(index=False))
print("숫자와 문자 처리를 유지하고, 숫자의 스케일만 바꾸었습니다.")
