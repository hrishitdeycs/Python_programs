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
a= input("enter first string :")
b= input("enter second string :")
occurances(a,b)
