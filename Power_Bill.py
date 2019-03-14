print("----------------Electricity Bill---------------------")
x = int(input("what is cost of current : "))
y = int(input("Enter Number of units used : "))
z = x/y
print("Each unit is charged as : ",z)
print("-----------------------------------------------------")
meter1 = int(input("First floor number of units used  :"))
First_floor = meter1*z
print("first floor bill is  : ",First_floor)
a = int(input("Enter Number of members in First floor  :"))
c = First_floor/a
print("In First floor Each member should pay  : ",c)
print("-----------------------------------------------------")
meter2 = int(input("Second floor number of units used :"))
Second_floor = meter2*z
print("Second floor bill is : ",Second_floor)
b = int(input("Enter Number of members in Second floor :"))
d = Second_floor/b
print("In Second floor Each member should pay : ",d)
print("-----------------------------------------------------")
print("Total Bill : ",First_floor+Second_floor)
print("-------------THNAK YOU-------------------------------")
