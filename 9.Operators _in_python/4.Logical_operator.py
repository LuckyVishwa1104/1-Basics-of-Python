#4] Logical Operators :
'''1. logical and - only T and T is True rest of is False
T and T=T '''
a=True
b=False
print(a and a)
print(a and b)
print(b and b)

''' 2. logical or -only F or  F is False rest of is True
F or F=F '''
print(a or a)
print(b or b)
print(a or b)

''' 3. logical not - it return the negation of passed value
~T=F and ~F=T '''
print(not a)
print(not b)
print(not(a and b))

# combined logical operation
# the precedence order is- not>and>or
''' the value "0" is always "False"
and rest of every thing is "True" '''
c=0
d="hii"
print(c and d)
print(c or d)
print(not c,not d)
print(a and (b or a ))
print(not(a or b and c))
print((a or b)and(b or a))
print(not a and b or a)
print(a or b and d or not b)

