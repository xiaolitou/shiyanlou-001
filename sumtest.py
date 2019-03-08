#!/usr/bin/env python3

num = {0:['a'],1:['b'],2:['c']}
tishi = {0:'first',1:'second',2:'third'}
_counter = 0
_sum = 0

while _counter <= 2:
    
    tmp = input('Please enter the {} num: '.format(tishi[_counter]))
    if tmp.isdigit():
    	
    	num[_counter].append(int(tmp))
    	_counter += 1



for i in num:

	_sum += num[i][1]

print('a is {}, b is {}, c is {}, a+b+c = {}'.format(num[0][1],num[1][1],num[2][1],_sum))