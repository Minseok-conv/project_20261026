"""제공 모듈: 전날 학습한 전처리를 한 함수로 재사용합니다. 직접 구현할 TODO는 없습니다."""
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

FEATURES = ["input_chars", "allowed_tools", "task_type", "priority"]

def build_model(estimator, scale="standard"):
    """입력4열 → 수치/문자 전처리 → 전달받은 모델. 호출할 때마다 새 객체를 만듭니다."""
    # passthrough도 결측 대체는 생략하지 않습니다. 바꾸는 것은 숫자의 스케일뿐입니다.
    scaler = {"none": "passthrough", "standard": StandardScaler(), "minmax": MinMaxScaler()}[scale]
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", scaler)])
    category = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                         ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])
    pre = ColumnTransformer([("num", numeric, FEATURES[:2]), ("cat", category, FEATURES[2:])])
    return Pipeline([("pre", pre), ("model", estimator)])
