import random
import time

coins = 0

def displayIntro():
	print("You are in a land full of dragons. In front of you,")
	print("you see three caves. In one cave, the dragon is friendly")
	print("and will share his treasure with you. In another, the dragon")
	print("is greedy and hungry, an wil eat you on sight. In the last")
	print("one, the dragon will dismiss you. ")
	print("")

def chooseCave():
	cave = ""
	while cave != "1" and cave != "2" and cave != "3":
		print("Which cave will you go in? (1, 2, or 3)")
		cave = input()

	return cave

def checkCave(chosenCave):
	print("You approach the cave...")
	time.sleep(2)
	print("It is dark and spooky...")
	time.sleep(2)
	print("A large dragon jumps out in front of you! He opens his jaws")
	print("and...")
	print("")
	time.sleep(2)

	list_1 = [1, 2, 3] 
	friendlyCave = random.choice(list_1)
	list_1.remove(friendlyCave)
	meanCave = random.choice(list_1)

	if chosenCave == str(friendlyCave):
		print("Gives you his treasure!")
		if coins == 0:
			coins += 10
		else:
			coins += coins/2
	elif chosenCave == str(meanCave):
		print("Dismisses you!")
	else:
		print("Gobbles you down in one bite!")
		coins = 0

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print("Do you want to play again? (yes, or no)")
	playAgain = input()

