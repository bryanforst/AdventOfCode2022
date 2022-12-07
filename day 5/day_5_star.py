"""Main Module"""
from collections import deque
import re

ship_stack  = []
ship_stack.append( deque(['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N']))
ship_stack.append( deque(['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G']))
ship_stack.append( deque(['L', 'Q', 'V']))
ship_stack.append( deque(['N', 'B', 'S', 'W', 'R', 'Q']))
ship_stack.append( deque(['N', 'D', 'F', 'T', 'V', 'M', 'B']))
ship_stack.append( deque(['M', 'D', 'B', 'V', 'H', 'T', 'R']))
ship_stack.append( deque(['D', 'B', 'Q', 'J']))
ship_stack.append( deque(['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q']))
ship_stack.append( deque(['B', 'N', 'H', 'M', 'S']))


with open("input.txt", encoding="utf-8") as inputFile:
    while True:
        line = inputFile.readline()
        if not line:
            break

        instructions = re.findall(r'\w+',line.strip())

        iterate_count = int(instructions[1])
        from_stack = int(instructions[3])-1
        to_stack = int(instructions[5])-1

        temp = []
        for _ in range(iterate_count):
            temp.append(ship_stack[from_stack].pop())

        temp.reverse()
        ship_stack[to_stack].extend(temp)

for queue in ship_stack:
    print(queue.pop(), end="")