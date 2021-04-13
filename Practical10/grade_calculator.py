def student(name, code, poster, exam):
	total_mark=code*0.4+poster*0.3+exam*0.3
	print('name: ',name, end='; ')
	print('total mark: ',str(total_mark))
	return

student(name='Mike',code=89,poster=78,exam=79)
