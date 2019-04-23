file = str(input('enter file name'))
print('File name is'+ file)
file = open("C:\pyth\myfile.txt")
file.read()
try:
	file = open("C:\pyth\myfile.txt")
except IOError:
	file = str(input("enter file name agine ? "))
finally:
	print('done')