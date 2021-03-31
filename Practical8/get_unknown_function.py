function = open('/Users/user/IBI1_2020-21/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
seq = {}
for line in function:
	if line.startswith('>'):
		name = line.replace('>','').split()[0]
		seq[name] = ''
	else:
		seq[name] += line.replace('\n','').strip()

print(seq[name])
function.close()
