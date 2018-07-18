# My Showroom and Junkyard

# create and empty set named showroom
showroom()

# add 4 cars
showroom = {'mini cooper', 'prius', 'vw bug', 'vw van'}
print(len(showroom))

# add one car again
showroom.add('prius')

# using update(), add 2 more cars
showroom.update(['space ship', 'tesla'])

# remove 1 car with discard()
showroom.discard('space ship')

print(showroom)
print(len(showroom))

# create set named junkyard
junkyard = {'clown car', 'truck', 'mini van',
    'mini cooper', 'tesla', 'vw bug', 'prius'}

# using intersection, combine showroom and junkyard
print(junkyard.intersection(showroom))

# use union method to join
showroom = showroom.union(junkyard)
print(showroom)

# use discard to remove cars
showroom.discard('clown car')
showroom.discard('mini cooper')

print(showroom)
