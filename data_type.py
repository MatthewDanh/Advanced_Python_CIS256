"""
Matthew Nichols
Module 04 Programming Assignment
Part B

This Python script demonstrates the use of stack and queue data structures by reading names
from a text file, performing various operations (push and pop), and printing the results.
It uses a stack to store and retrieve names in a last-in, first-out (LIFO) manner, and a queue
 to handle names in a first-in, first-out (FIFO) manner.
"""
from collections import deque

try:
    with open('G:/My Drive/Academic/cis256/03module/names.txt', 'r', encoding='utf-8') as file:
        pass
except FileNotFoundError as e:
    print(f"File not found error occurred: {e}")
except IOError as e:
    print(f"IO error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Create an empty stack and push the name "J.R.R. Tolkien" in as the first ("bottom") element.
stack = []
stack.append("J.R.R. Tolkien")

# Read the text file and push each name onto the stack.
with open('names.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stack.append(line.strip())

# Print the contents of your stack
print(stack)

# One at a time, pop and output the three top names from the stack
for _ in range(3):
    print(stack.pop())

# Push your own name into the stack
stack.append("Matthew Nichols")

# Print the contents of the stack
print(stack)

# Create a queue using the deque class
queue = deque()

# Push the name of a fictional character into the queue
queue.append("Fictional Character")

# One at a time, push the names from the text file into your queue
with open('names.txt', 'r', encoding='utf-8') as file:
    for line in file:
        queue.append(line.strip())

# Print the contents of the queue
print(list(queue))

# One at time, pop and print the five oldest names in the queue
for _ in range(5):
    print(queue.popleft())

# Push the name of a school teacher you liked into the "back" of the queue
queue.append("Favorite Teacher")

# Push the name of a favorite actor or musical artist into the "back" of the queue
queue.append("Favorite Actor/Musician")

# Print the contents of the queue
print(list(queue))
"""
References:
1. Python Official Documentation: https://docs.python.org/3/
2. Python File I/O: https://www.w3schools.com/python/python_file_handling.asp
3. Python deque: https://docs.python.org/3/library/collections.html#collections.deque
4. Stack Overflow - Reading and writing files in Python: https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
5. Stack Overflow - How does a Python deque work?: https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists
"""
