"""
Python hashlib 模块主要用于进行哈希（hash）操作。
哈希（Hash）是一种将任意长度的输入数据映射为固定长度输出数据的算法。
哈希通常用于验证数据的完整性、安全存储密码等场景。
哈希函数的输出通常是一串看似随机的字母和数字。
hashlib 模块提供了常见的哈希算法的实现，如 MD5、SHA-1、SHA-256 等。
"""

import hashlib


def hash_demo():
    """
    hash demo
    :return:
    """
    sha1_hash = hashlib.new(name="sha1")
    sha1_hash.update(b"Suoge@2023#OCP")
    print(sha1_hash.hexdigest())


if __name__ == '__main__':
    hash_demo()
