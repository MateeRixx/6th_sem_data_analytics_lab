
hours = [2, 3, 5, 7, 9, 11, 12, 15]
scores = [55, 60, 68, 75, 80, 85, 88, 92]

n = len(hours)


mean_hours = sum(hours) / n
mean_scores = sum(scores) / n


covariance = sum((hours[i] - mean_hours) * (scores[i] - mean_scores) for i in range(n)) / n
print(f"Covariance: {covariance:.2f}")


var_hours = sum((x - mean_hours) ** 2 for x in hours) / n
var_scores = sum((y - mean_scores) ** 2 for y in scores) / n
import math
std_hours = math.sqrt(var_hours)
std_scores = math.sqrt(var_scores)
pearson = covariance / (std_hours * std_scores)
print(f"Pearson correlation: {pearson:.2f}")