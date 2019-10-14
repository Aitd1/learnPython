'''
栈：
    1.进栈
    2.出栈
    3.查看栈顶元素
'''
class Stack():
    def __init__(self,limit = 10):
        self.lists=[]#定义一个栈
        self.limit=limit

    #进栈
    def push(self,data):
        '''
        1.检查进栈时：栈的大小是否超过栈的容量limit
        2.栈顶添加元素append()
        :param data:
        :return:
        '''
        if len(self.lists) >= self.limit:
            raise StopIteration('超出栈的大小了')
        else:
            self.lists.append(data)
    #出栈
    def pop(self):
        '''
        1.检测是否为空，不为空则弹出栈顶元素。使用方法是pop()。为空，抛出异常
        :return:
        '''
        if self.lists:
            return self.lists.pop()
        else:
            raise IndexError('栈已经为空了')
    #查看栈顶元素
    def peek(self):
        return self.lists[-1]
    #判断栈是否为空
    def isEmpty(self):
           return not bool(self.lists)
    #返回栈的大小
    def size(self):
        return len(self.lists)
#需求：字符串括号十分有效
def checkString(slits):
    '''
    思路：利用栈来解决
    1.字符串括号先将左括号进栈。
    2.当检测到右括号时，并检测栈是否为空，弹出进栈的左括号，如左边检测完了后，最后需要判断列表是否为空。为空返回true.不为空返回false.

    :param cstring: '((()))'
    :return:
    '''
    stack = Stack(len(slits))
    for i in slits:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.isEmpty():
                return False
            stack.pop()
    return stack.isEmpty()
if __name__ == '__main__':
    examples = ['((()))','(((())','(())))',"((((()))))"]
    for example in examples:
        bo = checkString(example)
        print(example+" :"+str(bo))

