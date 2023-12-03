import matplotlib.pyplot as plt

amount_over_threshold = 33

splitting_points = [0, 19, amount_over_threshold]
barchart_height = [1, 1, 1]  

labels = ['Anzahl Sequenzen mit Zitaten', 'Anzahl Sequenzen ohne Zitaten']
colors = ['skyblue', 'orange', 'lightgreen']

barchart_values = [19, amount_over_threshold - 19]

plt.figure(figsize=(8, 1.5))  

for i in range(len(splitting_points) - 1):
    plt.barh(0, splitting_points[i + 1] - splitting_points[i], left=splitting_points[i], height=barchart_height[i], color=colors[i], label=labels[i])
    plt.text(splitting_points[i] + (splitting_points[i + 1] - splitting_points[i]) / 2, 0, str(barchart_values[i]), ha='center', va='center', weight='bold')

plt.axis('off')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.025), fancybox=True, shadow=False, ncol=2)
plt.show()
