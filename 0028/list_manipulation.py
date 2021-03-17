import numpy as np
import matplotlib.pyplot as plt
average_exon_lengths=[9410/51,394141/1142,4442/42,105338/216,19149/25,76779/650,126550/32553,36296/57,842/1,15981/523]
n = 10
score = average_exon_lengths
plt.boxplot(score,
	vert = True,
	whis = 1.5,
	patch_artist = True,
	meanline = False,
	showbox = True,
	showcaps = True,
	showfliers = True,
	notch = False
	)
plt.show()