# **PyFlickr - An Unofficial Flickr API**

![PyFlickr](https://raw.githubusercontent.com/rf777rf777/PyFlickr/master/content/Banner.jpg)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  [![PyPI version](https://badge.fury.io/py/PyFlickr.svg)](https://badge.fury.io/py/PyFlickr)


**PyFlickr** provides python-developers to access to user, albums, photos and other public information from [**Flickr**](
https://www.flickr.com/) website in read-only mode. This API also provides some easy ways to download public photos and albums. You can customize these to fit your requirements.

<a id="setup" />

# **📕 Setup**
To install PyFlickr, simply use pip:
```shell
$ pip install PyFlickr
```
Then, before using, you have to download **[Chromedriver](http://chromedriver.chromium.org/downloads)** to **driver** folder and **unzip** it.

```shell
$ mkdir driver
$ cd driver
$ curl -O https://chromedriver.storage.googleapis.com/{VERSION}/chromedriver_{OS}.zip
$ unzip chromedriver_{OS}.zip
```

Remember to update`{VERSION}`with the latest version and`{OS}`with your computer OS.

For example:
```shell
# version 2.41 on Mac
$ curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_mac64.zip
```
```shell
# version 2.41 on Windows
$ curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip
```

# **📗 Getting Start**

Start by importing module - **PyFlickr**:



```python
from pyflickr import PyFlickr
```
# **📘 Documentation**

**PyFlickr** provides **5** features **:** **[User Information](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%94-User-Information)**, **[Photo Size Information](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%95-Photo-Size-Information)**, **[Photo Direct Url](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%97-Photo-Direct-Url)**, **[Download Single Photo](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%98-Download-Single-Photo)**, **[Download Single Album](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%99-Download-Single-Album)**.

### ❗️ For more details, please see **[PyFlickr Guide](https://github.com/rf777rf777/PyFlickr/wiki)** .

#### Example :
```python
# This example shows : Download all of albums of one user in a new folder named "ResultFolder"

from pyflickr import PyFlickr

user = PyFlickr.getUser('139958401@N06')
result = user.getAlbums(limit_trigger = False)
albums = result['Albums_Result']
for album_data in albums:
	album_url = album_data['url']
	PyFlickr.singleAlbum_DL(album_url = album_url, folder_path='ResultFolder')
```

# 📙 Development

It's simple to run PyFlickr on your computer.
Follow instruction below step-by-step:

```shell
$ git clone https://github.com/rf777rf777/PyFlickr.git
$ cd PyFlickr
$ pip install -r requirements.txt
```
Then, as mentioned previously, please setup your **[Chromedriver](http://chromedriver.chromium.org/downloads)** (see [Setup](https://github.com/rf777rf777/PyFlickr/wiki/%F0%9F%93%92-Setup)).

# 📝 License

Licensed under [MIT license](http://opensource.org/licenses/MIT).

