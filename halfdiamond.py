n=10

for i in range(0,5):
    for j in range(0,i):
        print('*',end='')
    print('\r')
for k in range(0,i):
    for j in range(0,i):
        print('*',end='')
    i=i-1
    print('\r')





