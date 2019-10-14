def my_max(x,y):
    return x if(x>y) else y

#i = my_max(1,2)
#print(i)
def demo(obj):
    obj += obj
    print('形参的值：',obj)
print('----值传递------')
a = "C语言中文网"
print("a的值为：",a)
demo(a)
print("实参值为：",a)
print("-----引用传递-----")
a = [1,2,3]
print("a的值为：",a)
demo(a)
print("实参值为：",a)

