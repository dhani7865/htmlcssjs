#Practise Answer 1
import shutil
import os

src = "demo.txt"
dst = "16Demo.txt"

shutil.copy(src, dst)

os.rename("16Demo.txt", "LeaveMeAlone.txt")

x = open("LeaveMeAlone.txt", "r")
print(x.read())
x.close()


#Practise answer 2
#import shutil
import os

x = open("MyNewFile.txt", "x")
x.close()

x = open("MyNewFile.txt", "a")

x.write("Here is line 1\n")
x.write("Here is line 2\n")
x.close()

src = "MyNewFile.txt"
dst = "DavesDemo.txt"

shutil.copy(src, dst)

x = open("DavesDemo.txt", "a")
b = 1
while b < 4:
    x.write("Time for new line " + str(b)+"\n")
    b+= 1
    x.close()

    first = open("MyNewFile.txt", "r")
    print(first.read())
    first.close()

    second = open("DavesDemo.txt", "r")
    print(second.read())
    second.close()
