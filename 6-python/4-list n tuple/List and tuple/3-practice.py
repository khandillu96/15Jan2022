#Write a program to store seven fruits in a list entered by the user
fr1=input("enter fruits 1  name: ")
fr2=input("enter fruits 2  name: ")
fr3=input("enter fruits 3  name: ")
fr4=input("enter fruits 4  name: ")
fr5=input("enter fruits 5  name: ")
fr6=input("enter fruits 6  name: ")
fr7=input("enter fruits 7  name: ")
fruits=[fr1,fr2,fr3,fr4,fr5,fr6,fr7]
print(fruits)
print(" ")


#Write a program to accept the marks of 6 students and display them in a sorted manner.
m1=int(input("enter mark 1: "))
m2=int(input("enter mark 2: "))
m3=int(input("enter mark 3: "))
m4=int(input("enter mark 4: "))
m5=int(input("enter mark 5: "))
m6=int(input("enter mark 6: "))
marks=[m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)
print(" ")

# #Check that a tuple cannot be changed in Python.
# t=(1,34,34,43)
# t[1]=22
# print(t)


#Write a program to sum a list with 4 numbers.
t=[22,43,43,54]
print(t[0]+t[1]+t[2]+t[3])
print(sum(t))
print(' ')


#Write a program to count the number of zeros in the following tuple:
t=(0,5,0,3,0,33)
print(t.count(0))