import random
"""Class that simulates a d6"""
class Dice:
	def __init__(self, sides):
		self.sides = sides

	def roll(self, times):
		while times != 0:
			roll = random.randint(1,self.sides)
			print(f"You rolled a {roll}")
			times -=1

d6 = Dice(6)
d6.roll(5)