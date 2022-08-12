st1 = 'Print only the words that start with s in this sentence'

txt = st1.split()
for item in txt:
    if (item[0].lower() == 's'):
        print(item)


num=range(0,11)
#if (num%2==0):
for n in num:
    if n%2==0:
     print(n)

list=[x for x in range(1,50) if x%3==0]
print(list)


st = 'Print every word in this sentence that has an even number of letters'
r=st.split()

for item in r:
    if len(item)%2==0:
        print('even')
    else:
        print('odd')



last=range(1,100)

for num in last:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')

    if num%3 ==0:
        print('fizz')
        continue
    if num%5==0:
        print('buzz')
        continue
    else:
        print(num)


st3 = 'Create a list of the first letters of every word in this string'
c=st3.split()
d=[]
for item in c:
    d.append(item[0])
print(d)