"""실습 04 응용: 같은 세 이웃에서 가중치만 바꿉니다."""
from sklearn.neighbors import KNeighborsRegressor

X = [[1], [2], [4], [7], [9]]
y = [10, 20, 40, 70, 90]
for weight in ["uniform", "distance"]:
    # TODO A04: weights에 반복 변수 weight를 넣으세요.
    # 힌트: 이웃 수는 3으로 고정합니다.
    model = KNeighborsRegressor(n_neighbors=3, weights= weight)
    model.fit(X, y)
    print(weight, "예측:", model.predict([[3.2]]).round(2))
# uniform은 3개를 똑같이, distance는 가까운 값에 더 큰 비중을 줍니다.
