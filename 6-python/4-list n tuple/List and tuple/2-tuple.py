#creating tuple with item using()
t=(1,3,23,55)
print(t)
print(t[2])

# t[3]=22           #will not update this is main diff btw list n tuple
# print(t[3])       #throw an error
print(" ")


t1=()    #empty tuple
t1=(1)   #wrong way to declear tuple with single item/element
t1=(1,)  #tuple with single element/item
print(t1)
print(" ")


##tuple method
t=(1,3,2,22,1,33,1)
'''t.count(1)
print(t)''' #==> thows error 

print(t.count(1))      # will return number of time 1 occurs in t
print(t.index(3))      # will return the index of list occureance of 3 in t
