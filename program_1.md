# WAP to find the roots of a quadratic equation
```bash
a,b,c = eval(input("enter value "))
d = b ** 2 - 4 * a * c
r1 = (-b + (d) ** 0.5) / 2 * a
r2 = (-b - (d) ** 0.5) / 2 * a
if d >=0:
    print("roots are real ",r1,r2)
else:
    print("roots are not real",r1,r2)
```
![Screenshot (6)](https://github.com/user-attachments/assets/56d2af80-6b15-40a5-9207-7324063249a4)

