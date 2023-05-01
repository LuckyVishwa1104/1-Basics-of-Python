#8] Bitwise Operator:- used to perform logical/boolean operation.
# given value(binary)>> binary result >> normal value.
# the value have to be input in binary.
# if the value is in integer it get
'''1. Bitwise and = "&" : it perform boolean multiplication between bit of operand
boolean and operation - (multiplication)'''
print("Bitwise and = &")
a=0b1011
b=0b1001
c=0b1111
print(a & b)
print(a&c)
print(c & a)
print(0b101 & 0b101)
print(b & 0b1000)
print(a&b&c)

'''#2. Bitwise or = "|" : it perform boolean addition between bits of operand
boolean or operation - (addition)'''
print("Bitwise or = |")
a=0b1011
b=0b1001
c=0b1110
print(a | b)
print(b|c)
print(b | 0b1010)
print(0b0011 | 0b1000)
print(a|b|c)

'''#3. Bitwise not = "~" : it perform negation of bits of operand
negation operation - opposite'''
print("Bitwise not = ~")
a=0b1011
b=0b1001
c=0b1110
d=0b101
print(~a)
print(~b)
print(~c)
print(~0b1001)
print(~(~a))

'''#4. Bitwise XOR = "^" : it perform bitwise xor operation on bits of operand
boolean X-OR operation - a`b+ab` '''
print("Bitwise XOR = ^")
a=0b1011
b=0b1001
c=0b1110
print(a^b)
print(b ^c)
print(c ^ a)
print(0b0100^0b0110)
print(a^0b1001^c)

'''5. Left shift = "<<" : it shift the bits of operand to left side and zeros to right end
shift all digit to left side'''
print("left shift operator = <<")
a=0b1011
b=0b1001
c=0b1110
print(a<<1)
print(b<<1)
print(c<<2)
print(0b101<<1)
print(0b0100^0b0110<<1)

'''#6.Right shift = ">>" : it shift the bits of operand to right side and add zeros to left end
shift all digit to right side'''
print("right shift operator = >>")
a=0b1011
b=0b1001
c=0b1110
print(a>>1)
print(b>>2)
print(~a>>1)
print(0b101>>3)