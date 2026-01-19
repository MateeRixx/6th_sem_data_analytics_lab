import matplotlib.pyplot as plt

sizes = [1500, 1800, 1200, 2200, 1400, 2000, 1700, 1300, 1900, 1600]
prices = [300000, 350000, 250000, 450000, 280000, 400000, 320000, 260000, 380000, 310000]

plt.figure(figsize=(10, 6))
plt.scatter(sizes, prices, color='teal', s=100, alpha=0.7)

plt.title('Relationship between House Size and Price', fontsize=14, fontweight='bold')
plt.xlabel('House Size (square feet)', fontsize=12)
plt.ylabel('House Price ($)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.show()