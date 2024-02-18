#Conversions below:

'''
int()
float()
bool()
str()
'''

#Our Own Tests:
str1 = "hello"
str2 = "world"
print(str1 + str2)
print(str1, str2)
print()
print(10/3)#returns decimal
print(10//3)#returns whole number
print(10%3)#returns remainders
print()
print(10**3)#NOTE:This is how exponents work (returns 1000)
x = 10
x += 3#Same as Java
print(x)
y = 10 + 3 * 2
print("Without paranthesis: 10 + 3 * 2 = " + str(y))
y = (10 + 3) * 2
print("With paranthesis: (10 + 3) * 2 = " + str(y))
print()
if y == 26:
    print("y does in fact equal 26")
elif y != 26:
    print("y does not equal 26")
print()
while y <= 30:
    print("* " + str(y))
    y += 1
print()
myNums = []#this is a list(equivalent to arraylist in Java) NOTE: [] brackets are only to define lists
for i in range(10):
    myNums.append(i)#we add to the list
    print(myNums[i])#we print what is within the list at that index
print(myNums)
print()
myNames = ["Tom", "John", "Bob", "Sam", "Mary", "Leslie"]
print(myNames[-2])#prints the second to last entry 'Mary'
print(myNames)
myNames[-2] = "Valerie"#we update the name held at this given index
print(myNames)
print(myNames[0:3])#prints the first 3 entries (inclusive 0, exclusive 3)
print()
#NOTE:Here we practice 'tuples' where tuples are IMMUTABLE lists meaning once set, the values can't be changed
#Additional NOTE: to define a tuple, you use paranthesis ()
numbers = (1, 2, 3)
#numbers[0] = 10 #NOTE: this will give an error
print(numbers[1])

#NOTE:Here we use a dictionary which is equivalent to a hashmap from Java, to define dicts we use curly brackets {}
#NOTE:Duplicates aren't allowed in dictionaries, so if you try to add the same thing again, it will instead update the value of
#what is already in there
myDict = {"Joshua" : 23, "Larry" : 32, "Gary" : 7}#name : age
print(myDict)#prints the entire dict
print("Joshua's age: " + str(myDict["Joshua"]))#returns the value attached to the key given

#checks such as Bools and those in math:

'''
>
<
==
>=
<=
!=
and
or
(ex. 10 > 3 and 10 < 30)#returns True
(ex. 10 > 3 or 10 < 3)#returns True
'''

