#mylist=('Hello Master Yoda')

def master_yoda(mylist):
    seperate_list=mylist.split()
    print(seperate_list)
    reverse_list=seperate_list[::-1]
    print(reverse_list)
    print(' '.join(reverse_list))


#master_yoda('Hello Dear how are you')

def has_33(mynums):
    for i in range(0, len(mynums)-1):
        if mynums[i] ==3 and mynums[i+1] ==3:
            print('this has 33')
        else:
            pass

#has_33([2,3,4,5,6,7,8,3,3,5,6,7])


def every_letter_three_times(text):
    result = ''
    for char in text:
        result += char*3
    print(result)

every_letter_three_times('Akanksha')
