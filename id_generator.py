from random import choice

def id_gen():
    id = ''
    while len(id) != 6:
        all_items = ('0', '1', '2', '3', '4', '5', '6', '8', '9',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
        item = choice(all_items)
        id += item
    return id







