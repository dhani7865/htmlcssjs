txt = input("Can you see this? Yes or No")
print("You said ", txt)

name = input("What is your name")
print("My name Is ", name)

txt = input("Give me a number")
num = int(txt)
print("The number you gave is:", num)

txt = input("Give me a number")
print("The number you gave is:", num)


txt = input("Give me a number please: ")

try:
    num = int(txt)
    print("The number you gave is: ", num)
except ValueError:
        print("Please put in a real number, not a string or text")


salary = 44000
txt = "You make () dollars a year"
print(txt.format(salary))


string = "Dave teaches() ()"
print(string.format("cyber", "security"))

#Substitutions
string = "David loves {} {}. and has {} {} "
print(string.format("cyber", "security", 14, "certifications"))

string = "David loves {1} {3}, and has {2} {0}"
print(string.format("siblings", "cyber", 7, "security"))

string = "Bob likes to play {act} and eat {1} {0}"
print(string.format("dogs", "hot", act="games"))

print("Bob likes to play {act} and eat {1} {0}".format("dogs", "hot", act="games"))

