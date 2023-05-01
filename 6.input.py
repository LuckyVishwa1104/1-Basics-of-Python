#7]. Input - input() function is used to input the data from keyboard or to take input from the users

# everything taken from input function is in the form of "string data-type"

''' Syntax:
	input( [prompt ] ) = value
	prompt - usually a string which indicate the type of data to input, but it can be any data-type
	value - only string , but using data type conversion it can be converted to any data type'''

#1. program to demonstrate input function
a=input("Entet your name : ")
print("Hello",a,"How ar you !!")  

#2. example 2
a=input("Enter data: ")
b=input("Enter data: ")
c=a+b
print(c)

#3. addition by using input function.
print("Addition of two numbers ")
''' Enter first no.
   Enter second no.'''
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
# store the result in c.
c=a+b
print('''Addition of two numbers is:
''',c)

#4. program to recover your login id and passward.
print("Username and password ")
user_name=input("Enter User name : ")
passw=input("Enter Passward : ")
print('''Your login details are;
username={0}
passward={1}
Loged in Successfully'''.format(user_name,passw))

#5. program to find simple interest using input function
print("Simple interest : ")
# enter principal amount.
PA=int(input("Enter Principle Amount : "))
# enter time period.
T=int(input("Enter Time Period : "))
# enter rate of interest
R=float(input("Rate of Interest : "))
'''calculate simple interest
and print the result as interest.'''
interest=(PA*T*R)/100
print("Simple Interest is",interest)

