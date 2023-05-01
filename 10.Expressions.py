#10] Expressions - expresson is a combination of operand and operator
'''operand - these are the values on which operation is being  performed
operator -these are the functions which performs operation'''
a=3
c=7
# + = operator and a,8 = operand
b=8+a
print("Expession 8+a =",b)
print("Expression a*6 =",a*6)
print("Experssion 3*a+b =",3*a+b)
print("Expression a**3/b =",a**3//b)
print("Expression 3*a*b%4 =",3*a*b%4)

# order of execution - order of execution of expression followes precedence rule.
# "P-E-M-D-A-S" - parenthesis, exponwtial, multiplication, divivsion, addition, subraction. inthis order only the expression is evaluated.
# following shows the order in which expression is evaluated
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