#3] Assignment operators: use to assign a value to variable.

#1. assignment operator "=" : it assign value to a variable
a=66
b=7-9j
c=99.7
print('''value of a is {0}.
value of b is {1}.
value of c is {2}.'''.format(a,b,c))

#2. plus equal to operator "+=" :
# it increment the current value of variable with specified value and store that value in the variable itself
# a+=b is equal to a=a+b
a=6
b=4
a+=b
print("a+=b is equal to a=a+b")
print("a=a+b=",a)
b+=a
print(b)

#3.  minus equal to "-=" :
# it decrement the current value of variable with specified value and store that value in the variable itself
# a-=b is equal to a=a-b
a,b=2,7
a-=b
b-=a
print("a-=b is equal to a=a-b")
print("a=a-b=",a)
print(b)

#4. asterisc equal to "*="
# it multiply the current value of variable with specified value and store that value in the variable itself
# a*=b is equal to a=a*b
a,b=4,9
a*=b
print("a*=b is equal to a=a*b")
print("a=a*b=",a)
b*=a
print(b)

#5. slash equal to "/="
# it divide the current value of variable with specified value and store that value in the variable itself
# a/=b is equal to a=a/b
a,b=6,5
a/=b
b/=a
print("a/=b is equal to a=a/b")
print("a=a*b=",a)
print(b)

#6. modulus equal to "%="
# it module divide the current value of variable with specified value and store that value in the variable itself
# a%=b is equal to a=a%b
a,b=7,9
a%=b
b%=a
print("a%=b is equal to a=a%b")
print("a=a%b=",a)
print(b)

#7. double asterisc equal to "**="
# it power multiply the current value of variable with specified value and store that value in the variable itself
# a**=b is equal to a=a**b
a,b=5,2
a**=b
b**=a
print("a**=b is equal to a=a**b")
print("a=a**b=",a)
print(b)

#8.duoble slash(floor division) equal to "//="
# a//=b is equal to a=a//b
a,b=9,5
a//=b
b//=a
print("a//=b is equal to a=a//b")
print("a=a//b=",a)
print(b)