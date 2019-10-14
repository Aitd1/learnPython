info1 = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(info1)):
    info1[i]+=1
print(info1)

info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = map(lambda x:x+1,info)
print(a)
for i in a:
    print(i)