string = "good"
vowels = ["a", "e", "i", "o", "u"]
empty_string = ""

#for loop that runs through each index in string first
# then checks to see if each string[index] is in the list vowels
# after that - setting the letter to be replaced to string[index of letter] helped simplify things in end expression
# diong the same for the "range" of double vowels - use 2 because +1 doesn't do anything doofus
# and then setting empty string = result of replacement

for i in range(len(string)):
    if string[i] in vowels:
        if string[i] == string[i+1]:
            letter = string[i]
            double = string[i:i+2]
            empty_string = string.replace(double, letter*5)

print(empty_string)

#loop through string
# if you encouter vowel check if next one is vowel