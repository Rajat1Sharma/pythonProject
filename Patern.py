list1 = ["abc1",100]
a,b=list1
l=len(a)
print(l)
z=a[0:l-1]
print(z)
for x in range(0,5):
    print(z+str(x+1),b+x)