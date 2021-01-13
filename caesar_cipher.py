

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

message = "lbh zhfg hayrnea jung lbh unir yrnearq"
deciphered = ""
shift = 13

for i in range(len(message)):
    char = message[i]
    if char == " ":
        deciphered += " "
    else:
        deciphered += chr((ord(char) + shift - 97) % 26 + 97)

print(deciphered)
print(14 % 26)