# create a tuple named zoo
zoo = ('zebra', 'elephant', 'flamingo', 'camel', 'polarbear')

# find animal using index
print(zoo.index('flamingo'))

# determine if animal is in tuple
animal = []

def find(animal):
    for value in zoo:
        if animal in zoo:
            print(f'{animal} is currently at the Zoo.')
        else:
            print(f'{animal} is not at the Zoo.')

find('flamingo')
find('lion')

# create variable for each animal
(zebra, elephant, flamingo, camel, polarbear) = zoo
print(elephant)

# convert tuple to list
zoo_list = list(zoo)
print(zoo_list)

# use extend to add 3 animals
zoo_list.extend(['kitty', 'cardinal', 'dolphin'])
print(zoo_list)

# convert list back to tuple
print(tuple(zoo_list))