string = "hello welcome to python"
character = input("enter a character ")
f = 0
for i in string:
    if i == character:
        f += 1
print("frequency of",character,'is',f)
string = "hello welcome to python"
print(string.replace("h","t"))
def remove_first_occurrence(s, char):
    index = s.find(char)
    if index != -1:
        return s[:index] + s[index+1:]
    return s
string = input("Enter the string: ")
char_to_remove =input("Enter the character to remove: ")
result = remove_first_occurrence(string, char_to_remove)
print(result) 
def remove_char(string, char):
    return string.replace(char, '')
input_string = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")
result = remove_char(input_string, char_to_remove)
print(result) 
