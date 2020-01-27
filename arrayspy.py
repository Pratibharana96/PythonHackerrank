#Array in Python can be created by importing array module. array(data_type, value_list) 
#is used to create an array with data type and value list specified in its arguments.

example 1:
import array as arr
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])


#How to slice arrays?
#We can access a range of items in an array by using the slicing operator :.

import array as arr
#slicing in python
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end
