#!/usr/bin/python3
import sys
i = len(sys.argv) - 1

print("{} arguments".format(i + 1))


if i >= 1:

	i = 0

	for arg in sys.argv:
		i += 1
		print("{}: {}".format(i, arg))
