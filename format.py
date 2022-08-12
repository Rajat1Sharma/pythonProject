#print('Hello this is {0} {2} {2}'.format('Rajat','kumar','Sharma'))

import math
#print('this ia is hasta lavista baby {0} {2}'.format('ff','rr','gg'))

list=[4,5,3,1,2,6,3,4,3,3,3]

#print(list[4][1])

#list.sort()

#list.append(89)
#list.pop(2)

#list.reverse()
#print(list[::])


#print(list)

tuple=(1,2,3,list)
print(tuple)


myset = set([1,1,2,3])

myset.add(1)
myset.add(2)
print(myset)

a = ((((10*5)**2)/10)+10)-159.75

print(a)

b=3+1.5+4

print(math.sqrt(b))

c='hello'


print(c[::-1])
print(c[1])
print()

mylist = [0,0,0]
print(mylist)


list3 = [1,2,[3,4,'hello']]

list3[2][2]='goodbye'

print(list3)

list4 = [5,3,4,6,1]
list4.sort()

print(list4)

#d = {'simple_key':'hello'}

#print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
#print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

