from pyflickr import PyFlickr
from pprint import pprint

def writeResultFile(title, result):
	with open("{0}.txt".format(title), 'w', encoding="utf-8") as f:
		f.write('{0}'.format(result))

		f.close()

user = PyFlickr.getUser("139958401@N06")
user1 = PyFlickr.getUser("128746471@N05")
user2 = PyFlickr.getUser("toosakasora")
user3 = PyFlickr.getUser("othree")
user4 = PyFlickr.getUser("kulagg")
user5 = PyFlickr.getUser("wingmanzero")

#Get user "About" Page
#user_about = user.getAbout()
#print(user_about)
#writeResultFile("About", user_about)
#user1_about = user1.getAbout()
#writeResultFile("About", user1_about)

#Get user "PhotoStream" Page
#user_photo_stream = user.getPhotoStream(limit_trigger = False)
#writeResultFile("PhotoStream", user_photo_stream)
#pprint(user_photo_stream)
#user1_photo_stream = user1.getPhotoStream()
#writeResultFile("PhotoStream", user1_photo_stream)

#Get user "Albums" Page
#user_album = user.getAlbums()
#writeResultFile("Albums", user_album)
#pprint(user_album)
#user1_album = user1.getAlbums()
#writeResultFile("Albums", user1_album)
#user2_album = user2.getAlbums(limit_trigger = False)
#writeResultFile("Albums", user2_album)

#Get user "Fave" Page
#user_faves = user.getFaves()
#writeResultFile("Faves", user_faves)
#pprint(user_faves)
#user1_faves = user1.getFaves()
#writeResultFile("Faves", user1_faves)
#user2_faves = user2.getFaves(limit_trigger = False)
#writeResultFile("Faves", user2_faves)

#Get user "Galleries" Page
#user_galleries = user.getGalleries(limit_trigger = False)
#writeResultFile("Galleries", user3_galleries)
#pprint(user_galleries)

#Get user "Groups" Page
#user_groups = user.getGroups()
#writeResultFile("Groups", user_groups)

#user5_groups = user5.getGroups()
#writeResultFile("Groups", user5_groups)

# Return 1 page of Groups Page.
#user_groups = user.getGroups()
#print(user_groups)
# Return 3 pages of Groups Page.
#user_groups = user.getGroups(limit_page = 3)
#print(user_groups)
# Return all pages of Groups Page.
#user_groups = user.getGroups(limit_trigger = False)
#print(user_groups)

'''
PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371869065/sizes/c/")
PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371867585/in/dateposted-public/")
PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371866885/in/album-72157670574464187/")

#Download single Album
#PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/139958401@N06/albums/72157670574464187", limit_trigger=False)

#PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/kulagg/albums/72157628010221485", album_name_to_save="new", limit_trigger=False)

#PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/55570664@N02/albums/72157662134683704", limit_trigger=False)

PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/55570664@N02/albums/72157668666673901", limit_trigger=False)

photo_size = PyFlickr.getPhotoSizePage("https://www.flickr.com/photos/139958401@N06/43371871895/in/dateposted-public/")

url = photo_size.medium_800

#direct_url = PyFlickr.getPhotoDirectUrl("https://www.flickr.com/photos/139958401@N06/43371866885/in/album-72157670574464187/")
direct_url = PyFlickr.getPhotoDirectUrl(url)

print(direct_url)
'''
'''
url = "https://www.flickr.com/photos/139958401@N06/44277691471/sizes/c"
dir_url = PyFlickr.getPhotoDirectUrl(url)
print(dir_url)
'''

#PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371867585/")

#PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371867585/", photo_name_to_save="A_new_photo", photo_size="small_320")

#PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371867585/", folder_path="NewFolder")

'''
target_album = "https://www.flickr.com/photos/139958401@N06/albums/72157670574464187"

PyFlickr.singleAlbum_DL(album_url = target_album)

PyFlickr.singleAlbum_DL(album_url = target_album, album_photo_size = "large_2048")

PyFlickr.singleAlbum_DL(album_url = target_album, album_name_to_save = "New_Album", folder_path = "ALBUM_FILE")
'''
from pyflickr import PyFlickr

user = PyFlickr.getUser('139958401@N06')

result = user.getAlbums(limit_trigger = False)

albums = result['Albums_Result']

for album_data in albums:
	album_url = album_data['url']
	PyFlickr.singleAlbum_DL(album_url = album_url, folder_path='ResultFolder')


#result = user.getGroups(limit_trigger = False)
#print(result)


