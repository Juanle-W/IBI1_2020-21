cases = {'USA':29967939, 'India':11305979, 'Brazil':11284269, 'Russia':4360823, 'UK':4241677}
import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29967939, 11305979, 11284269, 4360823, 4241677]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes,explode=explode, labels=labels, autopct = '%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()