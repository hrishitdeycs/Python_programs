# Write a function that accepts two strings and returns the indices of all the occurances of the second string in the first string as a list . if the second string is not present in the first string then it should return -1.
```bash
def occurances(a,b):
    newlist =[]
    if b not in a:
       print(-1)
    else:
       i= 0
       while i< len(a):
            c=a.find(b,i)
            if c== -1:
              break
            i= c+ len(b)
            newlist.append(c)
        print(newlist)
a= input("enter first string ;")
b= input("enter second string ;")
occurances(a,b)
```
![Screenshot (20)](https://github.com/user-attachments/assets/fe2f739c-8695-4fe0-a1fd-5e71e3efb18e)
