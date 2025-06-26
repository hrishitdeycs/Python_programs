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
n = eval(input("enter value "))
for num in range(1,n):
    if num > 1:
        for i in range (2,num):
           if num % i ==  0:
            break
        else:
            print(num,end =',')
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

