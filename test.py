#!/usr/bin/env python3

filename = input('Enter the file name: ')

with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('Line: {}'.format(count))

with open(filename,'w') as file:
    file.write('testline1\n')
    file.write('testline2')