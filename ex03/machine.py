#!/usr/bin/env python3
from beverages import *
from random import random


class CoffeeMachine:
	__drinks_before_break: int = 10

	class EmptyCap(HotBeverage):
		name = 'empty cup'
		price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__('This Coffee machine has to be repaired')

	def repair(self):
		self.__drinks_before_break = 10

	def serve(self, DrinkClass):
		if self.__drinks_before_break > 0:
			self.__drinks_before_break -= 1
			if random() >= 0.3:
				return DrinkClass()
			else:
				return self.EmptyCap()
		else:
			self.__drinks_before_break = 0
			raise self.BrokenMachineException


def main():
	coffee_machine = CoffeeMachine()
	for i in range(3):
		try:
			print(coffee_machine.serve(Tea),
			      coffee_machine.serve(Coffee),
			      coffee_machine.serve(Chocolate),
			      coffee_machine.serve(Cappuccino),
			      coffee_machine.serve(HotBeverage), sep='\n')
		except:
			coffee_machine.repair()

	for i in range(3):
		try:
			print(coffee_machine.serve(Tea),
			      coffee_machine.serve(Coffee),
			      coffee_machine.serve(Chocolate),
			      coffee_machine.serve(Cappuccino),
			      coffee_machine.serve(HotBeverage), sep='\n')
		except:
			coffee_machine.repair()

if __name__ == '__main__':
	main()
