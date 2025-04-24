
# NESTING LISTS
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [list_1,list_2,list_3]
print(matrix)

# Grab first item in matrix
print(matrix[0]) # [1,2,3]

# Grab first item of the first item in the matrix object
print(matrix[0][0]) # 1

# List Comprehensions
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix] 
print(first_col) # [1, 4, 7]


