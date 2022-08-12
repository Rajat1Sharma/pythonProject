import os

list1=[1,2,3,4,5,6,7,8,9,44,23423,55]

even=[]
odd=[]
for num in list1:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)
#print("Event list is :",even)
#print("Odd list is :",odd)

for num in range(0,101):
   os.system(f"touch file_{num}")








