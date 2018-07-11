zootuples = ('zebra', 'elephant', 'flamingo', 'camel', 'polar bear')

print(zootuples.index('flamingo'))

for value in zootuples:

    if not zootuples.animal('flamingo'):
        filtered_zootuples.append('flamingo')
        print(filtered_zootuples)
