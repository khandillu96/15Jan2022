#display user enter name follwed by good afternoon using input() function
name=input("enter name: ")
print("good afternoon :",name)
print(" ")



#fill a letter templte given below with name and date
#1) 1st way
name=input("Enter name\n")
date=input("Enter date\n")
print("dear ",name," your are selected on ",date)
print("\n\n")


#2) 2nd way
letter='''dear name
greeting from dilshad house,i am happy to tell you about 
your selection ,your are selected!
have a great day
thank regard 
dilsahd
date'''
namee=input("Enter name: ")
datee=input("Enter date: ")
letter=letter.replace("name",namee)
letter=letter.replace("date",datee)
print(letter)





#write a program to detect double space
str="this is string with  space"
dblsp=str.find("  ")
print(dblsp)



#write a program replace double sapce with single space
str1="this is string  space"
str1=str1.replace("  "," ")
print(str1) 


#write a program to formate the following letter using excape sequence character
letters="Dear harry,This python course is nice. thanks!"
letescape="Dear harry,\n\t This python course is nice.\nthanks!"
print(letescape)