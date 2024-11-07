# WAP to swap the first n characters of two strings
```bash
str1 = input("enter first string: ")
str2 = input("enter second string: ")
n1 = int(input("enter no of character which is to be swap: "))
n = str1[ :n1]
m = str2[ :n1]
if n1 <= min(len(str1),len(str2)):
    print(str1.replace(n,m))
else:
    print(str2.replace(m,n))
```
![Screenshot (19)](https://github.com/user-attachments/assets/808ea245-b739-479f-a89b-6bc09038d012)
