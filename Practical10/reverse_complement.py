#make a function
def reverse_complement (seq):
	abab={'A':'T', 'T':'A', 'C':'G', 'G':'C', 'c':'g', 'g':'c', 'a':'t', 't':'a'}
	bases=list(seq)#change the string type into the list type
	complement_bases=[]#build a list to store the complement bases
	reverse_complement_bases=[]#build a list to store the reverse complement bases
	for i in range(len(bases)):
		complement_bases.append(abab[bases[i]])#to get the complement bases
	for j in range(len(bases)):
		reverse_complement_bases.append(complement_bases[len(bases)-j-1])#to reverse the complement bases
	print('The reverse complement of a DNA strand is', end=' ')
	result=''.join(reverse_complement_bases)#change the list type to the string type
	return print(result)

reverse_complement('ATCGGGTCag')
