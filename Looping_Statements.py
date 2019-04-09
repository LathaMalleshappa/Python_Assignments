# 25. take a number from the user and check whether it is prime?
import math
def is_prime(n):
  if(n==1):
    return n,False
  max_divisor = math.floor(math.sqrt(n))
  for d in range(2,max_divisor+1):
    if(n%d)==0:
      return n,False
  return n,True
for n in range(1,21):
  print(is_prime(n)

# 26. take a string from the user and check contains only digits or not?
# 27. take a string from the user and check contains only alphabets or not?
# 28. take a string from the user and check contains only special chars or not?
# 29.take a string from the user and check contains only capital letters or not?
# 30.take a string from the user and check contains only small letters or not?
string = input("Enter a string value: ")
if(string.isdigit()):
  print("It's a string of digits only")
elif(string.isalpha()):
  if(string.isupper()):
    print("It's a string of Capital letters only")
  elif(string.islower()):
    print("It's a string of small letters only")
  else:
    print("It's a string of aplhabets only")
else:
  print("It's a string of special chars")
# 31. WAP to replace last n occurrence of a substring
mystr = "Remove last occurrence of a BAD word. This is a last BAD word."

removal = "BAD"
reverse_removal = removal[::-1]

replacement = "GOOD"
reverse_replacement = replacement[::-1]

newstr = mystr[::-1].replace(reverse_removal, reverse_replacement, 1)[::-1]
print ("mystr:", mystr)
print ("newstr:", newstr)

# 32. WAP to check given string contains numbers or not. it should consider float numbers also.
import re
string="I am in 20.19 year"
RE_D = re.compile('\d').search(string)
if(RE_D):
  print("string has numbers")

else:
  print("only aplhabetic string")


# 33. Convert the total string in to lower case. Without using lower() function.
string = 'I AM A STUDENT OF THE YEAR!'
print(string.casefold())

# 34. Convert the total string in to upper case. Without using upper() function.
string = "i am a student of the year!"
string1 = ''

for i in string:
    if(ord(i) >= 97 and ord(i) <= 122):
      string1 = string1 + chr((ord(i) - 32))
    else:
        string1 = string1 + i

print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

# 35. Show the below menu to the user until and until user select quit and display corresponding os message
#               Menu:
# 1. windows
# 2. Linux
# 3. Mac
# 4. quit

print(5*'****',' Menu ',5*'****')
print("1. windows")
print("2. Linux")
print("3. Mac")
print("4. quit")

while True:
  choice = input("Please enter your choice: ")
  if not (choice.isdigit()):
    print("Invalid option")
  else:
      if (int(choice)==1) :
        print("Buy windows laptop or mobile!!")

      elif (int(choice)==2):
        print("Linux machines!!")

      elif (int(choice)==3):
        print("Macinthosh!!")

      elif(int(choice)==4):
        exit()

# 36. take a string from the user and check contains at least one digit or not?
string = "It's a 2019 gift!"
if any(c.isdigit() for c in string):
  print("String has numbers too")
else:
  print("string doesn't contain numbers")
                    **OR****

import re
string = "It's a gift!"
match = re.findall('\d',string)
if(match):
  print("Found numbers!!")
else:
  print("No Numbers!!")

# ***********OR**************
import re
digits = re.compile(r'\d')
def contains_digit(s, digits):
  return bool(digits.search(s))
print(contains_digit('I am in 2019',digits))

# 37. take a string from the user and check contains at least one alphabets or not?
import re
s="World"
find = re.match('.*[a-zA-Z].*', s)
if find:
  print("found alphabets")
else:
  print("No alphabets")

# 38. take a string from the user and check contains at least one chars or not?
string = input("Please enter input: ")
if(string):
  print("string has characters")
else:
  print("None")

# 39. take a string from the user and check contains at least one capital letter or not?
string = input("Please enter input: ")
if any(c.isupper() for c in string):
  print("String has atleast one Caps")
else:
  print("String doesn't have atleast one Caps")

# 40. take a string from the user and check contains at least one small letter or not?
string = input("Please enter input: ")
if any(c.islower() for c in string):
  print("String has atleast one small letter")
else:
  print("String doesn't have atleast one small letter")

# 41. Print the first 100 odd numbers

print('\n'.join(map(str, range(1, 100, 2))))
# *********OR*************
print("\n".join(str(i) for i in range(1,100,2)))

# 42. Determine the factors of a number entered by the user
def factors(n):
  return filter(lambda i: n % i == 0, range(2, n + 1))
a=factors(10)
for i in a:
  print(i)
# ************* OR **********************
number = int(input("Please enter a number: "))
for i in range(2,number):
  if(number%i)==0:
    print("%d is a factor of %d" %(i,number))
  else:
    continue

# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This should continue until and until user gives a correct number or want to quit in the middle.
import random
number = random.randrange(10)
print(number)

for i in range(0,4):
  try:
    user = int(input("Guess a number: "))
  except ValueError:
    print("Integer only")
    continue
  if user == number:
    print("Bravo!! You guessed it!!")
    break
  elif user < number:
      print("number is lesser than the entry!!")
  else:
      print("number is greater than the entry!!")
print("It was %d"%number)


# 44. Take two numbers from the user a,b check whether a is divisible by b or not?
a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
if(a/b)==0:
  print("%d is divisible by %d"%(a,b))
else:
  print("%d is not divisible by %d"%(a,b))

# 45. Find the sum of all the multiples of 3 or 5 below 1000
sum=0
for i in range(2,1000):
  if(i%3==0) or(i%5==0):
    sum = sum + i
print("Sum of the multiples of 3 or 5 in range:",sum)

# 46. Write a program to find out big of two numbers
a,b =10,12
if(a>b):
  print("a is greater than b")
else:
  print("b is greater than a")

# 47. Write a program to find out biggest number in the given list.
lst = [1,2,67,89,45,-2]
lst.sort()
print(lst[-1])
# 48. find out third occurrence of given substring
import re
string = "I am I and I am who I am"
print([m.start() for m in re.finditer(r"am",string)][2]) #index 2 is third
occurrence
# **************OR****************************
text = "This is a test from a test ok test"

firstTest = text.find('test')
print(firstTest)
secondTest = text.find('test', firstTest+1)
print(secondTest)
ThirdTest = text.find('test', secondTest+1)
print(ThirdTest)
# ******************OR*******************
def find_2nd(string, substring):
   return string.find(substring, string.find(substring) + 2)
print(find_2nd("I am, I like all subjects, I need","I"))

# 49. find out nth occurrence of given substring
def find_nth(string, substring, n):
   if (n == 1):
       return string.find(substring)
   else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)
