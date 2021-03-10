#set the first two variables as 1, 1
n1=1
n2=1
#repeat adding the previous two numbers, use the sum of the previous two number$
for i in range (3,14):
        n3=n1+n2
        n1=n2
        n2=n3
        i=i+1
print n3
