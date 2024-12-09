my_dict = {
    'tuple': (1, 2, 3, 'four', 'five'),
    'list': [1, 2, 3, 'four', 'five'],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 'four', 'five'}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('new')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'new'
my_dict['dict'].pop('b')
my_dict['set'].add(777)
my_dict['set'].remove(777)
print(my_dict)
