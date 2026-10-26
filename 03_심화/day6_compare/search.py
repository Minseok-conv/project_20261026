"""제공: 실습06의 탐색을 재사용합니다. 새 후보를 추가하는 과제가 아닙니다."""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import f1_score, root_mean_squared_error
from preprocessing import build_model, FEATURES

def compare_k(train, valid):
    """같은 자료·전처리에서 K만 바꿔 두 문제의 비교표를 만듭니다."""
    rows = []
    for task in ["classification", "regression"]:
        target = "failed" if task == "classification" else "elapsed_ms"
        for k in [1, 3, 5, 9, 15]:
            estimator = KNeighborsClassifier(n_neighbors=k) if task == "classification" else KNeighborsRegressor(n_neighbors=k)
            model = build_model(estimator)
            model.fit(train[FEATURES], train[target])
            train_prediction = model.predict(train[FEATURES])
            valid_prediction = model.predict(valid[FEATURES])
            if task == "classification":
                train_score = f1_score(train[target], train_prediction, zero_division=0)
                valid_score = f1_score(valid[target], valid_prediction, zero_division=0)
                metric = "F1"
            else:
                train_score = root_mean_squared_error(train[target], train_prediction)
                valid_score = root_mean_squared_error(valid[target], valid_prediction)
                metric = "RMSE_ms"
            rows.append({"task": task, "K": k, "scale": "standard", "weights": "uniform",
                         "metric": metric, "train_score": train_score, "valid_score": valid_score})
    return pd.DataFrame(rows)
