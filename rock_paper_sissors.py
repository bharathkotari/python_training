import random
import os
u=0
c=0
game=['rock','paper','sissors']
willing=True
while(willing):
	os.system("cls")
	computer=random.randint(1,3)
	print("wins\n\t user=",u,"\t computer=",c)
	user=int(input("enter your choice \n1>rock\n2>paper\n3>sissors\n"))
	if(user>3):
		print("choice should be either 1,2 or 3\n")
	else:
		print("user selected ",game[user-1],"\n")
		print("computer selected ",game[computer-1],"\n")
		if (game[user-1]==game[computer-1]):
			print(">>>>>match draw<<<<<<\n")
		elif(user-1==0 and computer-1==1)or (user-1==1 and computer-1==2)or (user-1==2 and computer-1==0):
			print(">>>>computer wins<<<<\n")
			c=c+1
		else:
			print(">>>>user wins<<<<\n")
			u=u+1
		
		i=input("\n Play again y/n ?\n")
		if(i=='n'):
			willing=False
		else:pass