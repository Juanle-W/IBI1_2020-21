#input and output two fa files
f = open('/Users/user/IBI1_2020-21/Practical8/unknown_function.fa')
fw = open('/Users/user/IBI1_2020-21/Practical8/unknown_protein.fa','w')
#read the lines in the unknown_function.fa file
line = f.readlines()
name = []
protein = []
#similar way to translate dna sequence into protein sequence as DNA_to_protein.py
genetic_code = {
'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U',
'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z',
'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K',
'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
#get information of name and DNA sequence seperately as well as translating DNA sequence into protein sequence
for i in range (len(line)):
	if line[i].startswith('>'):
		name.append(line[i].split(' ')[0])
	else:
		dnaseq = line[i].replace('\n', '')
		proseq = ''
		for j in range (0, len(dnaseq), 3): #similar to the way in DNA_to_protein.py
			codon = dnaseq[j:j+3]
			proseq += genetic_code[codon]
		protein.append(proseq)

f.close()
#write the output fa file
for i in range (len(name)):
	fw.write(name[i])
	fw.write(' ')
	fw.write(str(len(protein[i])))
	fw.write('\n')
	fw.write(protein[i])
	fw.write('\n')

fw.close()	
