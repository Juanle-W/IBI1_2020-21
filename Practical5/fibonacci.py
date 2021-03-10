#set the first two variables as 1, 1
a=1
b=1
#repeat adding the previous two numbers, use the sum of the previous two number as the next number
#since a represents two number before the number I want, I should replace a value with the current b value. 
#Also I should replace b value with the current c value. 
#Finally I get the 13th value and show it as c value.
for i in range (3,14):
        c=a+b
        a=b
        b=c
        i=i+1
print c
