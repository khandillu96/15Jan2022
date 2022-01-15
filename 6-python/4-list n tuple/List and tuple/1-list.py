#creating list with item useing[]
a=[1,2,3,53,4]
print(a)
print(a[0])     #pritn(variablename[indexno])

a[4]=332        #updated with index no
print(a[4])
print(" ")


#we can creat list with item of diffrent data-type
b=[12,"13ee14","dilshad","khan"]
print(b)
print(b[1])

b[2]="dilshad ahmed"
print(b[2])
print(" ")


#slicing of list
friends=["noor","saif","zeshan","nisha",13]
print(friends[1:4])           #will print 1,2,3 not 4 index
print(friends[0:4:2])
print(" ")


##list method
li=[3,1,4,322,64,223]
li.sort()     #not use like ==>li=li.sort()
print(li)

li.reverse()
print(li)

li.pop()
print(li)      #remove item at end of the list

li.append(23)  #adds item at end of the list
print(li)


li.insert(0,555)    #insert 555 at index no 2
print(li)


li.remove(555)     #remove 555 from the list
print(li)

#list has many method we can search on google
# https://docs.python.org/3/tutorial/datastructures.html


