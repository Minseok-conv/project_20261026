"""실습 03 심화: 공통 데이터의 확률과 별도 가상 확률 예제를 구분합니다."""
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score

model = build_model(LogisticRegression(C=1.0, max_iter=1000))
model.fit(X_train, train["failed"])
actual_prediction = model.predict(X_valid)
print("공통 valid 혼동행렬")
print(confusion_matrix(valid["failed"], actual_prediction, labels=[0, 1]))
#confusion_matrix는 [[TN, FP],[FN, TP]]으로 출력됨

truth = np.array([0, 0, 0, 1, 1, 1])
probability = np.array([0.10, 0.40, 0.70, 0.35, 0.60, 0.90])
rows = []
for threshold in [0.5, 0.3]:
    # TODO H03: 고정값 0.5 대신 반복 변수 threshold를 사용하세요.
    # 힌트: 비교 결과 True/False를 astype(int)로 1/0으로 바꿉니다.
    prediction = (probability >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(truth, prediction, labels=[0, 1]).ravel()
    #label = [0,1]인 이유는 일단 이진분류여서 두가지 클래스 0,1로 지정하고, 혼동행렬 순서 [TN, FP, FN, TP] = [00,01,10,11]을 나타낸다.
    #ravel()은 [[2,1],[1,3]] => [2,1,1,3]으로 1차원으로 펼치는 역할임.
    rows.append({"threshold": threshold, "FP": fp, "FN": fn, "TP": tp,
                 "F1": f1_score(truth, prediction, zero_division=0)})
comparison = pd.DataFrame(rows)
out = HERE / "outputs"
out.mkdir(exist_ok=True)

comparison.to_csv(out / "threshold_comparison.csv", index=False, encoding="utf-8-sig")
print("가상 확률 6개의 임계값 비교")
print(comparison.round(3).to_string(index=False))
