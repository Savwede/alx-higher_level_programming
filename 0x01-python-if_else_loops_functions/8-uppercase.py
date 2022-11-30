#!/usr/bin/python3
def uppercase(str):
	result = ''
	for char in str:
		if ord('a') <= ord(c) <= ord('z'):
			result += chr(ord(char) - 32)
	print("{}".format(result))
	return (result)
