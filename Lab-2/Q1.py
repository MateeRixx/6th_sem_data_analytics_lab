import numpy as np
import pandas as pd
from itertools import combinations
from math import sqrt, log
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



customers = np.array([
    [25, 45, 1],
    [30, 60, 2],
    [35, 75, 3],
    [28, 50, 1],
    [40, 85, 2]
])


age_income = customers[:, :2]
dissimilarity = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        dissimilarity[i][j] = sqrt(
            (age_income[i][0] - age_income[j][0]) ** 2 +
            (age_income[i][1] - age_income[j][1]) ** 2
        )

print(dissimilarity)