"""실습 03 기본필수: 작은 정상 자료로 확률과 클래스를 확인합니다."""
from sklearn.linear_model import LogisticRegression

# 원리 확인용 데이터입니다. X의 한 값은 작업 복잡도, y는 성공 0 / 실패 1입니다.
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]
model = LogisticRegression()
# TODO B03: model을 X와 y로 학습하세요.
# 힌트: model.fit(입력, 정답)
model.fit(X,y)
new = [[2], [5]]
print("클래스 순서:", model.classes_)
print("확률 [성공, 실패]:")
print(model.predict_proba(new).round(3))
print("예측 클래스:", model.predict(new))
# 이 작은 시연의 출력은 평가 점수가 아닙니다. 실제 성능 비교는 07번의 valid로 합니다.
