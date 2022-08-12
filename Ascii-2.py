# n=10
#
# k=65+n
#
# for i in range(65,k):          #--------> i=65
#     for j in range(65,k):  #--------> i=65,j=65
#         if i<j:
#             print('',end='')
#             #print('')
#         else:
#             print(chr(j),end='')   #--------> i=65
#
#     i+=1
#
#
#     print('\r')

a=65
n=7
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(a),end='')
        a = a+1
    print()

