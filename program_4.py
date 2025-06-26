character = input("enter data ")
if character >='A ' and character<='Z':
    print("uppercase letter")
elif character >='a' and character<='z':
    print("lowercase letter")
elif character >='0' and character<='9':
    print("numeric digit")
    n = int(character)
    dict = 
{0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eig
ht',9:'nine'}
    print(dict[n])
else:
    print("special character")
