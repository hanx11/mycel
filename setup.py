# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from setuptools import setup

version = "0.0.1"

packages = ["mycel"]

packages = [package.encode('ascii') for package in packages]

setup(
    name="mycel",
    version=version,
    author="HanFeng",
    author_email="hanx11@163.com",
    url="",
    classifiers=[],
    zip_safe=False,
    packages=packages,
    install_requires=[
        "celery==4.0.2",
    ]
)
