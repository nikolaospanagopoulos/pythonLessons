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
print("INVERTED GRADES")
grades = {'Anna': 'A', 'Bob': 'B', 'Charlie': 'C'}
#invertedGrades = {value: key for key, value in grades.items()}

def invertGrades(grades):
    invertedGrades = {}
    for key,value in grades.items():
        invertedGrades[value] = key
    return invertedGrades

print(invertGrades(grades))

# print(invertedGrades)


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
print("PROFESSIONS EXAMPLE")
names = ['Alice', 'Bob', 'Charlie', 'David'] #4
professions = ['Engineer', 'Doctor', 'Artist',"Driver","Musician"] #4
professionsDict = {}
for index,job in enumerate(professions):
    print(index,job)
    if(index<len(names)):
        professionsDict[job]=names[index]




print(professionsDict)
#programmatically write a string like "Index: 0, value: apple"    (enumerate)
my_list = ['apple', 'banana', 'cherry']




# def writeAStringFromList(myList):
    # for index,fruit in enumerate(myList):
    #     print(f"index: {index}, value: {fruit}")

# writeAStringFromList(my_list)

#enumerate gives indexes to iterrables (list)
for index,fruit in enumerate(my_list,start=1):
    print(f"index: {index}, value: {fruit}")

for index in range(0,len(my_list)):
    print(f"index: {index}, value: {my_list[index]}")


#write a function that takes a day as an argument and returns list of fruit sold on that day
#example output ["apples","oranges"]
exerciseList = [
    {'apples': "tuesday", 'bananas': "friday"},
    {'apples': "tuesday", 'oranges': "thursday"},
    {'pineapples': "friday", 'cherries': "wednesday"}]


def fruitsSoldOnDay(day,list):
    fruitsSoldOnSpecificDay = []
    for fruitRecord in list:
        print("fruit record",fruitRecord)
        for fruit, saleDay in fruitRecord.items():
            print(fruit,saleDay)
            if(saleDay.lower() == day.lower()):
                fruitsSoldOnSpecificDay.append(fruit)

    return fruitsSoldOnSpecificDay


catalogue = fruitsSoldOnDay("friday",exerciseList)

print(catalogue)

#merge in a dictionary -> zip
#example output {"name":"Alice","age":25.....
keys = ['name', 'age', 'city'] #keys
values = ['Alice', 25, 'New York'] #values

def createDictionaryFromLists(keys,values):
    result = {}
    for index in range(0,len(keys)): #0-3
        result[keys[index]] = values[index]

    print(result)

createDictionaryFromLists(keys,values)











#create a dictionary from a nested list
nested_list = [
    ['name', 'Alice'],
    ['age', 25],
    ['city', 'New York']
]

print("NESTED LIST EX")
def createDictionaryFromNestedList(nested):
    resultDict ={}
    for pair in nested:
        print(pair)
        key = pair[0]
        value = pair[1]
        resultDict[key] = value
    return resultDict


resultDict = createDictionaryFromNestedList(nested_list)

print(resultDict)





#example output {"name":"Alice","age":25.....
#extra exercise
#count vowels but count each vowel
#example -> hello word -> {"e":1,"o":2} -> if key exists update it , if it doesnt exist, create it, "aeouiAEOUI"
#can work on any String

def countVowels(s):
    vowels = "aeouiAEOUI"
    vowelsDict = {}


    for char in s:
        if char in vowels:
            if char.lower() in vowelsDict:
                vowelsDict[char.lower()] +=1
            else:
                vowelsDict[char.lower()] = 1
    return vowelsDict

print(countVowels("hello world"))

