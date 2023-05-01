#2] Comparision operator: they are used to compare the operands

#1 equal to '==' : it return true value when operands are true else faLse
e=7
f=7
c=bool(e==f)
print(c)
a=5
b=5
if a==b:
	print(a,"is equal to",b)
print("input two equal no.")

#2. not equal to '!=' : it return true value when operands are not equal else return falsee value
e=7
f=9
g=e!=f
print(g)
a=7
b=4
if a!=b:
	print(a,"not equal to",b)
print("enter two not equal no.")

#3. grater than '>' : it return true value when left operand is greater than right operand
e=7
f=5
print(e>f)
a=8
b=6
if a>b:
	print(a,"is greater than",b)
print("enter two no.")

#4. greater than or equal to '>=' : it return true value when left operand is greater than or equal to right operand
e=8
f=8
print(e>=f)
a=9
b=9
if a>=b:
	print(a,"is greater than or equal to",b)
print("enter two no. ")

#5. less than '<' : it return true value when left operand is less than right operand
e=8
f=9
print(e<f)
a=7
b=8
if a<b:
	print(a,"is less than",b)
print("enter two no. ")

#6. less than or equal to '<=' : it return true value when left operand is less than or equal to right operand.
e=6
f=8
print(e<=f)
a=7
b=9
if a<=b:
	print(a,"is less than or equal to",b)
print("enter two no.")