import re
f = open('/Users/user/IBI1_2020-21/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fw = open('/Users/user/IBI1_2020-21/Practical8/unknown_function.fa','w')
seq = {}
for line in f:
	if line.startswith('>'):
		name = line.split()[0].split('_')[0]
		seq[name] = ''
	else:
		seq[name] += line.replace('\n','').strip()

f.close()

for i in  seq.keys():
	fw.write(i)
	fw.write(' ')
	fw.write(str(len(seq[i])))
	fw.write('\n')

f.close()
