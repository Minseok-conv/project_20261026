"""실습 02 기본필수: 미리 제공된 예측으로 MAE와 RMSE를 계산합니다."""
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

actual = [100, 200, 300]     # 실제 소요시간, 단위 ms
prediction = [120, 180, 360] # 모델이 예측했다고 가정한 값, 단위 ms
# TODO B02: 실제값과 예측값을 두 평가 함수에 넣으세요.
# 힌트: 두 함수 모두 (actual, prediction) 순서로 호출합니다.
mae = mean_absolute_error(actual, prediction)
rmse = root_mean_squared_error(actual, prediction)
print("MAE(ms):", round(float(mae), 2))
print("RMSE(ms):", round(float(rmse), 2))
# MAE는 절댓값 20·20·60의 평균입니다. RMSE는 제곱 400·400·3600의 평균에 루트를 취합니다.
