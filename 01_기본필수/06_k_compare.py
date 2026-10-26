"""실습 06 기본필수: 전날의 20건에서 같은 분할로 K만 비교합니다."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

# 제공: 이 파일 옆의 CSV를 읽고, 전날과 같은 요청들을 12 / 4 / 4로 나눕니다.
HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE / "requests.csv")
develop, test = train_test_split(raw, test_size=0.2, random_state=42, stratify=raw["failed"])
train, valid = train_test_split(develop, test_size=0.25, random_state=42, stratify=develop["failed"])
# test는 보관만 합니다. 학습·예측에 넣지 않습니다.

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# 글자 수 한 열만 쓰는 짧은 실험입니다. 파일07은 작업 종류도 쓰므로 별도 실험입니다.
X_train = train[["input_chars"]]
X_valid = valid[["input_chars"]]
for k in [1, 3, 5]:
    # TODO B06: 고정된 이웃 수 1을 반복 변수 k로 바꾸세요.
    # 힌트: n_neighbors=k이면 반복마다 1, 3, 5로 바뀝니다.
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    model.fit(X_train, train["failed"])
    prediction = model.predict(X_valid)
    print("K:", model[-1].n_neighbors, "valid F1:", round((f1_score(valid["failed"], prediction, zero_division=0), 3))
print("분할:", len(train), len(valid), len(test))
