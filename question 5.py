#List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#a. Write a Python program to print a specified list after removing 4th element.
#expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
#b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
#Do that in one line code.

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print(color)
