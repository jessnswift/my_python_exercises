planet_list = ['Mercury', 'Mars']
planet_list.append('Jupiter')
planet_list.append('Saturn')
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
planet_list.append('Pluto')

rocky_planets = planet_list[:4]
print(rocky_planets)

# del planet_list[len(planet_list) -1]
del planet_list[-1]
print(planet_list)

# if 'Pluto' in planet_list:
#     print('Pluto is not a planet')
# else:
#     print('You are correct')

spacecraft_tuple = [('Cassini', 'Saturn'), ('Deep Space 2', 'Mars'),
    ('Mariner 10', 'Mercury'), ('Pioneer 11', 'Jupiter'),
    ('Voyager 2', 'Uranus'), ('Voyager 2', 'Neptune'),
    ('Mariner 2', 'Venus'), ('Aliens', 'Earth'),
    ('New Horizons', 'PLuto')]

def spacecraft():
    for planet in planet_list:
        for tupleItem in spacecraft_tuple:
            if tupleItem[1] == planet:
                print(f'{tupleItem[0]} has landed on {planet}!')

print(spacecraft())