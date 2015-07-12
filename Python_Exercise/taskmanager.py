#!/usr/bin/env python
#encoding --utf-8

import random,time,Queue
from multiprocessing.managers import BaseManager

task_queue =Queue.Queue()
result_queue=Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',lambda:task_queue)
QueueManager.register('get_result_queue',lambda:result_queue)
manager=QueueManager(address=('',5000),authkey='abc')
manager.start()
task=manager.get_task_queue()
result=manager.get_result_queue()
for i in range(10):
    n=random.randint(0,10000)
    print 'put task %d...'%n
    task.put(n)
print 'Try to get results...'
for i in range(10):
    r=result.get(timeout=10)
    print 'Result:%s'%r
manager.shutdown()
