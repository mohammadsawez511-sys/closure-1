def counter():
    n=0
    def count():
        nonlocal n
        n+=1
        return n
    return count
x=counter()
print(x())
print(x())
print(x())
print(x())

def example():
    n=100
    def inner():
        m=10
        return m*n
    return inner
x = example()
print(x())