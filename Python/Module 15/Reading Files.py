a = open("demo.txt", "r")
print(a.read())

#fileobject = open(file_name [access_model])
a = open("demo.txt", "r")
print(a.read())
a.close()

a = open("demo.txt", "r")
print(a.read(7))
a.close()


myFile = open("demo.txt", "r")
contents = myFile.read()
print(contents)

#Writing Files
a = open("demo.txt", "a")
a.write("\n Here is another line in our text file")
a.close()

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)


#Remember, the access mode is pretty important.
a = open("demo.txt", "w")
a.write("What has happened now?")

