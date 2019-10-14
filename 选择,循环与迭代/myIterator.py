class MyIterator():
    def __init__(self):
        self.list=[]
        self.position =0
    def add_name(self,name):
        self.list.append(name)
    def __iter__(self):
        return self  #返回一个迭代器
    '''
    迭代思路：
        1.获取迭代对象的值。需要获取下标position. list[position]
        2.每调用一次next()方法，迭代一次，前进一个元素，故position 需要加1 即position +=1;
        3.判断position是否会超过len(list)，超过将保存，即抛出异常StopIteration错误。故需要做个选择。
    '''
    def __next__(self):
        if self.position < len(self.list):
            item = self.list[self.position]
            self.position+=1
            return item
        else:
            raise StopIteration
#person 即是迭代器也是迭代对象。
person = MyIterator()
person.add_name('张山')
person.add_name('小名')
person.add_name('王无')
person.add_name('里斯')

print(person.__next__())
print(person.position)
print(person.__next__())
print(person.position)
print(person.__next__())
print(person.position)
#验证humen是一个迭代对象。
humen = MyIterator()
humen.add_name('1')
humen.add_name('2')
humen.add_name('3')
humen.add_name('4')
humen.add_name('5')

iterator = iter(humen)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
