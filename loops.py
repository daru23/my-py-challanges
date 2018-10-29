"""
Task
Read an integer n. For all non-negative integers i < n, print i^2. See the sample for details.

Input Format

The first and only line contains the integer, n.

Constraints
1 <= n <= 20

Output Format

Print n lines, one corresponding to each i.

Sample Input 0

5

Sample Output 0

0
1
4
9
16
"""

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i * i)