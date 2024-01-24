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

myMarks.clear()
print(myMarks)
