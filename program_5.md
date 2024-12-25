# Write a program to perform the following operations on a string
## a)Find the frequency of a character in a string
```bash
string = "hello welcome to python"
character = input("enter a character ")
f = 0
for i in string:
    if i == character:
        f += 1
print("frequency of",character,'is',f)
```
![Screenshot (15)](https://github.com/user-attachments/assets/a20283bf-6d3a-4e0c-940a-84700fd2f560)

## b)Replace a character by another character in a string 
```bash
string = "hello welcome to python"
print(string.replace("h","t"))
```
![Screenshot (16)](https://github.com/user-attachments/assets/b5c04616-6540-4242-be6f-0c59454db425)

## c)Remove the first occurance of a character from a string
```bash
def remove_first_occurrence(s, char):
    index = s.find(char)
    if index != -1:
        return s[:index] + s[index+1:]
    return s
string = input("Enter the string: ")
char_to_remove =input("Enter the character to remove: ")
result = remove_first_occurrence(string, char_to_remove)
print(result)  
```
![Screenshot (51)](https://github.com/user-attachments/assets/85613046-162a-47d2-a881-b8844f517e76)


## d)Remove all occurances of a character from a string
```bash
def remove_char(string, char):
    return string.replace(char, '')
input_string = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")
result = remove_char(input_string, char_to_remove)
print(result) 
```

![Screenshot (52)](https://github.com/user-attachments/assets/262a3804-f15d-48d5-ab1c-23e300d32c4a)
