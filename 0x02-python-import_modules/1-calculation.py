#!/usr/bin/python3
if __name__ == "__main__":
	"""print sum , sub , avg and mul"""
	import calculator_1 as model

	a = 10
	b = 5

	print("{} + {} = {}".format(a , b , model.add(a , b)))
	print("{} - {} = {}".format(a, b, model.sub(a, b)))
	print("{} * {} = {}".format(a, b, model.mul(a, b)))
	print("{} / {} = {}".format(a, b, model.div(a, b)))
