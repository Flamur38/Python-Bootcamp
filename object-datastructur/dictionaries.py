# Dictionaries can't be sorted like list. We can call dict by their values

# Constructing a Dictionary
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key2'])

my_dict = {'key1':123, 'key2':[12,23,34], 'key3':['item0', 'item1']} # Diffrent Values
print(my_dict['key3'][1].upper()) # ITEM1 

  
# We can effect the values of a key
print(my_dict['key1']) # 123
my_dict['key1'] -= 123
print(my_dict['key1']) # 0

d = {}
d['animals'] = 'Dog'
d['answer'] = 42
print(d) # {'animals': 'Dog', 'answer': 42}


d = {'key1':1, 'key2':2, 'key3':3} # Create a typical dictionary
print(d.keys()) # dict_keys(['key1', 'key2', 'key3'])
print(d.values()) # dict_values([1, 2, 3])
print(d.items())  # dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

print('---')

price_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}
print(price_lookup['apple']) # 2.99

