WaP to create a list of only the even integers appearing in the input list(may have elements of other types) using for loop and list comprehension.
```bash
def cubes(): 
    newlist= []
    number = [1,2,3,4,5,6,"seven"]
    for i in number:
        if type(i)== int:
            if i % 2 == 0:
                newlist.append(i**3)
    print(newlist)
cubes()
```
![Screenshot (10)](https://github.com/user-attachments/assets/b1ec9a0d-2aea-434c-ba16-6cbecdc96b99)
