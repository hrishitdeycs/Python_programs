def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):    
  if y==0:
      return "cannot be divided"
  else:
       return x/y
def floordivision(x,y):
    if y==0:
      return "cannot be divided"
    else:
      return x // y
def remainder(x,y):
    if y==0:
      return "cannot be divided"
    else:
      return x % y
print("Operations :")
print("Add :  + ")
print("Subtract :  - ")
print("Multiplication :  * ")
print("Division :  / ")
print("Remainder :  % ")
print("Floor Division :  // ")
try:
     a = eval(input("enter number : "))
     c = input("enter operation ")
     b = eval(input("enter number : "))
     result =0;
     if(c== "+"):
          sum = add(a,b)
          result = sum
          print("result :",sum)
     elif(c=='-'):
          sub = subtract(a,b)
          result = sub
          print("result :",sub)
     elif(c== '*'):
         mul = multiply(a,b)
         result = mul
         print("result :",mul)
     elif(c== '/'):
         div = divide(a,b)
         result = div
         print("result :",div)
     else:
           print("InValid operation")
     while(True):
          d = input("enter operation : ")
          if(d == '+'):
               e = eval(input("enter number : "))
               sum2 = add(result,e)
               result = sum2
               print("result :",sum2)
          elif(d == '-'):
               e = eval(input("enter number : "))
               sub2 = subtract(result,e)
               result = sub2
               print("result :",sub2)
          elif(d == '*'):
               e = eval(input("enter number : "))
               mul2 = multiply(result,e)
               result = mul2
               print("result :",mul2)
          elif(d == '/'):
              e = eval(input("enter number : "))
              div2 = divide(result,e)
              result = div2
              print("result :",div)
          elif(d == '='):
              print(result)
              break
          else:
              print("wrong operation")
except:
     print("wrong enteries")
