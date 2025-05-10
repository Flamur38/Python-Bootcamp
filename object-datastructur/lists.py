# Indexing and Slicing
from typing import NewType

my_list = ['one', 'two', 'three', 4, 5]

# Grab element at index 0
print(my_list[0]) # one
 
# Grab index 1 and everything past it
print(my_list[1:]) # ['two', 'three, 4, 5]

# Grab everything UP TO index 3
print(my_list[:3]) # ['one', 'two', 'three']

# ======================
list1 = [1,2,3]

# add items at the end of the lists
print(list1.append(4)) 
print(list1) # [1,2,3,4]

# Pop off the 0 indexed item ( the pop() function can remove items from a list)
print(list1.pop(0)) # 1
print(list1)

#=====================

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,5,9] 

# sort items on a list
print(new_list.sort())
print(new_list)

# Use reverse to reverse order (this is permanent!)
print(new_list.reverse())
print(new_list)
