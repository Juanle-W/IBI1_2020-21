class Student:
	def __init__(self, first_name, last_name, programme):
		self.first_name=first_name
		self.last_name=last_name
		self.programme=programme
	def __str__(self):
		return "%s %s %s"%(self.first_name,self.last_name,self.programme)

a=Student('Wang', 'Juanle', 'BMS')
print(a)
