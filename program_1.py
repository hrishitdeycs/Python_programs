a,b,c = eval(input("enter value "))
d = b ** 2 - 4 * a * c
r1 = (-b + (d) ** 0.5) / 2 * a
r2 = (-b - (d) ** 0.5) / 2 * a
if d >=0:
    print("roots are real ",r1,r2)
else:
    print("roots are not real",r1,r2)
