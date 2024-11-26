# Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10)
# Write a program to perform following oprations:
# a)Print half the values of the tuple in one line and other half in the next line.
```bash
t1 = (1,2,5,7,9,2,4,6,8,10)
half_value=len(t1)//2
first_half = t1[ :half_value]
print("first_half", first_half)
second_half = t1[half_value: ]
print("second_half", second_half)
```
![Screenshot (12)](https://github.com/user-attachments/assets/0a11d248-8965-405a-a5e5-15029a3c18d8)
# b)Print another tuple whose values are even numbers in the given tuple.
```bash
t1 = (1,2,5,7,9,2,4,6,8,10)
even_number= tuple(filter (lambda x: x%2==0,t1))
print("tuple with even number", even_number)
```
![Screenshot (13)](https://github.com/user-attachments/assets/a2c2a2f9-1b70-49a8-a51a-f2aa9fd76283)

# c)Concatenate a tuple t2 = (11,13,15) with t1.
```bash
t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)
concatenation = (t1 + t2)
print("tuple with concatenation ", concatenation)
```
![Screenshot (14)](https://github.com/user-attachments/assets/12ea5d12-2c50-4269-8c30-e6e1b59f04ee)

# d)Return maximmum and minimum value from this tuple.
```bash
t1= (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
print("maximum value in t1 is ",max(t1))
print("minimum value in t1 is ",min(t1))
```
![Screenshot (15)](https://github.com/user-attachments/assets/e279a9d4-6f2a-4db7-924f-3f081cd39f08)


