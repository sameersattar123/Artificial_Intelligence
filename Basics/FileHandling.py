# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("sameer sattar shaikh")
f.close()

# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write(" Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write(" Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

