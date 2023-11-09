import sys

try:
    while True:
        a, b = map(int, input().split())
        print(a+b)
except:
    sys.stdin.readline()