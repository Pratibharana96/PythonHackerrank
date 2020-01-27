#vPython programming language allows to use one loop inside another loop.
# Following section shows few examples to illustrate the concept.
# Syntax:
#1) Continue Statement:
When the program encounters continue statement, it will skip the statements
which are present after the continue statement inside the loop and proceed with the next iterations.
example ::
1 for char in ‘Python’:
2
      if (char == ‘y’):
3
           continue
4
      print(“Current character: “, char)

Output:

Current character: P

Current character: t

Current character: h

Current character: o

Current character: n

#2) Break Statement:
The break statement is used to terminate the loop containing it, the control of the program will come out of that loop.

example::
1  for char in ‘Python’:
2
       if (char == ‘h’):
3
           break
4
       print(“Current character: “, char)
Output:

Current character: P

Current character: y

Current character: t


#3) Pass Statement:
Pass statement is python is a null operation, which is used when the statement is required syntactically.

1 for char in ‘Python’:
2
       if (char == ‘h’):
3
           pass
4
print(“Current character: “, char)

OUTPUT:
Output:

Current character: P

Current character: y

Current character: t

Current character: h

Current character: o

Current character: n
