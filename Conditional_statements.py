#Conditional statements

# 13.Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs, decide whether there is sufficient buses or not and give solution for how many extra buses required.
try:
  num_Passengers = int(input("Please Enter no. of Passengers:: "))
  bus_capacity = int(input("Please enter no. of seats a bus can occupy:: "))
  num_buses = int(input("Please Enter no. of buses:: "))

  buses_required = num_Passengers/bus_capacity
  if(num_buses < buses_required):
    print("%d Buses are not sufficient for %d people"%(num_buses,num_Passengers))
    print("We need %d more buses to fit the Passengers"%(buses_required-num_buses))
  else:
    print("Buses are sufficient to fit passengers")
except( ValueError ):
  print ("It has to be an integer")

# 14.Take number from the user decide whether it is even or odd.
try:
  num = int(input("Please Enter the number: "))
  if(num%2==0):
    print("%d is even"%num)
  else:
    print("%d is odd"%num)
except( ValueError ):
  print ("It has to be an integer")


# 15.take number from the user decide whether it is positive number or negative number

try:
  num = int(input("Please Enter the number: "))
  if(num<0):
    print("%d is negative number" %num)
  elif(num>0):
    print("%d is positive number" %num)
  else:
    print("%d is neither -ve nor +ve" %num)
except( ValueError ):
  print ("It has to be an integer")


# 16.take a string from the user print the length. if the user not given anything then show an error message
Str =input("Please Enter the string: ")
length = len(Str)
if length is 0:
  print("Error!! Nothing entered")
else:
  print("Length of str is %s" %length)


# 17. code to perform mathematical operations. take two numbers from the user and show the below menu
# 	1. add,
# 	2. sub,
# 	3. mul,
#  	4.div,
# 	5.quit
# 	Enter an option: based on the option need to perform an operations


while 1:
    a,b =input("Enter a value of a and b in one line using commas\n").split(',')
    if not (a.isdigit()and b.isdigit()):
      print("Invalid data")
    else:
      break
while True:
  ch = input("Enter operators (+, -,*,/):")
  if(ch not in (['+','-','*','/'])):
    print("Please enter the valid operation!!")
  else:
    a,b=int(a),int(b)
    if ch=='+' :
      Res = a+b
      print("Sum of %d and %d is %d:" %(a,b,Res))
    elif ch=='-':
      Res=a-b
      print("Subtraction of %d and %d is %d:"%(a,b,Res))
    elif ch=='*':
      Res=a*b
      print("Multiplication of %d and %d is %d:"%(a,b,Res))
    elif ch=='/':
      Res=a/b
      print("Division of %d and %d is %d:"%(a,b,Res))
    else:
      exit()


# 18. show the menu:
#    		 1. kids
#     		2. Men's
#    		 3. Women's
#   Show the corresponding message based on the selection. Mention error message if he enter >3.
while True:
  try:
    ch= int(input("Enter any number in the list [1,2,3]: "))
    if(ch==1):
      print("We are kids Hurray!!!")
    elif(ch==2):
      print("We are Men Yay!!")
    elif(ch==3):
      print("We are Women woo!!")
    else:
      print("invalid option")
      break
  except(ValueError):
    print("Type only integers")

# 19. write a program to chcek given substring is there in actual string or not?
# example: act="python is a pure object-oriented programing language"
# check whether “pure” is there in act or not. Note: Use in operator

act="python is a pure object-oriented programing language"
sub ="pure"
lst = act.split(" ")
if(sub in lst):
  print("success!!")
else:
  print("couldn't match the substring!!")

# 20. Take three numbers from the user and decide which is big
while 1:
  a,b,c = input("Enter three integers seperated with commas:\n").split(",")
  if not(a.lstrip('-').isdigit() and b.lstrip('-').isdigit() and c.lstrip('-').isdigit()):
    print("Enter valid integers!!")
  else:
    a,b,c=int(a),int(b), int(c)
    x= max(a,b,c)
    print("Max of %d,%d,%d is %d" %(a,b,c,x))
    break

