# Numeric literal - it contains numeric value only.
# 1. Integer Numeric literal : +/- combination of 0 to 9
# it includes integers, binary, octal, hexadecimal numbers.
print("1. Integer Numeric literal.")
int_1=1002
int_2=-234
int_3=8801
int_4=0
print("{0}, {1}, {2}, {3} are the Integer numeric literals.".format(int_1,int_2,int_3,int_4))
#1.1 binary numeric literal : "0b"
# 1 and 0 
b1=0b1010
b2=0b1101
print("{0}, {1} are binary numeric literal".format(b1,b2))
#1.2 octal numeric literal : "0o"
# 0 to 7
o1=0o123
o2=0o76
print("{0}, {1} are Octal numeric literal".format(o1,o2))
#1.3 hexadecimal numeric literal : "0x"
# 0 to 9 and A to F
h1=0x12A6
h2=0x67AF5
print("{0}, {1} are hexadecimal numeric literal".format(h1,h2))
print()
# 2. Float Numeric literal : +/- combination of 0 to 9 always with decimal point
print("2. Float Numeric literal")
flt_1=0.0
flt_2=-483.8
flt_3=3.14
flt_4=.98
flt5=89.
print("{0}, {1}, {2}, {3}, {4} are Float numeric literal.".format(flt_1,flt_2,flt_3,flt_4,flt5))
print()
# 3. Complex Numeric literal : 'real + imaginary'
# real = integer, float, bin, oct, hex,                              complex, bool, variable, input,                        expresion
# imaginary = represented by ' j ' - int, float
print("3. Complex Numeric literal")
cmx_1=10+4j
cmx_2=-3-8.8j
cmx_3=4.5-78.7j
print("{0}, {1}, {2} are Complex numeric literal.".format(cmx_1,cmx_2,cmx_3))
