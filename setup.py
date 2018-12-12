from setuptools import setup, find_packages
from os import path

this_path = path.abspath(path.dirname(__file__))

with open(path.join(this_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ctci',
    version='0.1.0',
    description='Cracking the Coding Interview 6th Ed. Solutions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='rm21845',
    author_email='rmdavis@buffalo.edu',
    classifiers= [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='algorithms coding interviews',
    packages=find_packages(exclude=['docs']),
    project_urls={
        'Bug Reports': 'https://github.com/rm21845/ctci/issues',
        'Source': 'https://github.com/rm21845/ctci',
    },
)