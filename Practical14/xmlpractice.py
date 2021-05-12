from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse('/Users/user/Downloads/go_obo.xml')
total=DOMTree.documentElement
terms=total.getElementsByTagName('term')
count1=0
count2=0
count3=0
count4=0
for n in range (terms.length):
	if 'DNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count1=count1+terms[n].childNodes.length

for n in range (terms.length):
	if 'RNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count2=count2+terms[n].childNodes.length

for n in range (terms.length):
	if 'protein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count3=count3+terms[n].childNodes.length

for n in range (terms.length):
	if 'glycoprotein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count4=count4+terms[n].childNodes.length

print('The number of childNodes associated with "DNA" is ', str(count1))
print('The number of childNodes associated with "RNA" is ', str(count2))
print('The number of childNodes associated with "protein" is ', str(count3))
print('The number of childNodes associated with "glycoprotein" is ', str(count4))

import matplotlib.pyplot as plt
labels='DNA', 'RNA', 'protein', 'glycoprotein'
sizes=[count1, count2, count3, count4]
explode=(0, 0, 0, 0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and glycoprotein')
plt.show()
