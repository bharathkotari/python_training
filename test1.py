'''def sayhello(name):
    print("hello",name)
    def innerfunc(name):
        print("good evening ",name)
    return innerfunc
sayhello("bharath")
address=sayhello("kumar")
address('kotari')
print(">>>>>>>>>>>>>>>>>>>>")

def hi():
    return "i say hi"
def hello():
    return "i say hello"
def greeting(fn):
    greet=fn()
    print(greet)
greeting(hi)
greeting(hello)

print(">>>>>>>>>>>>>>>>>>>>")
def addwith(num1):
    def addresult(num2):
        return num1+num2
    return addresult
add10=addwith(10)
print(add10(9))

print(">>>>>>>>>>>>>>>>>>>>")

def mycounter():
	num=0
	def startcount():
		nonlocal num
		num=num+1
		print("current count is ",num)
	return startcount
c1=mycounter()
c1()

print(">>>>>>>>>>>>>>>>>>>>")
t1=lambda p,q:p**q
print(t1(3,4))

import math
sq_root=lambda x:math.sqrt(x)
print(sq_root(5))
print(">>>>>>>>>>>>>>>>>>>>")

check=lambda x:'big' if x>100 else 'small'
print(check(12))
print(check(120))
print(">>>>>>>>>>>>>>>>>>>>")

lst=list(map(lambda num:num**2,[2,3,4,5]))
print(lst)
print(">>>>>>>>>>>>>>>>>>>>")
ls1=list(map(lambda x,y,z:((x**2)/5+(y/z)),[3,4,5],[6,7,8],[10,12,33]))
print(ls1)

print(list(filter(lambda x:x**3<100,[3,4,5,6])))


lst=['zebra','lion','tiger']
print(list(filter(lambda x:x[1]=='i',lst)))

print(list(filter(lambda x:len(x)>4,lst)))

def testfun2(*printables):
	print(printables)
	for i in printables:
		print(i)
testfun2("delhi","goa","chennai","mysore")

def testfun3(*num):
	print(sum(num))
	
testfun3(10,20,30,40,50)

def testfun4(**capitals):
	print(capitals)
	for k,v in capitals.items():
		print(v,"is the capital of",k)
	if 'india' in capitals:
		print("the capital of india is {}".format(capitals['india']))
	else:
		print("country not specified")
		
testfun4(india='newdelhi',pakistan='islamabad')
def testfun5(*lst):
	#print(lst)
	temp=[]
	for i in lst:
		if type(i) is list:
			temp=temp+i
	return temp

list_stream=[[1,2,3],[4,5,6],"hellow","banglore",12,45,87,['a','b','c']]
#print(testfun5([1,2,3],[4,5,6],"hellow","banglore",12,45,87,['a','b','c']))

from functools import reduce
product=reduce((lambda x,y:x*y),[1,2,3,4])
print(product)

def mygenerator(n):
	for i in range(n):
		name='rank'+str(i)
		yield name 
		
l=mygenerator(5)
print(type(l))
for k in l:
	print(k)

def enclosure(func):
	def wrapper(x):
		print("this line is printed before executing the passed function")
		x=x+5
		func(x)
		print("this is after function execution")
	return wrapper

@enclosure
def incrementor(n):
	k=n+1
	print(k)

@enclosure
def mulwit7(n):
	k=n*7
	print(k)


incrementor(12)
mulwit7(5)'''
