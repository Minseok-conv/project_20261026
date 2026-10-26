"""실습 04 심화: 이전 응용의 거리 가중치를 표로 설명합니다."""
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

X = np.array([[1], [2], [4], [7], [9]])
y = np.array([10, 20, 40, 70, 90])
plain = KNeighborsRegressor(n_neighbors=3).fit(X, y)
distance, indices = plain.kneighbors([[3.2]])
print(pd.DataFrame({"input": X[indices[0], 0], "distance": distance[0], "target": y[indices[0]]}).round(3).to_string(index=False))
# TODO H04: 가까운 이웃에 큰 가중치를 주도록 변경하세요.
# 힌트: weights="distance"
weighted = KNeighborsRegressor(n_neighbors=3, weights="uniform")
weighted.fit(X, y)
print("uniform:", plain.predict([[3.2]]).round(2))
print("distance:", weighted.predict([[3.2]]).round(2))
print("역거리 가중 손계산:", round(np.average(y[indices[0]], weights=1 / distance[0]), 2))
