"""
Task
Given two numbers, print in the first line the integer result of the division
and in the second line the full result of the division

"""

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

div = a / b
div_int = int(div)

print(div_int)
print(div)