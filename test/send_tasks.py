# -*- coding:utf-8 -*-

from __future__ import absolute_import

from random import randint
from multiprocessing.pool import ThreadPool

from mycel.tasks import add


pool = ThreadPool(100)

if __name__ == '__main__':
    pool.map(add.apply_async, ((randint(0, 9), randint(0, 9)) for _ in range(10)))
