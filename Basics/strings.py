name = "Sameer Sattar"
print(name)

# capital
print(name.upper())

# small
print(name.lower())

# finding any letter / word 
print(name.find("S")) # 0 index
print(name.find("a")) # 1 index
print(name.find("d")) # -1 index  (-1 means not found)

# replacing any word/letter 
print(name.replace("Sameer" , "sattar"))
print(name.replace("Sattar" , "sameer")) 

# check any letter / word exist or not 
print("s" in name) # false
print("S" in name) # true
