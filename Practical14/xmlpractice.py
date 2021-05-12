#import DOM module
from xml.dom.minidom import parse
import xml.dom.minidom
#parse the file
DOMTree=xml.dom.minidom.parse('/Users/user/Downloads/go_obo.xml')
#get the root element
total=DOMTree.documentElement
#get a list of elements for different genes
terms=total.getElementsByTagName('term')
count1=0
count2=0
count3=0
count4=0
#get the number of childNodes for DNA-related gene ontology terms, reference: https://www.cnblogs.com/zlstg/articles/14095898.html
for n in range (terms.length):#reference: https://www.cnblogs.com/poloyy/p/12207464.html
	if 'DNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:#get the defstr information by only getting the node of defstr and change the type from nodelist to node so that '.data' can be used
		count1=count1+terms[n].childNodes.length

#repeat for RNA and protein
for n in range (terms.length):
	if 'RNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count2=count2+terms[n].childNodes.length

for n in range (terms.length):
	if 'protein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		count3=count3+terms[n].childNodes.length

#the fourth macromolecule: glycoprotein
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
