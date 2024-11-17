
# Wap to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.
```bash
name = input("enter a name ")
try:
    if name.isalpha():
        print("This is correct Name")
    else:
        raise Exception(" There is NameError")
except Exception as e: 
    print(e)
```
![Screenshot (16)](https://github.com/user-attachments/assets/1550ee06-91d2-4650-9b4a-ad0a57652a13)

![Screenshot (17)](https://github.com/user-attachments/assets/f31130c2-75a2-4fe7-824b-8c90bd015c42)
