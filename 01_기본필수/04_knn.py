"""실습 04 기본필수: 이웃 3개의 투표와 평균을 비교합니다."""
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

X = [[1], [2], [4], [7], [9]]
class_y = [0, 0, 1, 1, 1]
number_y = [10, 20, 40, 70, 90]
# 3.2에 가까운 입력은 4, 2, 1입니다. 거리: 0.8, 1.2, 2.2
# TODO B04a: 분류에서 이웃 수를 3으로 바꾸세요.
# 힌트: n_neighbors는 참고할 이웃 수입니다.
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, class_y)
print("분류:", classifier.predict([[3.2]]))
# TODO B04b: 회귀에서도 이웃 수를 3으로 바꾸세요.
# 힌트: 같은 이웃의 숫자 정답 [40, 20, 10]을 평균냅니다.
regressor = KNeighborsRegressor(n_neighbors=3)
regressor.fit(X, number_y)
print("회귀:", regressor.predict([[3.2]]).round(2))
