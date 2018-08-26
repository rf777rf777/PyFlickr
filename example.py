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
#user3_galleries = user3.getGalleries(limit_trigger = False)
#writeResultFile("Galleries", user3_galleries)
#pprint(user_galleries)

#Get user "Groups" Page
#user_groups = user.getGroups()
#writeResultFile("Groups", user_groups)

#user5_groups = user5.getGroups()
#writeResultFile("Groups", user5_groups)


PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371869065/sizes/c/")
PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371867585/in/dateposted-public/")
PyFlickr.singlePhoto_DL("https://www.flickr.com/photos/139958401@N06/43371866885/in/album-72157670574464187/")

#Download single Album
PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/139958401@N06/albums/72157670574464187", limit_trigger=False)

PyFlickr.singleAlbum_DL(album_url="https://www.flickr.com/photos/kulagg/albums/72157628010221485", album_name_to_save="new", limit_trigger=False)

















