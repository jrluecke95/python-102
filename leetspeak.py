string = "I am a leet programmer"

for i in string:
    if i.upper() == "A":
        string = string.replace("a", "4")
    if i.upper() == "E":
        string = string.replace("e", "3")
    if i.upper() == "G":
        string = string.replace("g", "6")
    if i.upper() == "I":
        string = string.replace("i", "1")
    if i.upper() == "O":
        string = string.replace("o", "0")
    if i.upper() == "S":
        string = string.replace("s", "5")
    if i.upper() == "T":
        string = string.replace("t", "7")
    
print(string)

