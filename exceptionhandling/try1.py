#while True:
j=100	

try:
	
	print("money "+str(j)+" present")
	5/0
except ZeroDivisionError:
	print("cannot divide by zero")
except TypeError:
	print("typecast error ")
except:
	print("some error")
else:
	print("try success")
finally:
	print("finally!! it works .")

#print("money ",j," present")
