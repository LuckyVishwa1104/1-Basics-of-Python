# Set = {val_1,val_2,val_3, - - -,val_n}
# value can not be repeated in set
''' Set = variable(A to Z,a to z, _ ,0 to 9)
   value = variable, input, expression,
            all data-type( except List, Set, dict) 
 '''
# Examples.
set_1={"a","e","i","o","u"}
print(set_1)
set_2={"a","e","i","o","a","e","u","i"}
print(set_2)
set_3={1,2,3,4,5,6,1,2,3,7,8}
print(set_3)
set_4={"$","&","#","@","¥","$","@"}
print(set_4)
# Example 1.
set_a={33,4.6,5-7j,0b101,0o347,0x2A5F}
print(set_a)
# Example 2.
set_b={"string",'&$@',True,bool(0)}
print(set_b)
# Example 3.
set_c={45,5.89,(4,"sad",(45,55)),78+8j,0b10111}
print(set_c)