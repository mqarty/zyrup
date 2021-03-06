#!/usr/bin/env python2.7
"""
zyrup package
"""

import glob
from setuptools import setup, find_packages

setup(name="zyrup",
      version='1.0.0',
      description='Zuora Python Library',
      author='Marty Berryman',
      author_email='me@mqarty.com',
      url='https://github.com/mqarty/zyrup',
      zip_safe=False,
      install_requires=[
          'suds ==0.3.9',
          'requests ==1.2.3',
          'gevent ==1.0.1',
      ],
      data_files=[('config/zyrup', glob.glob('conf/zyrup/*'))],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      tests_require=['nose', 'mock'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Topic :: System :: Zuora',
    ]
)
