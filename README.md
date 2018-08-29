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

<a id="photo_user_info" />

## 🔎 User Information
If you want to get someone's user information, you should create a [User Instance](#user_instance), and use [Instance methods](#instance_method).

<a id="user_instance" />

### ✏️ User Instance

🔸 **`PyFlickr.getUser([user_id])`** - Get User instance

#### Parameters :

|    Name     | Type |    Description    | 
| ----------- | ---- | ----------------- |
| user_id     | str  | Find this parameter at someone's flickr url, like this :![user_id](https://upload.cc/i1/2018/08/28/sYzCIg.png)|

#### Example :

```python=3.6
user = PyFlickr.getUser(user_id="139958401@N06")
```

<a id="instance_method" />

### ✏️ Instance methods

Now, you get a **User instance** named **user**, and it has **6** methods : [getAbout](#get_about), [getPhotoStream](#get_photo_stream), [getAlbums](#get_albums), [getFaves](#get_faves), [getGalleries](#get_galleries), [getGroups](#get_groups).

<a id="get_about" />

#### 🔸 **`user.getAbout()`** - Get User about

#### Parameters : 
This method has no parameters.

#### Example : 
```python=3.6
user_about = user.getAbout()
```

#### Return Data : 
```json
{
  "title": "Syashin Chen",
  "subtitle": "PythonTest",
  "avatar": "https://s.yimg.com/pw/images/buddyicon01_r.png#139958401@N06",
  "followers": "3",
  "following": "3",
  "description": "For PyFlickr Test",
  "infos": {
    "Joined": "March 2016",
    "Hometown": "Tainan",
    "Current city": "Hsinchu",
    "Country": "Taiwan",
    "Website": "https://medium.com/@Syashin"
  },
  "general_stats": {
    "views": "518",
    "tags": "0",
    "map": "0",
    "favorites": "2",
    "groups": "2"
  },
  "showcase_photos": [
    "https://www.flickr.com/photos/139958401@N06/43371867585/",
    "https://www.flickr.com/photos/139958401@N06/43371866885/"
  ],
  "popular_photos": [
    "https://www.flickr.com/photos/139958401@N06/44277693001/",
    "https://www.flickr.com/photos/139958401@N06/44277691471/"
  ]
}
```

<a id="get_photo_stream" />

#### 🔸 **`user.getPhotoStream([limit_trigger],[limit_page])`** - Get User Photostream

#### Parameters : 

|      Name     |   Type   |   Description   | 
| ------------- | -------- |  -------------  |
| limit_trigger |   bool   |   It is uesd to set a limit to the returning pages through there are perhaps too many photos on **Photostream Page**. Default **limit_trigger = True** .   |
| limit_page    |   int    |   The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** .  |

#### Example : 

```python=3.6
# Return 1 page of PhotoStream Page.
user_photo_stream = user.getPhotoStream()

# Return 3 pages of PhotoStream Page.
user_photo_stream = user.getPhotoStream(limit_page = 3)

# Return all pages of PhotoStream Page.
user_photo_stream = user.getPhotoStream(limit_trigger = False)
```
#### Return Data : 
```json
{
  "Limit_Trigger": "False",
  "Limit_Page": "None",
  "Time_Spend": 19,
  "PhotoStream_Count": 26,
  "PhotoStream_Result": {
    "44277693001": "https://www.flickr.com/photos/139958401@N06/44277693001/",
    "43371871895": "https://www.flickr.com/photos/139958401@N06/43371871895/",
    "43371871115": "https://www.flickr.com/photos/139958401@N06/43371871115/",
    "44277691911": "https://www.flickr.com/photos/139958401@N06/44277691911/",
    "44277691471": "https://www.flickr.com/photos/139958401@N06/44277691471/",
    ...more
  }
}
```

<a id="get_albums" />

#### 🔸 **`user.getAlbums([limit_trigger],[limit_page])`** - Get User Albums

#### Parameters : 

|      Name     |   Type   |   Description   | 
| ------------- | -------- |  -------------  |
| limit_trigger |   bool   |   It is uesd to set a limit to the returning pages through there are perhaps too many albums on **Album Page**. Default **limit_trigger = True** .   |
| limit_page    |   int    |   The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** . |

#### Example : 

```python=3.6
# Return 1 page of Albums Page.
user_albums = user.getAlbums()

# Return 3 pages of Albums Page.
user_albums = user.getAlbums(limit_page = 3)

# Return all pages of Albums Page.
user_albums = user.getAlbums(limit_trigger = False)
```
#### Return Data : 
```json
{
  "Albums_Count": 2,
  "Albums_Result": {
    "72157670574464187": {
      "title": "Tainan_Taiwan",
      "url": "https://www.flickr.com/photos/139958401@N06/albums/72157670574464187"
    },
    "72157700310278564": {
      "title": "Travel_to_Japan",
      "url": "https://www.flickr.com/photos/139958401@N06/albums/72157700310278564"
    }
  },
  "Limit_Page": 1,
  "Limit_Trigger": "True",
  "Time_Spend": 21
}
```

<a id="get_faves" />

#### 🔸 **`user.getFaves([limit_trigger],[limit_page])`** - Get User Favorite Photos

#### Parameters : 

|      Name     |   Type   |   Description   | 
| ------------- | -------- |  -------------  |
| limit_trigger |   bool   |   It is uesd to set a limit to the returning pages through there are perhaps too many favorites photo on **Faves Page**. Default **limit_trigger = True** .   |
| limit_page    |   int    |   The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** . |

#### Example : 

```python=3.6
# Return 1 page of Faves Page.
user_favorites = user.getFaves()

# Return 3 pages of Faves Page.
user_favorites = user.getFaves(limit_page = 3)

# Return all pages of Faves Page.
user_favorites = user.getFaves(limit_trigger = False)
```
#### Return Data : 
```json
{
  "Faves_Count": 2,
  "Faves_Result": {
    "42447232940": "https://www.flickr.com/photos/bahnlandschaften/42447232940",
    "9480817678": "https://www.flickr.com/photos/othree/9480817678"
  },
  "Limit_Page": 1,
  "Limit_Trigger": "True",
  "Time_Spend": 19
}
```

<a id="get_galleries" />

#### 🔸 **`user.getGalleries([limit_trigger],[limit_page])`** - Get User Galleries

#### Parameters : 

|      Name     |   Type   |   Description   | 
| ------------- | -------- |  -------------  |
| limit_trigger |   bool   |   It is uesd to set a limit to the returning pages through there are perhaps too many Galleries on **Galleries Page**. Default **limit_trigger = True** .   |
| limit_page    |   int    |   The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** . |

#### Example : 

```python=3.6
# Return 1 page of Galleries Page.
user_galleries = user.getGalleries()

# Return 3 pages of Galleries Page.
user_galleries = user.getGalleries(limit_page = 3)

# Return all pages of Galleries Page.
user_galleries = user.getGalleries(limit_trigger = False)
```
#### Return Data : 
```json
{
  "Galleries_Count": 0,
  "Galleries_Result": {},
  "Limit_Page": "None",
  "Limit_Trigger": "False",
  "Time_Spend": 15
}
```

<a id="get_groups" />

#### 🔸 **`user.getGroups([limit_trigger],[limit_page])`** - Get User Groups

#### Parameters : 

|      Name     |   Type   |   Description   | 
| ------------- | -------- |  -------------  |
| limit_trigger |   bool   |   It is uesd to set a limit to the returning pages through there are perhaps too many Galleries on **Galleries Page**. Default **limit_trigger = True** .   |
| limit_page    |   int    |   The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** .  |

#### Example : 

```python=3.6
# Return 1 page of Groups Page.
user_groups = user.getGroups()

# Return 3 pages of Groups Page.
user_groups = user.getGroups(limit_page = 3)

# Return all pages of Groups Page.
user_groups = user.getGroups(limit_trigger = False)
```
#### Return Data : 
```json
{
  "Limit_Trigger": "True",
  "Limit_Page": 1,
  "Time_Spend": 16,
  "Groups_Count": 2,
  "Groups_Result": {
    "challengefactory": {
      "url": "https://www.flickr.com/groups/challengefactory/",
      "title": "工厂的挑战",
      "members": {
        "numbers": "5,596",
        "url": "https://www.flickr.com/groups/challengefactory/members"
      },
      "photos": {
        "numbers": "105,913",
        "url": "https://www.flickr.com/groups/challengefactory/pool"
      },
      "discuss": {
        "numbers": "145,829",
        "url": "https://www.flickr.com/groups/challengefactory/discuss"
      }
    },
    "35mmphotography": {
      "url": "https://www.flickr.com/groups/35mmphotography/",
      "title": "35mm - Photography",
      "members": {
        "numbers": "6,565",
        "url": "https://www.flickr.com/groups/35mmphotography/members"
      },
      "photos": {
        "numbers": "150,793",
        "url": "https://www.flickr.com/groups/35mmphotography/pool"
      },
      "discuss": {
        "numbers": "19",
        "url": "https://www.flickr.com/groups/35mmphotography/discuss"
      }
    }
  }
}
```

<a id="photo_size_info" />

## 🔎 Photo Size Information
If you want to get photo's every kind of sizes, you can create [Photo Instance](#photo_instance), and get [Instance Properties](#instance_properties). 

<a id="photo_instance" />

### ✏️ Photo Instance

#### 🔸 **`PyFlickr.getPhoto([photo_url])`** - Get Photo instance

#### Parameters :

|    Name     | Type |    Description    | 
| ----------- | ---- | ----------------- |
| photo_url   | str  | Photo url like: https://www.flickr.com/photos/139958401@N06/43371871895/ |

|  [photo_url] accept these kinds of url below:|
| -------- | 
| https://www.flickr.com/photos/139958401@N06/44277691471/ |
| https://www.flickr.com/photos/139958401@N06/44277691471/in/album-72157670574464187/  |
| https://www.flickr.com/photos/139958401@N06/44277691471/in/dateposted/ |
| https://www.flickr.com/photos/139958401@N06/44277691471/in/photostream/ |


#### Example :

```python=3.6
slide_page_url = "https://www.flickr.com/photos/139958401@N06/44277691471/" 

# Return Photo Instance
target_photo = PyFlickr.getPhoto(photo_url = slide_page_url)
```

<a id="instance_properties" />

### ✏️ Instance Properties
Now, you get a **Photo Instance** named **target_photo**, and it has **14** properties :

#### Properties :

|    Name     | Type | Usage |
| ----------- | ---- | ------- |
| title   | str  | ```target_photo.title```  |
| slide   | str  | ```target_photo.slide```|
| square_75   | str  | ```target_photo.square_75```| 
| square_150   | str  | ```target_photo.square_150```| 
| thumbnail   | str  | ```target_photo.thumbnail```|
| small_240   | str  | ```target_photo.small_240```|
| small_320   | str  | ```target_photo.small_320```|
| medium_500   | str  | ```target_photo.medium_500```|
| medium_640   | str  | ```target_photo.medium_640```|
| medium_800   | str  | ```target_photo.medium_800```|
| large_1024   | str  | ```target_photo.large_1024```|
| large_1600   | str  | ```target_photo.large_1600```|
| large_2048   | str  | ```target_photo.large_2048```|
| original   | str  | ```target_photo.original```|

#### Example :

```python=3.6
#Return title : 44277691471
title = target_photo.title 

#Return size page : https://www.flickr.com/photos/139958401@N06/44277691471/sizes/c
size_medium_800 = target_photo.medium_800

#Return size page : https://www.flickr.com/photos/139958401@N06/44277691471/sizes/o
size_original = target_photo.original
```

<a id="photo_direct" />

## 🔎 Photo Direct Url

You can get photo's direct url, just input size page url to [PyFlickr.getPhotoDirectUrl](#get_photo_direct_url) . 

<a id="get_photo_direct_url" />

### ✏️ PyFlickr.getPhotoDirectUrl

#### 🔸  **` PyFlickr.getPhotoDirectUrl([size_page_url])`**

#### Parameters :

|    Name     | Type |    Description    | 
| ----------- | ---- | ----------------- |
| size_page_url   | str  | Size page url like: https://www.flickr.com/photos/139958401@N06/44277691471/sizes/c |

#### Example :

```python=3.6
small_240_page = "https://www.flickr.com/photos/139958401@N06/44277691471/sizes/c/"

# Return https://c2.staticflickr.com/2/1896/43371871895_d1ab713987_m.jpg
target_photo_direct = PyFlickr.getPhotoDirectUrl(size_page_url = small_240_page)
```
## 🔎 Download Single Photo

**PyFlick** gives a class function to download single photo : [PyFlickr.singlePhoto_DL](#singlePhoto_DL)

<a id="singlePhoto_DL" />

### ✏️ PyFlickr.singlePhoto_DL
#### 🔸 **`PyFlickr.singlePhoto_DL([photo_url], [photo_name_to_save], [photo_size], [folder_path], [chunk_size])`**

#### Parameters :


|    Name     | Type |    Description    | 
| ----------- | ---- | ----------------- |
| photo_url   | str  | This photo_url is like: https://www.flickr.com/photos/139958401@N06/43371871895/  |
| photo_name_to_save   | str  | Name your photo to be downloaded. Default **photo_name_to_save is an empty string**, and it will save with id as name. |
| photo_size   | str  | Give a photo_size string from [Photo Instance Properties Name](#instance_properties). Default **photo_size = "medium_800"**|
| folder_path   | str  | Give a folder_path string to set where to save your photo. Default **folder_path is an empty string**, and your photo will be save locally.  |
| chunk_size   | int  | Set chunk_size of your download. Default **chunk_size = 512** |

#### Example :

```python=3.6
slide_url = "https://www.flickr.com/photos/139958401@N06/43371867585/"

# Download as 43371867585.jpg
PyFlickr.singlePhoto_DL(photo_url = slide_url)

# Download as A_new_photo.jpg and photo_size is small_320
PyFlickr.singlePhoto_DL(photo_url = slide_url, photo_name_to_save = "A_new_photo", photo_size = "small_320")

# Download as 43371867585.jpg in folder named FILE
PyFlickr.singlePhoto_DL(photo_url = slide_url, folder_path = "FILE")

```

## 🔎 Download Single Album

**PyFlick** provide a class function to download whole single Album : [PyFlickr.singleAlbum_DL](#singleAlbum_DL)

<a id="singleAlbum_DL" />

### ✏️ PyFlickr.singleAlbum_DL

#### 🔸 **`PyFlickr.singleAlbum_DL([album_url], [album_name_to_save], [album_photo_size], [folder_path], [limit_trigger], [limit_page], [chunk_size])`**

#### Parameters :

|    Name     | Type |    Description    | 
| ----------- | ---- | ----------------- |
| album_url   | str  | This album_url is like: https://www.flickr.com/photos/139958401@N06/albums/72157670574464187 |
| album_name_to_save   | str  | Name your album to be downloaded. Default **album_name_to_save is an empty string**, and it will save with original album name.  |
| album_photo_size   | str  | Give a photo_size string from [Photo Instance Properties Name](#instance_properties). Default **album_photo_size = "medium_800"**, and it will apply to all photos in that album. |
| folder_path   | str  | Give a folder_path string to set where to save your album. Default **folder_path is an empty string**, and your album will be save locally. |
| limit_trigger   | bool  | It is uesd to set a limit to the returning pages through there are perhaps too many photos in that album. Default **limit_trigger = True** .  |
| limit_page   | int  | The limit number of returning pages. Default **limit_page = 1**, and will be **invalid** when **limit_trigger = False** . |
| chunk_size   | int  | Set chunk_size of your download. Default **chunk_size = 512** |

#### Example :

```python=3.6
target_album = "https://www.flickr.com/photos/139958401@N06/albums/72157670574464187"

# Download whole albums as folder named Tainan_Taiwan
PyFlickr.singleAlbum_DL(album_url = target_album)

# Download whole albums with photo's size are "large_2048"
PyFlickr.singleAlbum_DL(album_url = target_album, album_photo_size = "large_2048")

# Download whole albums as folder named New_Album in other folder named ALBUM_FILE
PyFlickr.singleAlbum_DL(album_url = target_album, album_name_to_save = "New_Album", folder_path = "ALBUM_FILE")
```

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
