songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Elton John', 'Tiny Dancer'),
    ('Britney Spears', 'Hit Me Baby, One More Time')
}

# for s in songs:
#     if s[0] != 'Nickelback':
#         print(s)

kill_nickelback = {s for s in songs if s[0] != 'Nickelback'}
print(kill_nickelback)