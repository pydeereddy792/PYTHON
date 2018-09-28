#write a program to design the snake and lader game
count=0
import random
while (count<=100):
	n=input("enter r to roll the dice")
	if(n=='r'):
		a=random.randint(1,6)
	count=count + a
	print("my position",count)
	print("the r value",a)

	if(count==11):
		count=2
		print("sorry the snake bites you")
	elif(count==8):
		count=37
		print("congrats u have climbed the ladder")
	elif(count==13):
		count=34
		print("congrats u have climbed the ladder")
	elif(count==25):
		count=4
		print("sorry the snake bites you")
	elif(count==38):
		count=9
		print("sorry the snake bites you")
	elif(count==40):
		count=68
		print("congrats u have climbed the ladder")
	elif(count==52):
		count=81
		print("congrats u have climbed the ladder")
	elif(count==65):
		count=46
		print("sorry the snake bites you")
	elif(count==76):
		count=97
		print("congrats u have climbed the ladder")
	elif(count==89):
		count=70
		print("sorry the snake bites you")
	elif(count==93):
		count=64
		print("sorry the snake bites you")
	elif(count==100):
		print("congo u won the game")
	elif(count>100):
		count=100
		print("congo u won the game")

