# Assignments on variables expressions and statements

# 1.Take the input from the user for (Total number of people, Number of seats for bus. Based on two inputs, decide how many number of buses required.
# Input(“Enter no. of people”)
# Input(“Enter no. of seats in the bus”)

Solution:
try:
  people = int(input("Please Enter no. of people:: "))
  bus_capacity = int(input("Please enter no. of seats a bus can occupy:: "))
  buses_needed = people/bus_capacity
  if(people%bus_capacity)==0:
    print("no. of buses needed to fill the people",int(buses_needed))
  else:
    print("no. of buses needed to fill the people",int(buses_needed)+1)
except( ValueError ):
  print ("It has to be a number")


# 2.Take temperature from the user and convert Fahrenheit -> Celsius

try:
  fahrenheit =int(input("Please Enter temperature in Fahrenheit:: "))
  fahrenheit= float(fahrenheit)
#convert fahrenheit to celsius
  celsius = (fahrenheit - 32)*5/9
  print ("Celsius:", celsius)
except( ValueError ):
  print ("It has to be an integer")


# 3.Take temperature from the user and convert Fahrenheit → Celcious.

try:
  celsius =int(input("Please Enter teperature in Celsius :: "))
  celsius= float(celsius)
#convert celsius to fahrenheit
  fahrenheit =( (celsius*9/5)+ 32)
  print ("fahrenheit:", fahrenheit)
except( ValueError ):
  print ("It has to be an integer")

# 4.	take four number from the user, perform below operations
# •	(a+b)**2, (c+d)**3
# •	Variance
# •	standard deviation
# •	Regression
# 	y=mx+b
#     All a,b,c,d are consider as (x1,x2,x3,x4)
# •	m=1.23
#     b=0.045
#     find out y
#     y=m*(x1+x2+x3+x4)+b
#  Find the average of four numbers
# Find the sum of four numbers
import statistics
import math
choices = input("Please enter four input and seperate with space:: ")
# calculating expression result
a,b,c,d = (choices.split(" "))
var = int(a),int(b),int(c),int(d)
lst = list(var)
result1 = (int(a) + int(b))**2
result2 = (int(c) + int(d))**3
print("(a+b)**2 and (c+d)**3 = ", result1,result2)
# caluculating variance and deviation
print("Variance :", statistics.variance(lst))
print("Deviation ",(math.sqrt(statistics.variance(lst))))
#calculating Sum and average
average = 0
sum = 0
for n in lst:
  sum = sum + n
average = sum / len(lst)
print("Sum of a,b,c,d is:", sum)
print("Average of a,b,c,d is: ",average)

m,x=1.23,0.045
y=m*(int(a) + int(b) + int(c) + int(d))+x
print("Regression Value: ",y)


# 5.Take the distance in km, calculate that in cm, meters, in milli meters, cents, feets

try:
  km = float(input("Please enter distance in kelometer:: "))

  # kilo meter to meter, meter = km/1000 
  meter = km*1000
  print("%s km to meter is: %s " %(km,meter))
  
  # kilo meter to centimeter, km*100000 cm 
  cm = km*100000
  print("%s km to centimeter is: %s" %(km,cm) )

  # kilo meter to milli meter, k/0.0000010000
  mm = km*1000000
  print("%s km to millimeter is: %s " %(km,mm))

  # kilo meter to feets, 1 km = 3,280.839895 ft
  ft = km* 3280.839895
  print("%s km to feet is: %s " %(km,ft))

except(ValueError):
  print("Has to be a number")


# 6. Take the size of your hard disk in GB, calculate that in MB, KB, TB, PB


try:
  GB = int(input("Please enter the size of your harddisk in GB:: "))

  # GB to MB, 1GB = 1000 MB
  MB = GB * 1000
  print("%s GB to MB is: %s " %(GB,MB))

  # GB to KB, 1GB = 1000000 KB
  KB = GB*1000000
  print("%s GB to KB is: %s " %(GB,KB))

  # GB to TB, 1GB =  0.001 TB
  TB = GB/1000
  print("%s GB to TB is: %s " %(GB,TB))
  
  # GB to PB, 1GB =  0.000001 PB
  PB = GB/ 1000000
  print("%s GB to PB is: %s " %(GB,PB))
 
except(ValueError):
  print("Must be an integer")


# 7.  Take name, age, height from the user and print like below
# The details of the person: Name:name of the person, Age:age of the person, Height:height of the person
# Note: make sure that no space between: and a value and should be space after “COMA”
def name():
  while True:
    n=input("Please enter the name:").lower()
    if not n.isalpha():
      print ("Invalid! name")
    else:
      print("Name:",n)
      print("Name:{}".format(n))
      print("Name:" + str(n))
      break
def age():
    while True:
      a=input("Please Enter the age:")
      if not a.isdigit():
        print ("Invalid! age")
      else:
        print("Age:{}".format(a))
        break


def height():
    while True:
      h=input("Please Enter the height:")
      if not h.isdigit():
        print ("Invalid! height")
      else:
        print("Age:{}".format(h))
        break

# map the inputs to the function blocks
options = {0 : name,
           1 : age,
           2 : height,

}
opt = int(input("Please Enter 0 for name, 1 for age, 2 for height:: "))
options[opt]()

# 8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.

height = float(input("Your height in metres:"))
weight = int(input("Your weight in kilograms:"))
bmi = round(weight/ (height * height), 1)

if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means you are overweight.')

elif bmi > 30:
     print('Your BMI is', bmi, 'which means you are obese.')

else:
    print('Error!!')

# 9. name="Jayaram" , age=1.6, height=3.5356234, weight=10.343856783
# By using above inputs print the output
# Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
# Note: Use format specifiers(%s, %d, %f)

name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
print("Name:%s, Age:%d, Height:%f, Weight:%f" %(name,age,height,weight))

# 10. Take three upper case letters from the user convert in to small case.
while True:
    n=input("Please enter the name in Caps:")
    if not n.isupper():
      print ("Invalid! name")
    else:
      print("Name:{}".format(n.lower()))
      break

# 11. take base and exponent value from the user and print like in mathematics: example: base=2, exponent=3: 23

base = int(input("ENTER BASE: "))
exponent = int(input("ENTER EXPONENT: "))
if exponent == 0:
  print(1)
else:
  for i in range(exponent):
    if exponent > 0:
        res = base **exponent
  print(res)

  #OR
import math
base = 4
exponent = 2
print(math.exp(exponent*math.log(base)))

# 12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.
import numpy as np
Groceries_cost = [500,1550,1750,2335]
print("Max of cost",max(Groceries_cost))
print("Min of cost",min(Groceries_cost))
print("Total of cost",sum(Groceries_cost))
print("Average of cost",np.mean(Groceries_cost))
