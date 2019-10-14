def sum_and_avg(list):
    count = 0
    sum = 0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):
            sum+=e;
            count+=1;
    return sum,sum/count

mylsit=[12,32,43,54,3,'t',34,23,12]
# result = sum_and_avg(mylsit)
# for e in result:
#     print(e)
e,avg=sum_and_avg(mylsit)
print(e)
print(avg)