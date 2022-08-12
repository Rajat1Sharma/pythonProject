def myfunc(*args, **value):
    print(args)
    print(value)
    print('I like {} {}'.format(args[1],value['animal']))




def myfunc2(**kwargs):
    for item in kwargs:
        print(kwargs)



myfunc(8,22,44, fruits='orange',food='dosa',animal='wefwef')
#myfunc2(book='everyone has a life', book2='everyone has a life', book3='everyone has a life')


