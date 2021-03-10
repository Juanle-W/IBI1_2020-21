a=031202
b=190784
c=100321
d=abs(c-a)
e=abs(b-a)
if d>e:
        print('d is greater')
else:
        print('e is greater')
X=True
Y=False
Z=(X and not Y) or (Y and not X)
print Z==True
W=X!=Y
print Z==W
