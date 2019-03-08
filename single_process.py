#/usr/bin/env python3

import time
from multiprocessing import Process

def io_task():
    time.sleep(1)

def main():
    start_time = time.time()
 
    # for i in range(5):
    #     io_task()

    process_list = []
    for i in range(5):
        process_list.append(Process(target=io_task))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    end_time = time.time()
    print('cheng xu yun xing hao shi : {:.2f}s'.format(end_time - start_time))

if __name__ == '__main__':
    main()