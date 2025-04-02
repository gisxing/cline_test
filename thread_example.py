"""
Python多线程示例
English: Python Threading Example

功能说明:
1. 创建5个并发线程
2. 每个线程执行2秒任务
3. 主线程等待所有子线程完成
4. 演示基本线程创建和管理

Function Description:
1. Create 5 concurrent threads
2. Each thread executes a 2-second task
3. Main thread waits for all child threads
4. Demonstrates basic thread creation and management
"""

import threading
import time

# 线程任务函数/Thread worker function
def worker(num):
    """
    线程工作函数
    English: Thread worker function
    
    :param num: 线程编号/Thread number
    """
    print(f'线程 {num} 开始运行/Thread {num} started')
    time.sleep(2)  # 模拟工作负载/Simulate workload
    print(f'线程 {num} 结束运行/Thread {num} finished')

# 主程序/Main program
if __name__ == '__main__':
    threads = []
    
    # 创建5个线程/Create 5 threads
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成/Wait for all threads to complete
    for t in threads:
        t.join()
    
    print('所有线程执行完毕/All threads completed')