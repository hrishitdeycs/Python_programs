# WAP to read a file and
# (a) Print the total numbers of characters, words and lines in the file.
# (b) calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.
# (c) Print the words in reverse order.
# (d) Copy even lines of the file to a file named "file1" and odd lines to another file "file2".
```bash
#f=open("file2.txt",'w')
#f.write("Hello, my name is Hrishit Dey \n my course is bsc cs hons.")
#print("data updated")
#f.close()
def filehandling():
    f=open("file2.txt",'r')
    data=f.read()
    f.close()
    words=data.split()
    lines=len(data.splitlines())
    print("lines in text file is:",lines)
    print('Number of words in text file :',len(words))
    print("no of character in text file",len(data))
filehandling()
def freq():
    f=open("file2.txt",'r')
    data=f.read()
    f.close()
    d={}
    for i in data:
        b=data.count(i)
        d[i]=b
    print(d)
freq()
def reverse_words():
    f=open("file2.txt",'r')
    data1=f.read()
    data2=data1.split()
    reverse=data2[::-1]
    print("reversed words:"," ".join(reverse))
reverse_words()
def file1_and_file2():
    #f3=open("file3.txt",'x')
    #f4=open("file4.txt",'x')
    f=open("file2.txt",'r')
    f3=open("file3.txt",'w')
    f4=open("file4.txt",'w')
    lines=f.readlines()
    for i in range(len(lines)):
        if i%2==0:
            f3.write(lines[i])
        else:
            f4.write(lines[i])
    f.close()
    f3.close()
    f4.close()
    file5=open("file3.txt", 'r')
    file6=open("file4.txt","r")
    print("even lines : ",file5.read())
    print("odd lines: ",file6.read())
    file5.close()
    file6.close()
file1_and_file2()
```
![Screenshot (31)](https://github.com/user-attachments/assets/20ac8c21-406b-411c-ab35-029b28b2d653)

