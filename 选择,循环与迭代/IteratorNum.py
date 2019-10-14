class MyNumber():
    def __init__(self):
        self.i=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<20:
            self.i +=1
            return self.i
        else:
            raise StopIteration

person = MyNumber()

it = iter(person)

for  x in it:
    print(x)