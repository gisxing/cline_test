import threading
import time

# 线程任务函数
def worker(num):
    print(f'线程 {num} 开始运行')
    time.sleep(2)
    print(f'线程 {num} 结束运行')

# 创建5个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print('所有线程执行完毕')