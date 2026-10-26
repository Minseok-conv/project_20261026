"""실습08: main.py로 본인이 생성한 모델만 복원합니다. 재학습하지 않습니다."""
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from preprocessing import FEATURES

HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE / "data/requests.csv").set_index("request_id")
split = pd.read_csv(HERE / "data/split_manifest.csv")
ids = split.loc[split["split"] == "valid"].sort_values("position")["request_id"]
X_valid = raw.loc[ids, FEATURES]
selection = json.loads((HERE / "outputs/selection.json").read_text(encoding="utf-8"))
saved = pd.read_csv(HERE / "outputs/validation_predictions.csv")
# TODO H08: main.py로 직접 만든 models.joblib을 읽으세요.
# 힌트: joblib.load에는 실제 모델 파일 경로를 전달합니다.
models = None
for task in ["regression", "classification"]:
    prediction = models[task].predict(X_valid)
    reference = saved[(saved["task"] == task) & (saved["model"] == selection[task])].set_index("request_id").loc[ids]
    print(task, "복원 예측 일치:", bool(np.allclose(prediction, reference["predicted"])))
print("fit을 호출하지 않았고 test도 사용하지 않았습니다.")
