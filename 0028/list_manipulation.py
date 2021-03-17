#before starting, modules should be imported
import numpy as np
import matplotlib.pyplot as plt
#input two lists of values as requested
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#turn list type into array type so that gene lengths can be divided by exon counts
gene_lengths=np.array(gene_lengths)
exon_counts=np.array(exon_counts)
average_exon_lengths=gene_lengths/exon_counts
#turn array type into list type
average_exon_lengths=list(average_exon_lengths)
#draw a boxplot
n = 10
score = average_exon_lengths
plt.boxplot(score,
	vert = True, #place the boxplot vertically 
	whis = 2, #specifies the distance between the upper and lower quartiles as 2
	patch_artist = True, #fill the color of the boxplot
	meanline = False, #not going to write the mean as a line
	showbox = True, #the box is shown in the boxplot
	showcaps = True, #show the two lines at the top and end of the boxplot
	showfliers = False, #not diaplay outliers
	notch = False #The boxplot is not presented in the form of notches
	)
plt.show() #show the boxplot