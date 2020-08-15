import sub1.client1 as cli1
import sub2.client2 as cli2


def func(name):
    return f"hello {name}"


a = cli1.func1(1, 2)
b = cli2.func2(1, 2)
print(a)
print(b)
