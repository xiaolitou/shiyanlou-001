#!/usr/bin/env python3
from multiprocessing import Process,Queue

queue = Queue()

def f1(q):
	i = 'Hello shiyanglou'
	q.put(i)
	print('Send Data:{}'.format(i))

def f2(q):
	data = q.get()
	print('Receive Data: {}'.format(data))

def main():
	Process(target=f1,args=(queue,)).start()
	Process(target=f2,args=(queue,)).start()

if __name__ == '__main__':
	main()