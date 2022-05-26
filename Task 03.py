import functools
l1 = [ x for x in range(0,20) if x%2 == 0 ]
print(l1)

s1 = { x%10 for x in range(0,20) }
print(s1)

d1 = { v:k for (k,v) in zip(s1,l1) }
print(d1)

l1 = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x+10,l1)))
print(list(filter(lambda x:x<5,l1)))
print(functools.reduce(lambda x,y:x+y, l1))


list1 = ["Magic Coat","Blaze","Torrent","Sap Sipper","Overgrow"]

mylist = iter(list1)

print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))


def mygenerator():
    print("hello")
    yield 1
    for i in range(0,20):
        print(i)
    print("world")
    yield 2
    yield 3
x = mygenerator()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x)


def add(func):
	def inner(*args, **kwargs):
		x = func(*args, **kwargs)
		return x+x
	return inner

def mul(func):
	def inner(*args, **kwargs):
		x = func(*args, **kwargs)
		return x*x
	return inner
@add
@mul
def num():
	return 10

print(num())

import re
def first(func):
	def compare():
		x,y = func()
		if x == y:
			return True
		else:
			return False
	return compare
	
def second(func):
	def extract():
		x,y = func()
		a = re.findall(r'[0-9]',x)
		b = re.findall(r'[0-9]',y)
		return a,b
	return extract

@first
@second
def input_str():
	return "Kunj1234","1234krbg"

print(input_str())