# 21. Take age and gender from the user and decide whether he is eligible for marriage in India or not. Age criteria: men age>22, women>18
while 1:
  age,gender = input("Enter valid age, gender seperated with commas:\n").split(",")
  if not(age.isdigit() and (gender=='m' or "f")):
    print("Please enter a valid age and gender")
  else:
    if((gender == 'm' and (int(age)<22)) or(gender=='f' and (int(age)<18))):
      print("Not eligible for marriage")
    else:
      print("It's time to marriage!!")
  break

# 22. Take an age and gender from the user: and mention that what he/she can do in india.
#
# 		conditions
# 1. Theatre: 5 for men 7 for women
#     	2. Voting system: 18 for men and women
#     	3. Marriage in india: 23 for men and for women >21
#     	4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women
#    	 5. For driving license: (min:18, max:60) for men and women
# 	Eligibility:
#    		1. theatre
# 			2.  Voting system
# 			3.  Marriage in india
# 			4.  For govt obs
# 			5. For driving licence:
# 	Enter an option:
# 		Gender:
# 			1. men
# 			2. women
# 	Enter an option:
# 		Enter an age of person:
       ## Your menu design here
print(25 * "-" , "MENU" , 25 * "-")
print("1. Female")
print("2. Male")
print(60 * "-")
while True:
    choice = int(input("Enter your choice [1 or 2]: "))
    age = int(input("Enter the age of the person: "))

    if ((choice==1 and age>=5)or(choice==2 and age>=7)) :
        print("option %s with age %d can watch movie in Theatre!!"%(choice,age))

    if (choice==1 and age>=18)or(choice==2 and age>=18) :
        print("option %s with age %d can vote in India!!"%(choice,age))
    if (choice==1 and age>=21)or(choice==2 and age>=18) :
        print("option %s with age %d can get married"%(choice,age))
    if (choice==1 and (18<=age<=32))or(choice==2 and (18<=age<=34)) :
        print("option %s with age %d can join a government job"%(choice,age))

    if (choice==1 and (18<=age<=60))or(choice==2 and (18<=age<=60)) :
        print("option %s with age %d can apply for a DL"%(choice,age))
    else:
      break

# 23. operating systems:
# 	1.windows
# 	2.android
# 	3.mac
# Enter an option:
# If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
# If the user enters 2 then show "Goto second floor and buy adroid mobiles"
# If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
# If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"
       ## Your menu design here
print(25 * "-" , "MENU" , 25 * "-")
print("1. Windows")
print("2. Android")
print("3. Macinthosh")
print(60 * "-")

while True:
  choice = input("Enter of your choice [1,2,3]: ")
  if not (choice.isdigit()):
    print("Invalid Entry!! please re-enter")
  else:
    if (int(choice)==1) :
      print("Goto first floor and buy windows laptop or mobile!!")

    elif (int(choice)==2):
      print("Goto second floor and buy adroid mobiles!!")

    elif (int(choice)==3):
      print("Goto third floor and buy mac laptops")

    else:
      print("There is only three floors, please select 1 or 2 or 3")

# 24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old ager.

while True:
  age = input("Please enter the age: ")
  if not (age.isdigit()):
    print("Invalid age, please enter valid age!!")
  else:
    age=int(age)
    if(0<=age<=2):
      print("You are a Baby!!")
    elif(2<age<=5):
      print("You are a Toddler!!")
    elif(5<age<=12):
      print("You are a Child!!")
    elif(12<age<=19):
      print("You are a Teenager!!")
    elif(19<age<=25):
      print("You are a Young Adult!!")
    elif(25<age<=59):
      print("You are an Adult!!")
    else:
      print("You are an Elder!!")
# 25.Take two number a,b from the user and check whether a is divisible by b or not
def Divisible(a,b):
  if(a%b==0):
    print("%d is divisible by %d"%(a,b))
  else:
    print("%d is not divisible by %d"%(a,b))
Divisible(8,8)
