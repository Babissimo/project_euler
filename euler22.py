namesFile = open("0022_names.txt", "r") 

namesString = namesFile.read() 
 
names = namesString.replace("\"","").split(",")
names.sort()

def nameValue(name):
    nameVal = 0
    for c in name:
        nameVal += ord(c) - 64
    return nameVal

listValue = 0

for i in range(len(names)):
    listValue += nameValue(names[i])*(i+1)

print(listValue)