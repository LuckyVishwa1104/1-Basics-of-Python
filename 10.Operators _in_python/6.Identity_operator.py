# Identity Operator :- used to check whether operands has same memory location.
#1. "is" operator.
a="wonderful"
b=99.96
c=b
d="wonderful"
color=["red","blue","green"]
color1=["red","blue","green"]
print(a is d)
print(b is c)
print(color is color1)
print(d is b)
print(d is d)
print()
#2. "is not" operator
p=56
q="happy"
r=c
s="Happy"
print(q is not s)
print(p is not r)
print(r is not b)
print(r is not r)
print(c is not b)