print(find_nth("I am I and I am who I","I",3))

 # *********************OR**************************

import re
string = "I am I and I am who I am"
print([m.start() for m in re.finditer(r"am",string)][2])

# 50. Take some single digit numbers from the user and find out min, maximum, sum, average
a,b,c,d = (input("Please enter four single digit numbers seperated by comma: ")).split(',')
print(max(a,b,c,d))
print(min(a,b,c,d))
sum=(int(a) + int(b) + int(c) +int(d))
print(sum)
average =sum /4
print(average)

# 51. WAP> 10 -> 000010, 100 ->  000100, 1000 ->  001000 , 2345678  ->  2345678

lst =[10,100,1000,2345678]
for i in lst:
  print(str(i).zfill(6))

# 52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names.
names  ="emp1,emp2,emp3,emp4"
name=names.split(',')
for i in name:
  print(i)

# 53. Take actual string, source string, destination string. replace first nth occurrences of source string with destination string of actual string.
string = "It is a string example....wow!!! this is really"
print(string.replace("is", "was", 2))

# 54. Take a two numbers from the user and do below menu driven operations
# 1. addition
# 2. multiples
# 3.division
# 4.sqrt
# 5. pow    a**b
# 6.subtraction
# After selection do the corresponding operation.
# Note: user may give int, or float numbers. You should check whether it is proper digits or not. I.e the user given string should be in the position to convert to float. Other wise show the “inproper string given” Error.
import math
while 1:
    a,b =input("Enter a value of a and b in one line using commas\n").split(',')
    if not (a.isdigit()and b.isdigit()):
      print("Invalid data")
    else:
      break
