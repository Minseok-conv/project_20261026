"""실습07에서 main.py가 가져다 쓰는 작은 평가 모듈입니다."""
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def regression_metrics(actual, prediction):
    """회귀 오차의 단위는 ms, R²에는 단위가 없습니다."""
    # TODO H07r: MAE·RMSE를 계산하세요.
    # 힌트: 실습02에서 사용한 함수를 그대로 씁니다.
    mae = None
    rmse = None
    return {"MAE_ms": mae, "RMSE_ms": rmse, "R2": r2_score(actual, prediction)}

def classification_metrics(actual, prediction):
    """실패1을 양성으로 고정합니다. zero_division=0은 분모가 0일 때 0점 표시 규칙입니다."""
    tn, fp, fn, tp = confusion_matrix(actual, prediction, labels=[0, 1]).ravel()
    # TODO H07c: 실패1의 F1을 계산하세요.
    # 힌트: f1_score(actual, prediction, zero_division=0)
    f1 = None
    return {"Accuracy": accuracy_score(actual, prediction), "F1": f1,
            "Precision": precision_score(actual, prediction, zero_division=0),
            "Recall": recall_score(actual, prediction, zero_division=0),
            "TN": int(tn), "FP": int(fp), "FN": int(fn), "TP": int(tp)}
