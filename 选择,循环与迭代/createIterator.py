#空的迭代对象：
import collections.abc as c

class BecomeIterator:

    def __iter__(self):
        return None

becomeIterator =BecomeIterator()
print(isinstance(becomeIterator,c.Iterable))