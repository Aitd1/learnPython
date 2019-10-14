class Stack():
    #初始化变量
    def __init__(self,limit=10):
        self.lists=[] #创建一个空栈
        self.limit=limit #定义栈的容量大小
    #进栈
    #判断入栈的时候，栈的大小是否超过了容量。
    def push(self,data):
        if self.limit > len(self.lists):
            self.lists.append(data)#添加新元素入栈
        else:
            raise IndexError('超出栈的容量大小了')
    #出栈
    #判断栈是否为空，list为空，状态为false。
    #不为空，则弹出栈顶元素。是用(pop())
    def pop(self):
        if self.lists:
            self.lists.pop()
        else:
            raise IndexError("pop from")
