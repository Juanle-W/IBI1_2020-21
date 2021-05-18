from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse('/Users/user/Downloads/go_obo.xml')
total=DOMTree.documentElement
terms=total.getElementsByTagName('term')
#get the idea of use a dictionary from my classmate Wang Zhouyue
idis={}#use a dictionary to store the relationship between id and is_a
#establish the dictionary
for n in terms:#get id and is_a information from each term
	isa=n.getElementsByTagName('is_a')#as a list since there may be more than 1 go_id in is_a tag
	goid=n.getElementsByTagName('id')[0]
	for i in isa:
		if i.childNodes[0].data in idis:
			idis[i.childNodes[0].data].append(goid.childNodes[0].data)#thus, one key can have more than one value
		else:
			idis[i.childNodes[0].data]=[goid.childNodes[0].data]

#get the id of the terms about 'DNA', reference: https://www.cnblogs.com/zlstg/articles/14095898.html
DNAlist=[]
for n in range (terms.length): #reference: https://www.cnblogs.com/poloyy/p/12207464.html
	if 'DNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:##get the defstr information by only getting the node of defstr and change the type from nodelist to node so that '.data' can be used
		DNAlist.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

#repeat for RNA and protein
RNAlist=[]
protein=[]
carbohydrate=[]
for n in range (terms.length):
	if 'RNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		RNAlist.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

for n in range (terms.length):
	if 'protein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		protein.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)
	elif 'Protein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		protein.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

#the fourth macromolecule: carbohydrate
for n in range (terms.length):
	if 'carbohydrate' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		carbohydrate.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)
	elif 'Carbohydrate' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
		carbohydrate.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

#run a recursion to find the childnodes of terms about the molecules we need
def nodenumber(idis,molelist):
	child=[]
	for i in molelist:
		if i in idis:
			childnode=idis[i]
			child+=childnode
			child+=nodenumber(idis,childnode)
	return child

dna_length=len(set(nodenumber(idis,DNAlist)))#use "set()" to remove repeating parts
rna_length=len(set(nodenumber(idis,RNAlist)))
p_length=len(set(nodenumber(idis,protein)))
c_length=len(set(nodenumber(idis,carbohydrate)))

print('The number of childNodes of DNA-associated terms is ',str(dna_length))#8651
print('The number of childNodes of RNA-associated terms is ',str(rna_length))#11004
print('The number of childNodes of protein-associated terms is ',str(p_length))#33459
print('The number of childNodes of carbohydrate-associated terms is ',str(c_length))#4879

import matplotlib.pyplot as plt
labels='DNA', 'RNA', 'protein', 'carbohydrate'
sizes=[dna_length,rna_length,p_length,c_length]
explode=(0, 0, 0, 0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and carbohydrate')
plt.show()
