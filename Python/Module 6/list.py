employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees[1]+"is a great employee!")


fav_colors=['Vlue', 'Red', 'Green', 'Pink']
print(fav_colors[1], fav_colors[3])


fav_colors=['Vlue', 'Red', 'Green', 'Pink']
print(type(fav_colors[2]))

#Module 6
employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
employees[0]='Mark'
print(employees)

#Operators can be used to make modifications to lists
employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
employees = employees + ['Jim']
print(employees)



#the + p[erators can be used to concatenate two or more lists together.
fav_nums=['16', '24', '7', '100']
fav_colors=['Blue', 'Red', 'Green', 'Pink']
print(fav_nums+fav_colors)


employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
employees.insert(1, "Dave")
print(employees)

employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
del employees[2]
print(employees)

employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
employees.remove('Carrie')
print(employees)


#Foor loop
employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
for x in employees:
    print(x)


#To determine if a specified item is present in a list use the in keyword
employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
if "Tammy" in employees:
    print("Yes, Tammy does work here")

#To determine how many items a list has, use the len() method
employees = ['Sara', 'Tammy', 'Debbie','John', 'Carrie']
print(employees)
print(len(employees))

#1
nums=['1', '2', '3', '4', '5']
print(nums)

nums[3]='10'
print(nums)

#2
nums=['1', '2', '3', '4', '5']
print(nums)

del nums[2]
print(nums)


#3
nums=['1', '2', '3', '4']
print(nums)

nums.insert(2, '25')
print(nums)

