n=10
k= n-1
for i in range(0,n):        #i=0 -------> Is loop se spacess milenge saari rows k liye
    for j in range(0,k):    #i=0,j=0 ---> is loop se hme position milegi ki kaha star print krna h
        print(end=' ')

    k=k-1
    for j in range(0,i+1):  #---> is loop se hme no. of stars milenge ki kitna print krna h
        print('* ',end='')

    print('\r')

