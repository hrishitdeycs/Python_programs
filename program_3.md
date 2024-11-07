# WAP to create a pyramid of the character '*' and reverse pyramid
```bash
n = int(input("enter the no of rows "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end =" ")
    print()
for i in range (n):
    for j in range (i+1):
        print(" ",end = " ")
    for j in range(2*n-2*i-3):
        print("*",end =" ")
    print()
```
![Screenshot (10)](https://github.com/user-attachments/assets/150e10da-d511-49e9-a660-e4d0a96c1229)
