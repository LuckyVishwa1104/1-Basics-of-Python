# Membership Operators.
# used to check whether the value is present or not present in sequence.
#1. "in" operator.
list=["a","e","i","o","u"]
print("a" in list)
print("e" in list)
print("o" in list)
print("b" in list)
x="u" in list
print(x and False)
print("c" in list)
#2. "not in" operator
tuple=(2,4,6,8,10)
print(1 not in tuple)
print(3 not in tuple)
print(8 not in tuple)
y=10 not in tuple
print(y or True)
print("h" not in tuple)
print()
# string
s="Lucky"
print("L" in s)
print("l" not in s)
print("Luc" in s)
n=56,56,67
print(56 in n)
dic={1:"a",2:"b",3:"c"}
print(3 in dic)

print()
# combined form
print(("a" in list)and(9 not in tuple))
print(("x" not in list)or(7 in tuple))
print(("b" in list)and(5 not in tuple)or(not("u" in list)))