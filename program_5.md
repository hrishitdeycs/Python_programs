# WAP to perform the following operations on a string
## a)find the frequency of a character in a string
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

## b)replace a character by another character in a string 
```bash
string = "hello welcome to python"
print(string.replace("h","t"))
```
![Screenshot (16)](https://github.com/user-attachments/assets/b5c04616-6540-4242-be6f-0c59454db425)

## c)remove the first occurance of a character in a string
```bash
string = "hello welcome to python"
print(string[1:len(string)])
```
![Screenshot (17)](https://github.com/user-attachments/assets/8995a27c-d169-43b2-93d9-a46d9717f4f0)

## d)remove the all occurance of a character from a string
```bash
string = "hello welcome to python"
print(string[:0])
```
![Screenshot (18)](https://github.com/user-attachments/assets/7c78ee81-10ea-4503-b23a-4505b6c1860e)
