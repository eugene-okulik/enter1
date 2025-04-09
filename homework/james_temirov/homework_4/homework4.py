my_dict = {
    'tuple':(1, 2, 3, 4, 5),
    'list': [45, 657, 243, 6456, 7567, 'food', True, 'kitty' ],
    'dict': {'name': 'James', 'last_name': 'Temirov', 'age': 30, 'state': 'NC', 'city': 'Charlotte', 'car': 'VW'},
    'set': {100, 200, 300, 400, 500, 600, 700}
}

print(my_dict['tuple'] [-1])

my_dict['list'].append('Adding last item')
my_dict['list'].pop(1)

my_dict['dict'] [('i am a tuple', )] = 'i hope its correct' # В примере вы специально оставили запятую? я вложил картеж в словарь получается?
my_dict['dict'].pop('state')

my_dict['set'].add(800)
my_dict['set'].remove(200)

print(my_dict)