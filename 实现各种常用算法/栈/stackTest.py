class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        '''
            思路：
            理解：压入push:即将新的元素放在栈顶
            步骤：
                1.检查栈是否溢出。溢出并抛出异常。
                2.然后添加新元素。
        '''
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        '''
        出栈：即移出栈顶的元素。使用pop()方法,同时能获取移出的新元素。
        步骤:
            1.判定栈是否为空栈，if self.stack :
            2.不为空则，返回移出的新元素 return self.stack.pop()；为空，则抛出异常。
        '''
        if self.stack:  # 判断列表是否为空
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')  # 空栈不能被弹出
    #添加其他函数：
    '''
    需求：
    1.查看栈顶的元素。
    2.判断栈是否为空
    3.返回栈的大小
    '''
    def peek(self):
        if self.stack:
            return self.stack[len(self.stack)-1]
            # return self.stack[-1]
    def is_empty(self):
        #
         return not bool(self.stack)

    def size(self):
        #返回栈的大小.
        return len(self.stack)

def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

if __name__=='__main__':
    examples = ['((()))','((())','(()))']
    print('Balanced parenrheses demonstartion:\n')
    for example in examples:
        print(example+': '+ str(balanced_parentheses(example)))