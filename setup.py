import codecs
import os
import sys
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    return read("./README.md")

VERSION = "0.0.1"

setup(
    name='remote_auth',
    version=VERSION,
    description='Provide multiple Django Auth support to a project',
    long_description=readme().strip(),
    author='mymusise',
    author_email='mymusise1@gmail.com',
    url='https://github.com/mymusise/django-view-limiter',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='remote multi default django auth',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    include_package_data=True,
    package_data={
        '': ['.README.md']
    },
    zip_safe=False,
)