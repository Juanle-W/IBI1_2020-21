#input and output fa files
f = open('/Users/user/IBI1_2020-21/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fw = open('/Users/user/IBI1_2020-21/Practical8/unknown_function.fa','w')
#read the Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa file
line = f.readlines()
seq = []
name = []
for i in range (len(line)):
	if line[i].startswith('>') and line[i].find('unknown function')>=0:
		name.append(line[i].split()[0].split('_')[0])
	elif line[i-1].startswith('>') and line[i-1].find('unknown function')>=0:
		partseq = '' #prevent accumulating of the sequences from different genes 
#try to get all lines that have information about the DNA sequence of one gene
#use for loop and if loop to get which lines have sequence information
		for j in range (i,len(line)):
			if line[j].startswith('>'):
				break
			else:
				partseq += line[j].replace('\n','').strip() #store all information from different lines in one string called partseq
		seq.append(partseq) #put the sequence of one gene into the list
print(name) #check if the loop works normally
f.close()
#write the output file
for i in range (len(name)):
	fw.write(name[i])
	fw.write(' ')
	fw.write(str(len(seq[i])))
	fw.write('\n')
	fw.write(seq[i])
	fw.write('\n')

f.close()
