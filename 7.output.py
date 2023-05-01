#8]. print() function - used to display the output on console (output window).
''' Syntax:
	   print(parameters) '''
# parameter - all data-type, variables, experssion, input.
# parameters are separeted by commas.
# Examples
print(8,3.14,7-5j)
print(0b101,0o25,0x2AD)
print("string",False,bool(78))
print(["ghe","gen",],(3,6.7,89),{2:4,3:9,4:16},{7,8,9})

a,b,c=2,6,4
# expression get evaluated in print function
print(a,b,c,a*b,c-5,a*5+b)
print(input("entet first elem: "),input("enter second elem: "),input("enter third elem: "))

# multiplication of two numbers by using print functions.
# input the first number
print("Enter first no. : ")
a=int(input())
# input second number
print("Enter second no. : ")
b=int(input())
c=a*b
# display the result
print("Required product is ")
print(a,"x",b,"=",c)

# .format() - format is used to display the parameters according to index
'''Syntax:
	print(- - {index1} , {index2}.format(val1,val2))'''
# example for demonstration of format
print("{0} is elder than {1} !".format("sam","adam")) # sam is assigned to 0 index and adam is assigned to 2 inedx
print("{0} × {1} = {2}".format(2,2,4) )
a,b,c,d,e=int(input("a=")),int(input("b=")),int(input("c=")),int(input("d=")),int(input("e="))
f=a+b+c+d+e
print("sum of {0}+{1}+{2}+{3}+{4} is {5}".format(a,b,c,d,e,f))