while True:
  ch = input("Enter operatorations ('add','sub','mul','div','power','sqrt'):")
  if(ch not in (['add','sub','mul','div','power','sqrt'])):
    print("Please enter the valid operation!!")
  else:
    a,b=int(a),int(b)
    if ch=='add' :
      Res = a+b
      print("Sum of %d and %d is %d:" %(a,b,Res))
    elif ch=='sub':
      Res=a-b
      print("Subtraction of %d and %d is %d:"%(a,b,Res))
    elif ch=='mul':
      Res=a*b
      print("Multiplication of %d and %d is %d:"%(a,b,Res))
    elif ch=='div':
      Res=a/b
      print("Division of %d and %d is %d:"%(a,b,Res))
    elif ch=='power':
      Res =a**b
      print("Power of %d and %d is %d:"%(a,b,Res))
    elif ch=='sqrt':
      Res = math.sqrt(a)
      Res1 =  math.sqrt(b)

      print("Squareroot of %d,%d is %d,%d:"%(a,b,Res,Res1))
    else:
      exit()

# 56. lst =[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even numbers are there and how many odd numbers are there and how many positive numbers are there and how many negative numbers are there and how many prime numbers are there and how many perfect numbers are there and how many Armstrong numbers are there and how many palindrome numbers are there.
import math
lst =[1,2,3,5,6,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
lst.sort()
# Even, Odd,Positive,Negative,Prime,Perfect,Armstrong ,Palindrome numbers

Even_Odd = ["%d,EVEN"%i if i%2==0 else "%d,ODD"%i for i in lst]
print("Even,ODD numbers in the list are: ",Even_Odd)

#printing positive numbers
positive = ["%d,positive"%i if i>0 else "negative:%d "%i for i in lst ]
print(positive)

#finding Prime numbers
def is_prime(i):
  if(i==1):
    return i,False
  max_divisor= math.floor(math.sqrt(i))
  for d in range(2,1+max_divisor):
    if(i%d)==0:
      return  i,False
  return (i,"is a Prime")

for i in lst:
  print(is_prime(i))

#finding Perfect number
def is_perfect(n):
  sum1 = 0
  for i in range(1,n):
    if( n % i == 0):
      sum1 = sum1 + i
  if (sum1 == n):
    print("%d is a Perfect number!"%n)

for n in lst:
  is_perfect(n)

# check whether a number is an Armstrong number or not in Python
lst =[1,2,3,5,6,7,8,9,153,10,11,12,13,370,20,22,23,24,25,26,27,20,21,22,371,4]
lst.sort()
#153 = 1*1*1 + 5*5*5 + 3*3*3
for num in lst:
  order = len(str(num))
  temp = num
  sum=0
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

  if num == sum:
    print(num)

# Check for Palindrome
a=['122','333','343']
for i in a:
  if(i[::-1]==i):
    print("%s is Palindrome"%i)

# 57. Take a string from the user and find out how many digits are there, how many special symbols are there, how many small letters are there, how many caps are there.
string = input("Enter a String: ")
special_chars=0
numeric =0
alphabets=0
upper =0
for i in string:
  if(i.isdigit()):
    numeric = numeric + 1
  elif(i.isalpha()):
    alphabets +=1
  else:
    special_chars +=1

print(numeric)
print(alphabets)
print(special_chars)


# 58. Take a string of characters or numbers from the user and find out how many number of occurrences are there in given string
string = "Applebee"
dic ={}
for i in string:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
print(dic)

# 59. Take an element from the user and find out how many times the element occurred in given list
lst = ["abc","efg","abc","ght","pol"]
substring ='abc'
print(lst.count('abc'))

# 60. Take an element from the user and find out how many number of occurrences are there in given tuple
lst = ("abc","efg","abc","ght","pol")
substring ='abc'
print(lst.count('abc'))
#
# 61. Reverse the string without affecting the special symbols. It involves three variations. Write code for three variations.
# 62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba
# 63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^
# 64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^

