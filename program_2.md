# Write a program to accpet a number 'n' to perform  the following

## a)Check if 'n' is prime 



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
```bash
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
n=int(input("Enter number of prime numbers :"))
print(generate_primes(n))
```
![Screenshot (32)](https://github.com/user-attachments/assets/6a5a240f-0bfd-4562-adc5-9029673cc8c7)
