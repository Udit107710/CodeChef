import calendar
from sys import stdin

for _ in range(int(stdin.readline())):
    m1, y1 = map(int, stdin.readline().split())
    m2, y2 = map(int, stdin.readline().split())

    if y2 > y1:
        for i in range(y1, y2+1):
            pass