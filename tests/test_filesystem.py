import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = os.path.join(path, 'data')

print(data)

class Test():
    def __init__(self):
        self = self

    def __str__(self):
        self.name = self


foo = Test()
print(foo.name)
