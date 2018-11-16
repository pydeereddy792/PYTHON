# write a program to genarate the game rock ,paper,siscor
import random
d={1:'r',2:'p',3:'s'}

c=d[random.randint(1,3)]
p=input("enter'r','p','s'")
print("computer",c)
if(c==p):
	print("tie")
if((c=='r'and p=='s') or(c=='p'and p=='r') or(c=='s'and p=='p')):
	print("c won the game")
else:
	print("p lost the game")