# Indexing and Slicing
my_list = ['one', 'two', 'three', 4, 5]

# Grab element at index 0
print(my_list[0]) # one
 
# Grab index 1 and everything past it
print(my_list[1:]) # ['two', 'three, 4, 5]

# Grab everything UP TO index 3
print(my_list[:3]) # ['one', 'two', 'three']

# ======================

list1 = [1,2,3]

# Pop off the 0 indexed item
print(list1.pop(0)) # 1

#=====================

new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)

# Use reverse to reverse order (this is permanent!)
print(new_list.reverse())

print(new_list.sort())
