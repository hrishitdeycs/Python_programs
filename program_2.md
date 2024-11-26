# Write a program to accpet a number 'n' to perform  the following

## a)Check if 'n' is prime 
```bash
n = eval(input("enter value "))
if n>1:
  for i in range(2,n):
      if n % i == 0:
        print(n,"not a prime number ")
        break
  else:
      print(n,"prime number")
else:
    print(n,"not a prime number ")
```
![Screenshot (7)](https://github.com/user-attachments/assets/7d9c2f50-5979-4d55-b6f9-e87f976732b9)

![Screenshot (8)](https://github.com/user-attachments/assets/1de1be76-f162-4d89-89fe-18549ebc6ec2)
## b)Generate all prime numbers till 'n'
```bash
n = eval(input("enter value "))
for num in range(1,n):
    if num > 1:
        for i in range (2,num):
           if num % i ==  0:
            break
        else:
            print(num,end =',')
```
![Screenshot (9)](https://github.com/user-attachments/assets/6d14a027-535f-467f-a0a5-a037fc982ef7)
## c)Generate first 'n' prime numbers
