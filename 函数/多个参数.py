def test(b,*args):
    # print(b)
    for a in args:
        print(a)

# test('123','q','w','e','r','t')
def test02(**kwargs):
    for i in kwargs.keys():
        print(i)
        print(kwargs.get(i))


test02(name='xie',name2='xie2',name6='xie',name3='xie',name4='xie',name5='xie')

