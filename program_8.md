# Write a program to create a list of the cubes of only the even integers appearing in the input list(may have elements of other types) using the following:
# a)'for' loop 
# b)list comprehension.
```bash
test = []
n = int(input('enter the length of list \n'))
for j in range(0, n):
    vals = input('enter the values: ')
    test.append(vals)
cubes = []
for i in test:
    if str(i).isdigit():
        if int(i) % 2 == 0:
            i = int(int(i) ** 3)
            cubes.append(i)
print('The cubed values of all the even digits in the given list using for loop are: ')
print(cubes)
list_comp = [int(cube)**3 for cube in test if cube.isdigit() and int(cube) % 2 == 0]
print('The cubed values of all the even digits in the given list using list comprehension are: ')
print(list_comp)
```
![Screenshot (33)](https://github.com/user-attachments/assets/d5aaae2b-4f23-416f-b6c0-772be61b3e39)

