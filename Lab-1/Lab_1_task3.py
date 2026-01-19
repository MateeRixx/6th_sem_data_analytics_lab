import matplotlib.pyplot as plt

sales = [45, 52, 48, 55, 60, 58, 62, 65, 70, 68, 72, 150]

plt.figure(figsize=(10, 6))
plt.hist(sales, bins=10, edgecolor='black', color='skyblue')

plt.title('Histogram of Monthly Sales (in $1000)', fontsize=14, fontweight='bold')
plt.xlabel('Monthly Sales ($1000)', fontsize=12)
plt.ylabel('Number of Months (Frequency)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')

plt.show()