#!/usr/bin/env python
#   Copyright 2017 Alex Krzos
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='collectd-rabbitmq-monitoring',
    version='0.0.3',
    description='Collectd plugin for Rabbitmq.',
    long_description=read('README.rst'),
    url='https://github.com/akrzos/collectd-rabbitmq-monitoring',
    author='Alex Krzos',
    author_email='akrzos@redhat.com',
    packages=[
        'collectd_rabbitmq_monitoring',
    ],
    install_requires=[
        'pyrabbit'
    ],
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License ',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
)
