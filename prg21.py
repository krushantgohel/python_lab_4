# Write a program to create dictionary emp=[id,name,designation,salary]and delete designation key,update name.f

emp = {
    'id': 101,
    'name': 'Het Agravat',
    'designation': 'Software Engineer',
    'salary': 75000
}

print("Original dictionary:", emp)

del emp['designation']

emp['name'] = 'Agravat Het'


print("Updated dictionary:", emp)