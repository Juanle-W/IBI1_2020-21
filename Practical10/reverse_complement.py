def reverse_complement (seq):
	abab={'A':'T', 'T':'A', 'C':'G', 'G':'C', 'c':'g', 'g':'c', 'a':'t', 't':'a'}
	bases=list(seq)
	complement_bases=[]
	reverse_complement_bases=[]
	for i in range(len(bases)):
		complement_bases.append(abab[bases[i]])
	for j in range(len(bases)):
		reverse_complement_bases.append(complement_bases[len(bases)-j-1])
	print('The reverse complement of a DNA strand is', end=' ')
	result=''.join(reverse_complement_bases)
	return print(result)

reverse_complement('ATCGGGTCag')
