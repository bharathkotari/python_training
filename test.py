'''def fun(n1):
    def fun2(n2):
      # nonlocal n1
      # n1=n1+n2
        return fun3
    def fun3(n3):
        return n1+n3
    return fun2
a=fun(10)
b=a(8) 
c=b(2)
print(c,b,a)'''



i='global value'
def A():
	i='enclosed_value'
	def b():
		nonlocal i
		print("im non local",i)
		i='local value'
		print(i)
	b()
print(i)
A()