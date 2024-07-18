my_dict = {'Alex': 1900, 'Bogdan': 1905, 'Clod': 1910}
print(my_dict)
print(my_dict.get('Bogdan'))
print(my_dict.get('Nina'))
my_dict.update({'Nasti': 1950,
                'Tati': 1980})
print(my_dict)
my_dict.pop('Alex')
print(my_dict)

my_set = {1, 1, 1, 11, 2, 22, 2, 'gnom', 'grot', 'grot', (0.35, 0.36, 0.36)}
print(my_set)
print(my_set.update({666, '+WWW'}))
print(my_set)
print(my_set.discard(1))
print(my_set)