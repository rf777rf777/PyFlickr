# **PyFlickr - An Unofficial Flickr API**

![PyFlickr](https://raw.githubusercontent.com/rf777rf777/PyFlickr/master/content/Banner.jpg)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


**PyFlickr** provides python-developers to access to user, albums, photos and other public information from [**Flickr**](
https://www.flickr.com/) website. You can customize these to fit your requirements. This API also provide an easy way to download public photos and albums. 

# **📕 Installation**
 ~~To install PyFlickr, simply use pip:~~ **not available yet**
```shell
$ pip install PyFlickr
```
Then, before using, you have to download **[Chromedriver](http://chromedriver.chromium.org/downloads)** to **driver** folder and **unzip** it.

```shell
$ mkdir driver | cd driver
$ curl -O https://chromedriver.storage.googleapis.com/{VERSION}/chromedriver_{OS}.zip
$ unzip chromedriver_{OS}.zip
```

Remember to update`{VERSION}`with the latest version and`{OS}`with your computer OS.

For example:
```shell
# version **2.41** on **Mac**
$ curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_mac64.zip
```
```shell
# version **2.41** on **Windows**
$ curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip
```

# **📗 Usage**

Start by importing module - **PyFlickr**:

```python=3.6
from pyflickr import PyFlickr
```
# **📘 Documentation**

**PyFlickr** provides **5** features **:** **[User Information](#photo_user_info)**, **[Photo Size Information](#photo_size_info)**, **[Photo Direct Url](#photo_direct)**, **[Download Single Photo](#)**, **[Download Single Album](#)**.


# 📙 Development

It's simple to run PyFlickr on your computer.
Follow instruction below step-by-step:

```shell
$ git clone https://github.com/rf777rf777/PyFlickr.git
$ cd PyFlickr
$ pip install -r requirements.txt
```
Then, before using, you have to download **[Chromedriver](http://chromedriver.chromium.org/downloads)** to **driver** folder and **unzip** it.

```shell
$ mkdir driver | cd driver
$ curl -O https://chromedriver.storage.googleapis.com/{VERSION}/chromedriver_{OS}.zip
$ unzip chromedriver_{OS}.zip
```
Remember to update`{VERSION}`with the latest version and`{OS}`with your computer OS.

# 📝 License

MIT
