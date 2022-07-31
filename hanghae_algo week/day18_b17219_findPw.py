# https://www.acmicpc.net/problem/17219

import sys
from pprint import pprint

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

dct = dict()

for i in range(n):
    site, pw = input().split()
    dct[site] = pw
# pprint(dct)

for i in range(m):
    site = input()
    print(dct[site])