
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



# customers = np.array([
#     [25, 45, 1],
#     [30, 60, 2],
#     [35, 75, 3],
#     [28, 50, 1],
#     [40, 85, 2]
# ])


a, b, c, d = 45, 5, 10, 940
smc = (a + d) / (a + b + c + d)
jaccard = a / (a + b + c)
print(smc, jaccard)