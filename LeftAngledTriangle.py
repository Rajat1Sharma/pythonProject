n=5
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k=k-2
    for j in range(0,i+1):
       print('* ',end='')
    print('\r')

p=5
X = 2 * p - 2
for m in range(0, p):
    for n in range(0, X):
        print(end="")
    X = X - 2
    for n in range(0, m + 1):
        print("* ", end="")
    print("\r")