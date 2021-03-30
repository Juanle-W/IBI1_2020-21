protein = ''
seq = 'ATGCGACTACGATCGAGGGCC'
genetic_code = {'ATG':'M', 'CGA':'R', 'CTA':'L', 'TCG':'S', 'AGG':'R', 'GCC':'A'}
for i in range (0, len(seq), 3):
	codon = seq[i:i+3]
	protein = protein + genetic_code [codon]

print(protein)
