'''
Question 1 -- sortByStrings(s,t): Sort the letters in the string s by the order they occur in the string t.
You can assume t will not have repetitive characters. For s = "weather" and t = "therapyw",
the output should be sortByString(s, t) = "theeraw".
For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".

'''


def sortByStrings(string, index_string):
    letter_to_idx = dict(reversed(kv) for kv in enumerate(index_string))
    string = sorted(string, key=lambda char: letter_to_idx[char])
    return ''.join(string)

print(sortByStrings('weather', 'therapyw'))
print(sortByStrings('good', 'odg'))
