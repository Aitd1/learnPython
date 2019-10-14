#列表，元组
def test(name,age,sex):
    print('我的名字叫：'+name+',我的年龄有：'+age+',我的性别是：'+sex)

list=('谢君','27','男')
test(*list)
#字典

def test1(name,age,sex):
    print('我的名字叫：' + name + ',我的年龄有：' + age + ',我的性别是：' + sex)
dictinfo={'name':'谢君','age':'27','sex':'男'}
test1(**dictinfo)