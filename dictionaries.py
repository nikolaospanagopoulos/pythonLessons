myDict = {
    "name":"john",
    "age":30,
    "city":"New York"
}

print(myDict)

print(myDict["name"])
print(myDict["city"])
print(myDict["age"])

myDict['salary'] = "3000"

myDict["name"] = "george"
myDict["city"] = "L.A"


myDict.pop("city")
myDict.pop("name")

print(myDict)

grades = {'Anna': 88, 'Bob': 76, 'Charlie': 90}

for  name,grade in grades.items():
    print(name,grade)

for grade in grades.values():
    print(grade)

for name in grades.keys():
    print(name)

dict1 = {
    "a":100,
    "b":200,
    "c":300,
    "d":300
}
dict2 = {
    "x":600,
    "y":700,
    "z":800,
    "c":600
}

#This creates a new dictionary without modifying the originals.
margedDict = {**dict1,**dict2}

dict1.update(dict2)
print(dict1)
print(margedDict)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

#This creates a new dictionary without modifying the originals.
merged_dict = dict1 | dict2

grades = {'Anna': 'A', 'Bob': 'B', 'Charlie': 'C'}
invertedGrades = {value: key for key, value in grades.items()}
print(invertedGrades)


items = {'apples': 5, 'bananas': 8, 'grapes': 12}
fullPrice = 0
for price in items.values():
    fullPrice+=price;
print(fullPrice)

employees = {
    'group1':{"name":"John Doe","job":"manager"},
    'group2':{"name":"jane smith","job":"programmer"}
}
employees["group3"] = {"name":"mike","job":"cleaner"}
print(employees)
print(employees["group2"]["name"])

#create a new dictionary containing only products whose price is higher than 0.5
product_prices = {'apple': 0.45, 'banana': 0.30, 'orange': 0.55, 'pear': 0.80}
#1 create the new empty dictionary
filteredProducts = {}

for key,value in product_prices.items():
    if value>0.5:
       filteredProducts[key] = value

print(filteredProducts)

studentList = [];

studentList.append({"name":"john","grade":10})
studentList.append({"name":"jace","grade":8})
studentList.append({"name":"john","grade":7})
studentList.append(5)

print(studentList)

names = ['Alice', 'Bob', 'Charlie', 'David']
professions = ['Engineer', 'Doctor', 'Artist',"Driver","Pilot"]
professionsDict = {}
for index,job in enumerate(professions):
    if index<len(names):
        professionsDict[job]=names[index]



print(professionsDict)
#programmatically write a string like "Index: 0, value: apple"    (enumerate)
my_list = ['apple', 'banana', 'cherry']
#write a function that takes a day as an argument and returns list of fruit sold on that day
#example output ["apples","oranges"]
exerciseList = [{'apples': "tuesday", 'bananas': "friday"}, {'apples': "tuesday", 'oranges': "thursday"}, {'bananas': "friday", 'cherries': "wednesday"}]
#merge in a dictionary -> zip
#example output {"name":"Alice","age":25.....
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
#create a dictionary from a nested list
nested_list = [['name', 'Alice'], ['age', 25], ['city', 'New York']]
#example output {"name":"Alice","age":25.....
#extra exercise
#count vowels but count each vowel
#example -> hello word -> {"e":1,"o":1} -> if key exists update it , if it doesnt exist, create it, "aeouiAEOUI"
#can work on any String