#a = {2,3}
#b = {55,44}
#c = {1,2}
# c=a.union(b)

#d = "a"}, {"b"}, {"c"}}
#d=[a,b,c]
#print(d)

def spy_game(nums):
    code =[0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    print(len(code) == 1)

#spy_game([1,2,3,4,0,4,4,7,6,8])

def check_primes(nums):
    if the nums <= 2:
        print('0')

    for num in nums()






