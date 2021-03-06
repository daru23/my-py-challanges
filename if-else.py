"""
Task
Given an integer, n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
"""

n = int(raw_input())

if n % 2:
    print("Weird")
elif n % 2 & 2 <= n <= 5:
    print("Not Weird")
elif n % 2 & 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
