#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='dhub',
      version='0.1',
      keywords=('dhub', 'Data Hub'),
      description='dhub提供了数据存储功能，用于存储大批量数据，如音乐',
      long_description='See http://github.com/yeelink-python-sdk',
      license='MIT License',

      url='http://liluo.github.com/douban-client',
      author='smallmuou',
      author_email='lvyexuwenfa100@126.com',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=[
          'flask',
          'flask_restful'
      ],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],)
