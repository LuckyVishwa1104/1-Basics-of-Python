#6] Data-types :- types of data stored in variable
# type( ) function is used to identify the data-type.

# Numeric datatype :- holds numeric values.
num1=68
num2=778.99
num3=89+99j
print(num1,num2,num3)

#1. Integer data-type - combination 0 to 9,binary, octal, hexadecimal
num1=7
print(num1,"=",type(num1))
num2=1101
print(num2)
n3=0b1011  # binary = "0b_"
print(type(n3))
n4=0o367   # octal = "0o_"
print(type(n4))
n5=0x4A6D0  # hexadecimal = "0x_"
print(type(n5))

#2. float data-type - combination of 0 to 9 always includes decimal point
num3=13.99
print(num3,"=",type(num3))
n6=-8.960
print(type(n6))

#3. Complex data-type - (real+imaginary) it is a combination of real part and imginary part, imaginary part is always associated with 'j'
num4=77+9j
print(num4,"=",type(num4))
n7=-88-7j
print(type(n7))

#4. String data-type - collection of alphabate, numbers, characters. Always enclosed within double or single quotes.
str1="Hello"
str2="99.99"
str3="#$@"
print(str1,"=",type(str1))
print(str2)
print(str3)
# operations on string
#a. '+'-concatenation= joining strings
print(str1+str2)
print(str1+str2+str3)
#b. '*'- repitition of string
print(str1*3)
print((str1+str3)*2)

#5. Boolean data-type: - 0 and 'FALSE' are false and rest of everything is true .
a=True
b=False
c=bool(57)
print(a,"=",type(a))
print(b,"=",type(b))
print(c,"=",type(c))

#None data-type: - used to define null variable
name=None
print(name,"=",type(name))
lst=[None,None]
print(lst,"=",type(lst))

#6. List data-type: list=[val1,val2,val3,...,valn]
# it is a collection of similar or different types of values and enclosed within square brackets
list_1=["a","e","i","o","u","j"]
print(list_1,"=",type(list_1))
list_2=["Hello","@","lucky",4805,99+88j,89.9]
print(list_2,"=",type(list_2))
a=[1,2,3,4,5,6,7,8]
b=["a","b","c","d","e"]
# accesing random values of list
print(a[2],b[-2],a[4])

#7. Tuple data-type: tuple=(v1,v2,v3,...,vN)
# it is a collection of similar or different types of data, but it is immutable and enclosed within circle brsckets.
tuple1=("apple","mango","guava")
print(tuple1,"=",type(tuple1))
# accessing random values of tuple
tuple2=(11,22,33,44,55)
print(tuple2[2],tuple1[1],tuple2[4])

#8. Dictionary data-type: dict={key:value}
# it is collections of values in key-value form and enclosed within curly brackets
dict_1={1:"one",2:"two",3:"three"}
print(dict_1,"=",type(dict_1))
dict_1={"apple":120,"mango":105,"banana":45}
# accessing keys and values of dictionary separately.
print(dict_1.keys())
print(dict_1.values())

#9. Set data-type: set={val1,val2,....,valn}
# it is collection of values but not in order
set1={"@","#",45,78.9,"hello","phines"}
print(set,"=",type(set))
set2={1,2,2,2,"dg",bool(67),8-7j}
print(set2)

print()
# Data-type conversion.
print("Data-type conversion.")
#1. int - float, string, bool, bin, hex, oct.
print("int - float, string, bool, bin, hex, oct.")
a=56.86
print(int(a))
a="78"
print(int(a))
a=True
print(int(a))
# Binary number are input by taking "0b" at starting followed by no. in 1 and 0.
b=0b1000
print(int(b))
# Octal no. = "0o" followed by 0 to 7
o=0o473
print(int(o))
#hexadecimal no.= "0x"-( 0 to 9 and A to F)
h=0x7896A
print(int(h))
boolian=True
print(int(boolian))
#2. float - int, string, bool, bin, oct, hex
print("float - int, string, bool, bin, oct, hex")
a=-45
print(float(a))
a="55"
print(float(a))
a=False
print(float(a))
print(float(b))
print(float(o))
print(float(h))

#3. complex - int, float, string, bool, bin, oct,hex.
print("complex - int, float, string, bool, bin, oct,hex.")
a=-82
print(complex(a))
c=67.78
print(complex(c))
print(complex(boolian))
print(complex(b))
print(complex(o))
print(complex(h))

#4. string - int, float, complex, bool, bin, oct,hex, list, tuple, dict, set
print("4. string - int, float, complex, bool, bin, oct,hex, list, tuple, dict, set")
print(str(c))
print(str(a))
d=7+8j
print(str(d))
a=True
print(str(a))
print(str(b))
print(str(h))
print(str(o))

#5. boolian - only 0 is false and all other datatype are true for bool.
print("all dat-type can be converted into boolian tupe")
print(bool(a))
a=1
print(bool(a))
# 0,False=false and rest of everything is true 
a=66-7j
print(bool(a))
a="ty"
print(bool(a))
print(bool(list_1))
print(bool(tuple1))
print(bool(dict_1))
print(bool(o))

#6. list - string,tuple,dict,set.
print("list - string,tuple,dict,set.")
a="lucky"
print(list(a))
print(list(tuple1))
print(list(dict_1))
d={1:2,3:4,5:6}
print(list(d))
print(list(set1))

#7. tuple - string,list,dict,set.
print("tuple - string,list,dict,set.")
print(tuple(a))
print(tuple(list_1))
print(tuple(dict_1))
print(tuple(set1))

#8. dict - no data type can be converted into dictionary.
print(dict(dict_1))

#9. set- string,list, tuple, dict.
print("set- string, list, tuple, dict.")
a="lucky"
print(set(a))
print(set(list_1))
print(set(tuple1))
print(set(dict_1))

#1.1 bin - int, oct, hex, bool
print("bin - int, oct, hex, bool")
a=8
print(bin(a))
print(oct(a))
print(hex(a))
#1.2 oct - int, bin, hex, bool
print("oct - int ,bin, hex, bool")
a=True
print(bin(a))
print(oct(a))
print(hex(a))
#1.3 hex - int, oct, hex, bool
print("hex - int, oct, hex, bool")
a=0b1001
print(oct(a))
print(hex(a))
b=0o657
print(bin(b))
print(hex(b))
c=0x579A
print(bin(c))
print(oct(c))
