
single="dilshad's"
double="ahmed's"
triple='''khan
from kurla
'''
print(single,double,triple)




#string method
#string slicing:
str="india is a beutiful country "
mum="city of india"
print(str + mum)   #concat
print(str[-5])     #index no print (-ve will accept)
print(str[2:5])    #slice (strt 2index to 5 index(-ve will accept))
print(str[0:6:2])  #slice with skip [str:end:skipstep(like 2)](- will acpt)
print(" ")




#string function
story="once upon a TIME there WAS a programer who name is  dilshad "
print(len(story))           #length
print(story.upper())        #upper
print(story.lower())        #lower
print(story.capitalize())   #capitalize (1st latter CAPS)
print(story.count("a"))     #cout (will count Cheractor like a,b,c)
print(story.startswith("ownce"))
print(story.endswith("dilshad"))
print(story.find("dilshad"))  #will give index no


print(story.replace("dilshad","afsha"))  #replace
print(story[::-1])                        #reverse
print(story*2)                            #repeate


# import string_utils
# print string_utils.shuffle("random_string")

