import re
f = open('/Users/user/IBI1_2020-21/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fw = open('/Users/user/IBI1_2020-21/Practical8/unknown_function.fa','w')
line = f.readlines()
seq = []
name = []
for i in range (len(line)):
	if line[i].startswith('>') and line[i].find('unknown function')>=0:
		name.append(line[i].split()[0].split('_')[0])
	elif line[i-1].startswith('>') and line[i-1].find('unknown function')>=0:
		partseq = ''
		for j in range (i,len(line)):
			if line[j].startswith('>'):
				break
			else:
				partseq += line[j].replace('\n','').strip()
		seq.append(partseq)			
print(name)
f.close()

for i in range (len(name)):
	fw.write(name[i])
	fw.write(' ')
	fw.write(str(len(seq[i])))
	fw.write('\n')
	fw.write(seq[i])
	fw.write('\n')

f.close()
