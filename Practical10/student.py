#build a class
class Student(object):
	def __init__(self, first_name, last_name, programme):#to initialize three data attributes, which are the first name, the last name and the undergraduate programme
		self.first_name=first_name
		self.last_name=last_name
		self.programme=programme
	def __str__(self):#to output the student's full name and undergraduate programme
		return "full name: %s %s; undergraduate programme:  %s"%(self.first_name,self.last_name,self.programme)#I got the idea from "https://blog.csdn.net/pdstar/article/details/90900944"

#give an instance
a=Student('Wang', 'Juanle', 'BMS')
print(a)
