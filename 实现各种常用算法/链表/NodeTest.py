#创建一个None节点类
class Node:
    def __init__(self,data):
        self.next=Node
        self.data=data

class Linked_list:
    def __init__(self,head=None):
        self.head=head

    #链表添加一个元素
    def append(self,new_element):
        current = self.head #不可以用
        if self.head:
            while current.next:#current.next：表示指针向前移动了，最后一个current.next 为None 即false.
                current = current.next ##将前一个节点的指针向向前移动一位，即等于下一位。
            current.next = new_element #将新元素链点复制给链表的最后一个节点的链点
        else:
            self.head=new_element #新元素作为链表的第一个节点。jiedian
    def is_empty(self):
        '''
        判断是否为空。 True 表示不为空， False:表示为空。
        :return:
        '''
        return bool(self.head)

    def insert(self,position,new_element):
        '''
        需求：向链表中任意插入一个新元素。
        思路：
            1.先判断要插入的位置是否在链表索引范围内。
            2.当插入的位置是头结点(索引为0)时，作特殊情况处理
            3.当要插入结点的位置并不在0时，找到要插入的位置，插入新结点
        :param position: 序号
        :param new_element: 插入新元素
        :return:
        '''
        if position <0 or position > self.get_length():
            raise IndexError('insert 插入时，key的值超出了范围')
        temp = self.head #不可以用head来遍历列表 否则会丢失列表的一些节点 以使用和head相同类型的索引变量：curren
        #将插入元素的next属性只想老的结点，并且将新的元素复制给头结点。
        if position == 0:
            new_element.next = temp;
            self.head = new_element
            return
        i = 0
        while i<position:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = new_element
        new_element.next = temp
        #删除任意位置的一个元素
    def remove(self,position):
        if position<0 or position > self.get_length():
            raise IndexError("删除元素的索引超过范围")
        i = 0
        temp = self.head
        while temp !=None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return
            pre = temp
            temp = temp.next
            i+=1
            if i ==position:
                pre.next = temp.next
                temp.next =None
                return

    def get_length(self):
        """
        返回链表的长度
        """
        #头部结点赋值给头部结点
        temp = self.head
        # 计算链表的长度变量
        length = 0
        while temp != None:
            length = length + 1
            temp = temp.next
        # 返回链表的长度
        return length

    def print_list(self):
        """
        遍历链表，并将元素依次打印出来
        """
        print("linked_list:")
        # 头部结点赋值给临时变量 temp
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        """
        将链表反转
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def initlist(self, data_list):
        """
        将列表转换为链表
        """
        # 创建头结点
        self.head = Node(data_list[0])
        temp = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next