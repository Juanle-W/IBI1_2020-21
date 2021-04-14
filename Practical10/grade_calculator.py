def student(name, code, poster, exam):
	total_mark=code*0.4+poster*0.3+exam*0.3#calculate the total mark
	return name + ' ' + str(total_mark)

#give an instance
a=student(name='Mike',code=89,poster=78,exam=79)
print(a)
