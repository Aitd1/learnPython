dict = {"Alice":"1234","Beth":"9102","Cecil":"123","Alice":'xiejun'}
print(type(dict))
print(dict)

x = dict.get("Alice",None)
print(x)

y = dict.get("aAlice","xie")
print(y)
radiansdict = dict.copy()
print(radiansdict)
# radiansdict.clear()
print(radiansdict)
if "xiejun" in dict:
    print("key have xiejun ")
else:
    print("key havd not xiejun")
radiansdict.popitem()
print(radiansdict)


dictlist = radiansdict.values()
print(list(dictlist))
dict.update(radiansdict)
print(dict)
print(dict.setdefault('zs','asd'))
print(dict)
tupledict = dict.items()
for i in tupledict:
    print(i)
    print(i[0]+" : "+i[1])




