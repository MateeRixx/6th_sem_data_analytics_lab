import matplotlib.pyplot as plt

activities = ['Watching Videos', 'Creating Content', 'Messaging', 'Shopping']
percentages = [60.2, 23.1, 11.1, 5.6]
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96c93d']

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(percentages, labels=activities, autopct='%1.1f%%',
                                 startangle=90, colors=colors, pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('How Typical TikTok Users Spend Their Daily Time\n(108 minutes total per day)', fontsize=14, fontweight='bold')
plt.axis('equal')

plt.show()