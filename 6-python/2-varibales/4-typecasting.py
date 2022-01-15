'''type casting(change data type)
covert string to int, example-- given below


str(31) => "31" (integer to string  conversion)
int("32")=> 32  (string  to integer conversion)
float(32)=> 32.1(integer to float   conversion)
'''



a="123"
a=int(a) #imp
print("integer ",a+1)
print(type(a))
print(" ")

b=31
b=str(b)
print("string ",b)
print(type(b))
print(" ")


c=32
c=float(c)
print("float ",c)
print(type(c))
print(" ")



'''Q- input() function
ans - input function allow the user to take input 
from the kewborad as a string'''
inp=input("enter your name: ")  #-->data type is string 
print(inp)
print(type(inp))