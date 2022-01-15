'''comparision operator
==	:Is equal to 
===	:equal value and  equal data type => not use in python 
!=	:Not equal to	 
!==	:not equal value or not equal type
>	:Greater than 
>=	:Greater than or equal to	 
<	:Less than   
<=  :less than or equal to   '''

a=5
b=10

print(a==b)
print(a!=b)

print(a>b)
print(a>=b)

print(a<b)
print(a<=b)








'''logical operator
&& : AND -- both condition true out of 2conditon  will print true.
|| : OR  -- any one condition true out of 2conditon will print true.
!  : NOT -- if one condition true out of 1conditon will print faule. '''

print("logical operators")
x=12
y=13
z=14

print("and--- ",(x==12) and (y==13))
print("or--- ",(x<=y) or (y==z))
print("not--- ",not(z>y))


