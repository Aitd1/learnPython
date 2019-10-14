'''
这是我们编写的第一个模块，该模块包含以下内容：
my_book：字符串变量
say_hi：简单的函数
User：代表用户的类
'''
#变量
print("这是一个自定义模块")
my_book='Python入门教材';
#方法
def say_hi(user):
    print('%s,您好，欢迎学习python' %user)
#类
class User:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print('%s正在慢慢的走路：' %self.name)
    def __repr__(self):
        return 'User[name=%s]'%self.name

#自定义模块测试代码
if __name__=='__main__':
    def test_my_book():
        print(my_book)
    def test_say_hi():
        say_hi('Mary')
        say_hi(User('Charlie'))
    def test_User():
        u = User('Liyi')
        u.walk()
        print(u.name)

    test_my_book()
    test_say_hi()
    test_User()
