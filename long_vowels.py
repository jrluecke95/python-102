string = "good"
vowels = ["a", "e", "i", "o", "u"]
empty_string = ""

for i in range(len(string)):
    if string[i] in vowels:
        if string[i] == string[i+1]:
            letter = string[i]
            print(letter)
            double = string[i:i+2]
            print(double)
            empty_string = string.replace(double, letter*5)

print(empty_string)


#loop through string
# if you encouter vowel check if next one is vowel