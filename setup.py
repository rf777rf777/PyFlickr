# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='PyFlickr',
    version='1.0.0',
    keywords='flickr',
    packages=find_packages(),
    license='MIT License',
    description='PyFlickr - Unofficial Flickr SDK',
    author='SyashinChen',
    author_email='rf777rf777@gmail.com',
    url='https://github.com/rf777rf777/PyFlickr',
    python_requires='>=3',
)