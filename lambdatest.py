#!/usr/bin/env python3

list1 = [('Shi',100), ('Yan', 75), ('Lou', 200), ('Plus', 80)]

# sortedlist = sorted(list1, key=TODO)
sortedlist = sorted(list1,key=lambda i: i[1])

print(sortedlist)