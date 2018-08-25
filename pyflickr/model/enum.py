from enum import Enum

class PageEnum(Enum):
	People = "people"
	Photo = "photos"

class PeopleEnum(Enum):
	Groups = "groups"

class PhotosEnum(Enum):
	Albums = "albums"
	Favorites = "favorites"
	Galleries = "galleries"	

class PhotoSizeEnum(Enum):
	square_75 = "sizes/sq"
	square_150 = "sizes/q"
	thumbnail = "sizes/t"
	small_240 = "sizes/s"
	small_320 = "sizes/n"
	medium_500 = "sizes/m"
	medium_640 = "sizes/z"
	medium_800 = "sizes/c"
	large_1024 = "sizes/l"
	large_1600 = "sizes/h"
	large_2048 = "sizes/k"
	original = "sizes/o"
