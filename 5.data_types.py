#5] Data-types :- types of data stored in variable
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
# binary = "0b_" : binary numbers are initiated with usong 0b at the begining followed sequence of number 1 and 0
n3=0b1011  
print(type(n3))
# octal = "0o_" : octal nuber are initiated by using 0o at the begining followed by 0 to 7
n4=0o367   
print(type(n4))
# hexadecimal = "0x_" : hexaaldecimal number are inititated by usong 0x at the begining 0 to 9 and A to F
n5=0x4A6D0  
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
# there are two type of string-
#a. singleline string - written in single line, it is initiated by single or double quotes 
str4,str5='hello you',"politician are in the race o gaining power"
print(str4)
print(str5)
#b. multiline string - written in multiple lines, it is initiated with triple single or double quote
str6='''hello 
hope you are doing well'''
str7="""hello you 
hope you are doing well"""
# operations on string
#a. '+'-concatenation= joining strings
print(str1+str2)
print(str1+str2+str3)
#b. '*'- repitition of string
print(str1*3)
print((str1+str3)*2)

#5. Boolean data-type: - 0 and 'FALSE' are false and rest of everything is true i.e. everything (int, string, collection, etc are considered as true).
a=True
b=False
c=bool(57)
d='hello'
e=bool([2,4,6,8])
print(a,"=",type(a))
print(b,"=",type(b))
print(c)
print(bool(d))
print(d)

#None data-type: - used to define null variable, it is having empty value
name=None
print(name,"=",type(name))
lst=[None,None]
print(lst)

#6. List data-type: list=[val1,val2,val3,...,valn]
# it is a collection of similar or different types of values and enclosed within square brackets
list_1=["a","e","i","o","u","j"]
print(list_1,"=",type(list_1))
list_2=["Hello","@","lucky",4805,99+88j,89.9]
print(list_2)
a=[1,2,3,4,5,6,7,8]
b=["a","b","c","d","e"]
# accesing random values of list
print(a[2],b[-2],a[4])

#7. Tuple data-type: tuple=(v1,v2,v3,...,vN)
# it is a collection of similar or different types of data, but it is immutable and enclosed within circle brsckets.
tuple1=("apple","mango","guava")
print(tuple1,"=",type(tuple1))
tuple3=(12,23,34,45,56)
print(tuple3)
# accessing random values of tuple
tuple2=(11,22,33,44,55)
print(tuple2[2],tuple1[1],tuple2[4])

#8. Dictionary data-type: dict={key:value}
# it is collections of values in key-value form and enclosed within curly brackets
dict_1={1:"one",2:"two",3:"three"}
print(dict_1,"=",type(dict_1))
dict3={1:1,2:4,3:9,4:16,5:25}
print(dict3)
dict_1={"apple":120,"mango":105,"banana":45}
# accessing keys and values of dictionary separately.
print(dict_1.keys())
print(dict_1.values())

#9. Set data-type: set={val1,val2,....,valn}
# it is collection of values but not in order
set1={"@","#",45,78.9,"hello","phines"}
print(set,"=",type(set))
set3={1,2,3,4,5}
print(set3)
set2={1,2,2,2,"dg",bool(67),8-7j}
# values at respective index are going to change at every run as set is unordered.
print(set2[1],set[3])

print()
# Data-type conversion.
print("Data-type conversion.")
#1. float, string, bool, bin, hex, oct - all these data-types can be converted into integer.
print("int <-- float, string, bool, bin, hex, oct.")
a=56.86
print(int(a))
a="78"
print(int(a))
boolian=True
print(int(boolian))
# Binary number are input by taking "0b" at starting followed by no. in 1 and 0.
b=0b1000
print(int(b))
# Octal no. = "0o" followed by 0 to 7
o=0o473
print(int(o))
#hexadecimal no.= "0x"-( 0 to 9 and A to F)
h=0x7896A
print(int(h))

#2. int, string, bool, bin, oct, hex - all these data-types can be converted into float
print("float <-- int, string, bool, bin, oct, hex")
a=-45
print(float(a))
a="55"
print(float(a))
a=False
print(float(a))
print(float(b))
print(float(o))
print(float(h))

#3. int, float, string, bool, bin, oct, hex - all these data-types can be converted to complex 
print("complex <-- int, float, string, bool, bin, oct,hex.")
a=-82
print(complex(a))
c=67.78
print(complex(c))
print(complex(boolian))
print(complex(b))
print(complex(o))
print(complex(h))

#4. int, float, complex, bool, bin, oct,hex - all these data-types can be converted to string
print("string <-- int, float, complex, bool, bin, oct,hex, list, tuple, dict, set")
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
print("all dat-type can be converted into boolian type")
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

#6. string,tuple,dict,set - all these data-type can be converted to list type
print("list <-- string,tuple,dict,set.")
a="lucky"
print(list(a))
print(list(tuple1))
print(list(dict_1))
d={1:2,3:4,5:6}
print(list(d))
print(list(set1))

#7.string,list,dict,set : all these data-types can be converted to tuple
print("tuple <-- string,list,dict,set.")
print(tuple(a))
print(tuple(list_1))
print(tuple(dict_1))
print(tuple(set1))

#8. dict - no data type can be converted into dictionary.
print(dict(dict_1))

#9. string,list, tuple, dict - all these data-tyoe can be converted to set type
print("set <-- string, list, tuple, dict.")
a="lucky"
print(set(a))
print(set(list_1))
print(set(tuple1))
print(set(dict_1))
