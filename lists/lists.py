# Indexing and Slicing

my_list = ['one', 'two', 'three', 4, 5]

# Grab element at index 0
print(my_list[0]) 
 
# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything UP TO index 3
print(my_list[:3])

# ======================

list1 = [1,2,3]

# Pop off the 0 indexed item
print(list1.pop(0))

#=====================

new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)

# Use reverse to reverse order (this is permanent!)
print(new_list.reverse())

print(new_list.sort())
#==========================

# NESTING LISTS
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [list_1,list_2,list_3]
print(matrix)
# Grab first item in matrix
print(matrix[0])

# Grab first item of the first item in the matrix object
print(matrix[0][0])



