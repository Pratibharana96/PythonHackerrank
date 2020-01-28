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

*****************************************************adding items and deleting item in array********************************************
import array as arr
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
# changing first element
numbers[0] = 0    
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

#append() in arary and extend () used to add severalitems in the array
numbers.append(3)
print(numbers)

#extend()
numbers.extend([5,6,8])
print(numbers)

#We can concatenate two arrays using + operator.
odd= arr.array('i',[1,3,4])
even= arr.array('i',[2,4,6])

number = arr.array('i') #creating empty array of integer
number = odd + even
print(number)


#How to remove/delete elements?
#We can delete one or more items from an array using Python's del
#statement.

del(number[3])
print(number)


#remove() method to remove the given item, and pop()
number.remove(1)
print(number)

print(number.pop(3))
print(number)
