print('hello python')

..............................................................

...... for and array
numbers = [1, 2, 3, 4, 5]
for i in numbers: print((i+2)*5)

..............................................................

......inputs, read from user
num1 = input("enter num 1: ")
num2 = input("enter num 2: ")

num1 = int(num1)
num2 = int(num2)

..............................................................

......functions
def sum(a, b):
    print(a + b)        

def diving(a, b):
    print(a * b)

def printdata(number1, number2):
    print(sum(number1, number2))  
    print(diving(number1, number2))  

print(printdata(num1, num2))

..............................................................

......operoter
print(5 >= 7)
print(5 is 7)
print(5 is not 7 and 3 is not 4)
print(5 is not 5 or 3 is not 3)

..............................................................

...... if, else condations
static_number = 5
if(static_number > 5):
    print(static_number+5)
elif(static_number < 6):
    print(static_number+3)
else:
    print(static_number)

..............................................................

......lists 
list1 = [1, 2, 3, 4, 5]
list1[1] = 5
delete all list, if i need to delete some of indexs i will put it in a list like (list1[0]) 
del(list1)
for i in list1: print(i)

....... sum tow list

firstName = ['yousef', 'mohammed', 'khaled']
lastName = ['shallah', 'sameh', 'farg']
fullName = firstName + lastName

for j in firstName: 
    print(j)

for q in lastName:
    print(q)

print(fullName)

..............................................................

