# -*- coding:utf-8 -*-

BROKER_URL = 'amqp://Aaron:Aaron123456@45.62.106.31//'

CELERY_RESULT_BACKEND = 'amqp://Aaron:Aaron123456@45.62.106.31//'

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'
