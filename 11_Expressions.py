# Expressions.
'''expresson is a combination of operand and operator'''
a=3
c=7
# + = operator and a,8 = operand
b=8+a
print("Expession 8+a =",b)
print("Expression a*6 =",a*6)
print("Experssion 3*a+b =",3*a+b)
print("Expression a**3/b =",a**3//b)
print("Expression 3*a*b%4 =",3*a*b%4)
# order of execution - precedence rule.         "P-E-M-D-A-S"
''' ( )
**
+X, -X, ~
*, /, %, //
+, -
<<, >>
&, ^, |
==, !=, <, <=, >, >=
is, is not
not, and, or'''
# Types of expression.
#1. Infix expression = normal form (a+b)
print("Experssion a+b =",a+b)
print("Expression a*c+b =",a*c+b)
print("Expression a//c =",a//b)
#2. Prefix expression = +ab
print("+ab is equal to a+b")
print("*ab is equal to a*b")
#3. Postfix expression = ab+
print("ab+ is equal to a+b")
print("ab* is equal to a*b")