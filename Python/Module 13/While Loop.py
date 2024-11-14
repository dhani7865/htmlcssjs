#With the while loop we can execute a set of statements as long as a condition is true.

a=1
print(a)
a+=1

x="Heello World"
y=1
y+=1

#While loop
a=1
while a < 6:
    print(a)
    a+=1

    x="Heello World"
    y=1
    while y <= 3:
        print(x)
        y += 1
        print("End of second loop")


#With the "Continue" statement we can stop the current iteration, and contine with the next
#This should sop at 4, even though we have 14 as the high end for the loop
        x=0
        while x < 6:
            x += 1
            if x == 4:
                continue
            print(x)

a=1
while a <= 3:
    print("Great Job")
    a += 1

    x=1
    while x < 10:
        print(x)
        if x == 6:
            break
        x += 1
