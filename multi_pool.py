#!/usr/bin/env python3
import os,time,random
from multiprocessing import Pool

def task(name):
    print('ren wu {} qi dong yun xing , jing cheng ID:{}'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('ren wu {} jie shu yun xing , hao shi :{:.2f}s'.format(name,(end-start)))

if __name__ == '__main__':
        print('dang qian wei zhu jing cheng , jing cheng ID:{}'.format(os.getpid()))    
        print('---------------------------------------------')

        p = Pool(4)

        for i in range(1,6):
            p.apply_async(task,args=(i,))

        p.close()

        print('kai shi yun xing zi jing cheng...')
        
        p.join()
        print('---------------------------------------------')
        print('suo you zi jing cheng yun xing wan bi , dang qian wei zhu jing cheng , jing cheng ID:{}'.format(os.getpid()))