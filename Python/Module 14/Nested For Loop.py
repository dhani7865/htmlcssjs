#Module 14
#Nested for loop
outer = ['outer1', 'outer2', 'outer3']
nest = ['nest1', 'nest2', 'nest3']

for x in outer:
    for y in nest:
        print(x, y)
# numbers
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for x in numbers:
    print(x)
    for y in letters:
        print(y)

#Nested for loop with the outer loop
leads = ['Mark', 'Bob', 'Sara']

departments = ['IT', 'Public Relations', 'Human Resources', 'Sales', 'Administration']

for x in leads:
    print(x)

    for y in departments:
        print(y)
    print("\n")
