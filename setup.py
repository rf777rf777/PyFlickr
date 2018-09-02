# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open
from os import path

this_directory = path.abspath(path.dirname(__file__)) 
def read_file(filename): 
    with open(path.join(this_directory, filename), encoding='utf-8') as f: 
        long_description = f.read()
        return long_description

setup(
    name='PyFlickr',
    version='1.0.0',
    keywords=['PyFlickr','flickr'],
    packages=['pyflickr','pyflickr.constant','pyflickr.model'],
    install_requires=['requests','beautifulsoup4','selenium'],
    license='MIT License',
    long_description=read_file('README.rst'),
    long_description_content_type="text/markdown", 
    description='PyFlickr - Unofficial Flickr API',
    author='SyashinChen',
    author_email='rf777rf777@gmail.com',
    url='https://github.com/rf777rf777/PyFlickr',
    python_requires='>=3.5',
)