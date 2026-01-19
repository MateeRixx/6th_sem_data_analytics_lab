
#part-1


import matplotlib.pyplot as plt

stores = ['A', 'B', 'C', 'D', 'E', 'F']
total_sales = [177.3, 207.6, 156.0, 231.1, 192.2, 171.0]

plt.figure(figsize=(10, 6))
bars = plt.bar(stores, total_sales, color='cornflowerblue')

plt.title('Total Weekly Sales by Store (in $1000)', fontsize=14, fontweight='bold')
plt.xlabel('Store', fontsize=12)
plt.ylabel('Total Sales ($1000)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}', ha='center')

plt.show()

#part-2


import matplotlib.pyplot as plt
import numpy as np

stores = ['A', 'B', 'C', 'D', 'E', 'F']
wed_sales = [18.5, 22.1, 16.9, 24.8, 20.2, 18.3]
sat_sales = [45.8, 52.1, 39.5, 58.3, 48.7, 42.9]

x = np.arange(len(stores))
width = 0.35

fig, ax = plt.subplots(figsize=(11, 6))
ax.bar(x - width/2, wed_sales, width, label='Wednesday', color='mediumseagreen')
ax.bar(x + width/2, sat_sales, width, label='Saturday', color='tomato')

ax.set_title('Wednesday vs Saturday Sales Comparison Across Stores', fontsize=14, fontweight='bold')
ax.set_xlabel('Store', fontsize=12)
ax.set_ylabel('Sales ($1000)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend(title='Day of Week')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

#part-3

import matplotlib.pyplot as plt
import numpy as np

categories = ['Grocery', 'Dairy', 'Meat & Poultry', 'Bakery', 'Beverages', 'Others']
store_a = [35, 20, 15, 12, 10, 8]
store_b = [32, 22, 16, 14, 9, 7]
store_c = [38, 18, 14, 13, 11, 6]

x = np.arange(3)
bottom = np.zeros(3)

fig, ax = plt.subplots(figsize=(10, 7))

colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948']

for i, cat in enumerate(categories):
    ax.bar(x, [store_a[i], store_b[i], store_c[i]], bottom=bottom, label=cat, color=colors[i])
    bottom += [store_a[i], store_b[i], store_c[i]]

ax.set_title('Product Category Distribution by Store (Percentage)', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage of Total Sales (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(['Store A', 'Store B', 'Store C'], fontsize=11)
ax.legend(title='Category', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.show()