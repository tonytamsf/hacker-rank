#!/usr/bin/env python3 

print('''This will take an array and reverse it by
swaping items in place.
''');
def reverse(s):
    for i in range (0, int(len(s) / 2)):
        tmp = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = tmp
    return s

print (reverse ([400,300,200,100]))
