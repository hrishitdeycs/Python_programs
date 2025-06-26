name = input("enter a name ")
try:
    if name.isalpha():
        print("This is correct Name")
    else:
        raise Exception(" There is NameError")
except Exception as e: 
    print(e)
