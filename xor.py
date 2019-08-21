#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def xor(l, n):
    maps = Counter(l)
    c = 0
    for i in maps.keys():
        if maps[i]>1:
            c+=maps[i]*(maps[i]-1)//2
    return c
        
    


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    result = xor(l, n)
    print(result)