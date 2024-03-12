def sayHello(firstName,lastName):
    print(f"hello {firstName} {lastName}")


sayHello("john","doe")

myNum = 5;
def calculateSum(num1,num2):
    num1 = 40
    num2=800
    return num1+num2
print(myNum,"!!!!")

number1=10
number2=20
result =  calculateSum(number1,number2)
print(number1,number2)
print(result)


def tryToChangeVar(num):
    num = 80


numberToChange = 50

tryToChangeVar(numberToChange)

globalNumber = 30



def changeGlobalNum():
    globalNumber = 80


print("before change: ",globalNumber)
changeGlobalNum()
print("after change: ",globalNumber)


myList = [5,6,7,8]

def changeList(listToChange):
    listToChange.append(30)
    
print("before change: ",myList)
changeList(myList)
print("after change: ",myList)




my_list = [50,80,900,700,50]

for element in my_list:
    print(element)




def calculateAvg(listToCalc):
    res = 0
    for element in listToCalc:
        res = res + element
    #print(f"sum = {res}")
    avg = res // len(listToCalc)
    return avg
    



average = calculateAvg(my_list)
print(f"average equals {average}")


list_to_insert = [50,50,50,70]
 

list_to_insert.insert(2,100)
list_to_insert.append(800)
#remove(): Removes the first occurrence of an element from the list.
list_to_insert.remove(50)
removed = list_to_insert.pop()
print(f"removed element {removed}")
list_to_insert.sort()
#list_to_insert.reverse()
print(list_to_insert)
#METHODS THAT DO NOT CHANGE LIST
position = list_to_insert.index(70)
print(f"occurances {list_to_insert.count(50)}")
print(f"70 position: {position}")
copiedList = list_to_insert.copy()

exerciseList = [6,8,10,90,78,68,7]
exerciseList2 = [6,8,17,50]
#function that return result

#calculate sum
#find largest number
#find smallest number
#find odd and even and print them -> odd: 7, even: 8 -> number % 2 == 0 ->for loop
#find common elements and return a list with them ->[6,8]



