import matplotlib.pyplot as plt

platforms = ['TikTok', 'Instagram', 'YouTube', 'Facebook', 'Twitter/X', 'Others']
percentages = [32, 28, 22, 10, 5, 3]
colors = ['#ff0050', '#e1306c', '#ff0000', '#1877f2', '#1da1f2', '#aaaaaa']

plt.figure(figsize=(6, 6))
plt.pie(percentages, labels=platforms, autopct='%2.5f%%', startangle=90, colors=colors, shadow=True)

plt.title('Market Share of Social Media Platforms\n(Among 1,000 Internet Users Aged 18–35)', fontsize=10, fontweight='bold')
plt.axis('equal')

plt.show()