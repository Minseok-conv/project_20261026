"""실습 01 심화: 기존 응용의 두 입력 선형회귀를 수식과 연결합니다."""
from sklearn.linear_model import LinearRegression

X = [[200, 1], [400, 1], [200, 3], [600, 2]]
y = [700, 800, 900, 1000]
model = LinearRegression()
# TODO H01: 두 특성을 가진 X와 y로 model을 학습하세요.
# 힌트: 기본필수와 호출 방법은 같습니다.
model.fit(X,y)
new = [[400, 2]]
prediction = model.predict(new)[0]
# 같은 수식을 직접 계산합니다. 모델을 별도로 학습하거나 고치지 않습니다.
manual = model.intercept_ + model.coef_[0] * new[0][0] + model.coef_[1] * new[0][1]
print("계수:", model.coef_.round(1))
print("절편:", round(float(model.intercept_), 1))
print("예측(ms):", round(prediction, 1))
print("손계산(ms):", round(manual, 1))
print("차이:", round(abs(prediction - manual), 8))
