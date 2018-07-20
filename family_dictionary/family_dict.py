my_family = {
    'sis': {
        'name': 'Olivia',
        'age': 20
    },
    'mum': {
        'name': 'Sheila',
        'age': 54
    },
    'husband': {
        'name': 'Zach',
        'age': 31
    },
    'bro': {
        'name': 'Keith',
        'age': 29
    }
}

family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

# print(family_stuff)

family_stuff = set()
for family_member, member_values in my_family.items():
        family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old')
print("My family!", family_stuff)
# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

#With comprehension instead
family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}
print("My family!", family_stuff)