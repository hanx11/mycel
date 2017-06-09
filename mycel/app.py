# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from celery import Celery
from .config import BROKER_URL, CELERY_RESULT_BACKEND

app = Celery('mycel', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND, include=['mycel.tasks'])

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='asia/shanghai',
    enable_utc=True,
)

if __name__ == '__main__':
    app.start()
