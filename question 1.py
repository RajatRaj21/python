#1. For a given input string “Python is a case sensitive language”. Write python
#code for the following:
#a. Find the length of the input string.
#b. Reverse the order of the string in one line code.
#c. Using Slice function store “a case sensitive” in new string.
#d. Replace “a case sensitive” with “object oriented”.
#e. Find index of substring “a” in the given input string.
#f. Remove the white spaces from the given input string.

string="Python is a case sensitive language."
print(string,"length of given string is :",len(string))

print("reverse order of string :",string[::-1])

print("the sliced string is :",string[10:26])

string2=string[0:10]+"object oriented"+string[26:50]
print("the new updated string :",string2)

print("index of string 'a' in the string :",string2.find("a"))

print("string without whitespaces :",string.replace(" ",""))



