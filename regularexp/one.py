import re
p=re.compile('o[a-z]*')
#print(p)
'''q=p.finditer("a12sabcab15ab",4)
for i in q:
	print(i)
q=p.findall("a125ab43abkioab")
print(q)
print(type(q))
print(p.fullmatch("dog"))
print(p.fullmatch("og51gre"))
q=p.fullmatch("cow",1,5)
print(q.group())
print(q.span())
print(q.start(),q.end())
s='<html><head><title>Tiele</title>'
print(re.match('<.*?>',s).group())
print(re.match('<.*>',s).group())

#search and replace

paymentdate="23/10/18 #Amount paid on this day"
num=re.sub('#.*$',"",paymentdate)
print("paymentdate:",num)
num=re.sub('\D',"",num)
print(num)'''
p=re.compile('\W')
print(re.match('\w.*$',"helloworld").group())