"""
@Project: python-service
@File: log.py
@Author: David
@Date: 2025/5/27
@Brief: python 数据结构队列示例
"""
import queue


def queue_demo():
    """
    队列示例, 先进先出
    :return:
    """
    # 创建一个队列
    q = queue.Queue()

    # 向队列中添加元素
    q.put(1)
    q.put(2)

    # 从队列中取出元素, 如果队列为空, 会阻塞
    print(q.get())
    print(q.get())


def lifo_queue_demo():
    """
    lifo_queue 队列示例, 后进先出, 类似于栈
    :return:
    """
    q = queue.LifoQueue()

    q.put(1)
    q.put(2)

    print(q.get())
    print(q.get())


def priority_queue_demo():
    """
    优先级队列示例, 优先级越高, 越先被取出, 数值越小, 优先级越高
    :return:
    """
    q = queue.PriorityQueue(maxsize=10)

    q.put((3, "Low priority"))
    q.put((1, "High priority"))
    q.put((2, "Medium priority"))

    while not q.empty():
        print(q.get()[1])


def queue_function():
    """
    队列通用函数
    :return:
    """
    q = queue.Queue(maxsize=3)

    # 队列是否为空
    print(q.empty())

    q.put(1)
    q.put(2)
    q.put(3)

    # 队列长度
    print(q.qsize())

    # 队列是否已满
    print(q.full())


if __name__ == '__main__':
    queue_function()
