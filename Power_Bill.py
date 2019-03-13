x = int(input("what is cost of current : "))
y = int(input("Enter Number of units used : "))
z = x/y
print("Each unit is charged as : ",z)
meter1 = int(input("First floor number of units used  :"))
meter2 = int(input("Second floor number of units used :"))
First_floor = meter1*z
Second_floor = meter2*z
print("first floor bill is  : ",First_floor)
print("Second floor bill is : ",Second_floor)
print("Total Bill : ",First_floor+Second_floor)
a = int(input("Enter Numbr of members in First floor  :"))
b = int(input("Enter Numbr of members in Second floor :"))
c = First_floor/a
d = Second_floor/b
print("In First floor Each member should pay  : ",c)
print("In Second floor Each member should pay : ",d)
