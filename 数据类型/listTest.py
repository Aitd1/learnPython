list1 = ['Google', 'Runoob', 'Taobao']
list2 = ['1', '2', '3']
list2.extend(list1)
# list2.append(list1)
print(list2)
list2.insert(5,'3')
print(list2)
list2.remove('3')
print(list2)
#remove element
list2.remove('Runoob')
print(list2)
print(list2.pop())
print(list2)
print(list2.pop(0))
print(list2)