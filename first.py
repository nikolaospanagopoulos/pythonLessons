# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import collections
#PRIMITIVE
# Integer
x = 5


# Float
y = 3.14

# Boolean
is_valid = True

#char
char = 'a'

#None
none_val = None

# String
my_string = 'Hello, World!'

#____________________________________________________________


# List
my_list = [1, 2, 3, 4, 5]

# Range
my_range = range(1, 10)

# Tuple
my_tuple = (10, 20, 30)

# Dictionary
my_dict = {'name': 'John', 'age': 30}

# Set
my_set = {1, 2, 3, 4, 5}


#----------------------Strings-------------------------------


myString = "helloworld"
myNewString = myString.capitalize() #Hello

print(myString.strip()) #remove space before and after

print(myString.replace('hello','Hi'))

print(myString.find("w")) #returns position

print(myString.split(','))#splits and returns list

print(myString.startswith("hello")) #returns true if string starts with all the specified chars

print(myString.endswith("!")) #returns true if string ends with all the specified chars

print(len(myString)) #size of String

print(myString.isalpha()) #returns if chars are from a-z A-Z

print(myString.isdigit()) #returns if chars are from 0-9

mySymbolStr = "#$#$$$%"
print(not mySymbolStr.isalnum())

if(not mySymbolStr.isalnum()):
    print("contains symbols")
else:
    print("is alphanumerical")

vowels = "aeiouAEIOU"
strCountVowels = "hello"
count = 0
for char in strCountVowels:
    if(char in vowels):
        #count = count + 1
        count +=1

print(count)
print('_______________________________')

for num in range(1,11):
    print(num)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    pass
    # if fruit == "apple":
    #     print("found apple and stopping")
    #     break
for fruit in fruits:
    if fruit == "apple":
        continue
    print("fruit except apple: "+fruit)
    
    #print(fruit)


exampleString = "hello"
#print(exampleString[::-1])

palindromeString = "Level"
palindromeString2 ="vue"

#Level
#level
#level == level

#vue
#vue == euv
#false
stringToLowerCase = palindromeString.lower()
print(stringToLowerCase)
reversedString = stringToLowerCase[::-1]
print(reversedString)
print(reversedString == stringToLowerCase)


string1 = "listen"
string2 = "silent"

print(sorted(string1.lower()) == sorted(string2.lower()))

reversedString = ""
toReverse = "hello"

for char in toReverse:
    reversedString = char+reversedString
    #h+"" = h
    #e+"h" = eh
    
print(reversedString)
    

# 1. Counter
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = collections.Counter(my_list)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 2. Deque
deque = collections.deque([1, 2, 3])
deque.append(4)
deque.appendleft(0)
print(deque)  # Output: deque([0, 1, 2, 3, 4])

# 3. NamedTuple
Point = collections.namedtuple('Point', ['x', 'y'])
point = Point(3, 5)
my_tuple = (3,5)
print(point.x, point.y)  # Output: 3 5

# 4. OrderedDict
ordered_dict = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 5. DefaultDict
default_dict = collections.defaultdict(int)
default_dict['a'] = 1
print(default_dict['b'])  # Output: 0 (default value for new keys)

# 6. ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = collections.ChainMap(dict1, dict2)
print(chain_map['a'])  # Output: 1
print(chain_map['c'])  # Output: 3


#StringToCountCapials = "HellO"
#you need to find a way to check if a letter is capital
#char.isupper char.islower
#Exercise 1: Count Uppercase and Lowercase Letters

#Remove duplicates StringToRemoveDuplicated = "123 123 456 hello hello bye"
#set

#sentance = "i love eating pancakes"
#capitalize words


