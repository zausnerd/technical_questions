# # Question 2 -- decodeString(s): Given an encoded string, return its corresponding decoded string. 

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer. 

# For s = "4[ab]", the output should be decodeString(s) = "abababab" 
# For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"


def decodeString(string):
    multiplier = ''
    current_string = ''
    for idx, char in enumerate(string):
        if char.isdigit():
            multiplier += char
        elif char.isalpha():
            current_string += char
        elif char == '[':
            substring = decodeString(string[idx + 1:])
            if multiplier == '':
                multiplier = '1'
            current_string += int(multiplier) * substring
            return current_string
    return current_string

print(decodeString("2[b3[a]]"))
print(decodeString("4[ab]"))
print(decodeString("[abcd]"))
print(decodeString(""))
