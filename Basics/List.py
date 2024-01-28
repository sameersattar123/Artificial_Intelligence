# Lists
marks = [33,44,55,66]

marks.append(77)

print(marks) # [33, 44, 55, 66, 77]

marks.insert(0,22)

print(marks) # [22, 33, 44, 55, 66, 77]

marks.insert(6,88)

print(marks) # [22, 33, 44, 55, 66, 77, 88]

myMarks = [22, 33, 44, 55, 66, 77, 88]

i = 0
while i < len(myMarks):
    print(myMarks[i])
    i = i + 1

for item in myMarks:
    print(item)
    i = i + 1

myMarks.clear()
print(myMarks)

#Tuple
UniMarks = (44 , 55 , 66  , 66 ,66 ,66)
# UniMarks[0] = 33 'tuple' object does not support item assignment
print(UniMarks.count(66)) # count the number which is repeat in tuple by using tuple method
print(UniMarks.index(55)) # identify the number position in tuple by using index method 
print(UniMarks.index(66)) # identify the number position in tuple by using index method 
print(UniMarks)

# Set 
UniqueElements = {3,4,4 ,4,4,4,44,45,6,7,8,8,8,8}
# UniqueElements[0] = 33 #'set' object does not support item assignment
print(UniqueElements)

for marks in UniqueElements:
    print(marks) # order does not matter in set but they are unique 

# Dictionary

information = {
    "fatherName" : "Abdul Sattar",
    "MotherName" : "Khalida Sattar",
    "BrotherName" : "Daniyal Sattar",
    "SitterName" : "Paras Sattar",
} 

print(information["fatherName"])
print(information["MotherName"])
information["SitterName"] = "Paras"
print(information)

