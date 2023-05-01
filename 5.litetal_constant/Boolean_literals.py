# Boolean literals - True , 1 , False , 0.
''' only 0 , False are false
  True = variables, input, output, expression,               all data-types'''
# demonstration of Boolean Literal.
a=(1==True)
b=(1==False)
print("a: ",a)
print("b:",b)
# Example-1.
x=True
y=0
# True and False = False.
z=bool(x and y)
print(z)

#Example-2.
x=False
y=1
z=bool(x or y)
print(z)

#Example-3.
x=bool(True or False)
print(x)

#Example-4.
a=bool(1 and 1)
print(a)

#Example-5.
a=((1 and 1)or(0 and 0))
print(a)