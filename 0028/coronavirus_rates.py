#input the tatal number of cases in the five countries as a list
cases = {'USA':29967939, 'India':11305979, 'Brazil':11284269, 'Russia':4360823, 'UK':4241677}
#import the module we need to use
import matplotlib.pyplot as plt
#draw a pie chart
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK' #set the caption displayed on the outside of the pie chart
sizes = [29967939, 11305979, 11284269, 4360823, 4241677] #set the proportion for the five countries
explode = (0.1, 0, 0, 0, 0) #highlight the USA section
plt.pie(sizes,explode=explode, labels=labels, autopct = '%1.1f%%', shadow=False, startangle=90) #display one digit after the decimal point; not draw shadow; start drawing from the positive y-direction
plt.axis('equal') #make the pie chart equal in length and width
plt.show() #show the pie chart 