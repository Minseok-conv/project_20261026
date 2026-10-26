"""실습 01 기본필수: 학습과 예측 두 문장을 연결합니다."""
from sklearn.linear_model import LinearRegression

# X는 한 행이 한 사람이고, 각 행의 숫자는 공부시간입니다. 그래서 [[1], [2], ...]입니다.
X = [[1], [2], [3], [4], [5]]
y = [52, 61, 69, 80, 89]  # 같은 순서의 실제 점수
model = LinearRegression()  # 선을 맞추는 모델을 준비합니다. 아직 학습 전입니다.
# TODO B01: model을 X, y로 학습하고, [[6]]의 예측을 prediction에 넣으세요.
model.fit(X,y)
prediction = model.predict([[6]])
print("기울기:", round(model.coef_[0], 1))
print("절편:", round(model.intercept_, 1))
print("6시간 예측:", round(prediction[0], 1))
# 주의: 6시간은 학습 범위 1~5시간 밖입니다. 수식 확인용이며 실제 점수를 보장하지 않습니다.
