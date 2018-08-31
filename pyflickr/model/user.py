#from about import About
import re
from pyflickr.constant.constant import *
from pyflickr.model.enum import PageEnum, PeopleEnum, PhotosEnum
from pyflickr.model.about import About
import time
class User:
	def __init__(self, user_id):
		self.user_id = user_id

	def getAbout(self):
		
		#Determine "About page" url
		url = "{0}/{1}/{2}/".format(ROOT_URL, PageEnum.People.value, self.user_id)
		
		#Get requests result from url
		result = getRequestsResult(url)

		#Create "About" class
		about = About()

		#Get title
		title = firstOrDefault(result.select('div.title h1'))
		about.title = title.text.strip() if title is not None else "None"
		
		#Get subtitle
		subtitle = firstOrDefault(result.select('div p.subtitle.no-shrink.truncate'))
		about.subtitle = subtitle.text.strip() if subtitle is not None else "None"

		#Get avatar url
		avatar_url = firstOrDefault(result.select('.avatar.no-menu.person.large'))
		if avatar_url is not None:
			avatar_url = avatar_url['style'].replace(' ','')
			if HTTPS_TITLE in avatar_url:
				avatar_url = avatar_url.split("(")[-1][:-2]
			else:
				avatar_url = avatar_url.split(";")[-2].split(":")[-1][4:-1]
				avatar_url = "{0}{1}".format(HTTPS_TITLE, avatar_url)
		else:
			avatar_url = "None"
		about.avatar = avatar_url

		#Get followers & following
		followers = firstOrDefault(result.select('p.followers.truncate.no-shrink'))
		#re.findall(r"\d+\.?\d*",followers.text)
		about.followers = re.findall(r"\d+\.?\d*K?M?G?T?", followers.text.strip().split('•')[0])[0] if followers is not None else "None"
		about.following = re.findall(r"\d+\.?\d*K?M?G?T?", followers.text.strip().split('•')[1])[0] if followers is not None else "None"

		#Get description
		description = firstOrDefault(result.select('.description.expanded'))
		about.description = description.text.strip().replace(u'\xa0', u' ') if description is not None else "None"

		#Get info
		infoDict = {}
		infos = result.select('.infos-view-container ul li')
		for info in infos:
			infoTitle = info.span.text
			infoValue = info.text.replace(infoTitle, '')

			infoTitle = info_english_title(infoTitle)
			infoDict[infoTitle] = infoValue
		about.infos = infoDict
		
		#Get general
		generalDict = {}
		general_stats = result.select('.general-stats ul li')
		for general in general_stats:
			if general_stats.index(general) == 0:
				title = "views"
			elif general_stats.index(general) == 4:
				title = general.a.get('href').split('/')[-2]
			else:
				title = general.a.get('href').split('/')[-1]
			generalDict[title] = general.span.text
		about.general_stats = generalDict
		
		#Get showcase photos
		showcase_photos = result.select('.showcase .view.photo-list-photo-view.awake')
		showcase_photoList = []
		for photo in showcase_photos:
			if len(showcase_photos) != 0:
				#https://c1.staticflickr.com/5/4412/36764461820_309f2d5038_n.jpg
				photo_id = photo['style'].replace(' ','').split(";")[-1].split(":")[-1][4:-1].split('_')[0].split('/')[-1]
				photo_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id, photo_id)
				#photo_url = "{0}{1}".format(HTTPS_TITLE, photo_url_after)
				showcase_photoList.append(photo_url)
		about.showcase_photos = showcase_photoList

		#Get popular photos
		popular_photos = result.select('.popular-container .view.photo-list-photo-view.awake')
		hot_photoList = []
		for photo in popular_photos:
			if len(popular_photos) != 0:
				#photo_url_after = photo['style'].replace(' ','').split(";")[-1].split(":")[-1][4:-1]
				photo_id = photo['style'].replace(' ','').split(";")[-1].split(":")[-1][4:-1].split('_')[0].split('/')[-1]
				photo_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id, photo_id)
				#photo_url = "{0}{1}".format(HTTPS_TITLE, photo_url_after)
				hot_photoList.append(photo_url)
		about.popular_photos = hot_photoList

		return to_dict(about)

	def getPhotoStream(self, limit_trigger = True, limit_page = 1):
		
		#Start Time
		startTime = time.time()

		#Determine "PhotoStream page" url
		photoStream_url = "{0}/{1}/{2}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id)
		
		#Get Seleinum Result from photoStream_url
		driver = getSeleinumResult(photoStream_url)
		
		#Determine max page
		paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
		pageMax = getPageMax(paginationArea, limit_trigger, limit_page)

		#Create photo list
		photoUrlList = []

		#Now page number
		pageNumber = 1
		
		#Photo counter
		photoCounter = 0

		while True:

			#Get photo elements on page
			elements = driver.find_elements_by_css_selector('.overlay')
 			
			#total = len(elements)	

			#Get photo url
			for elem in elements:
				photo_url = elem.get_attribute('href')
				photo_id = photo_url.split('/')[-2]
				photoUrlList.append(photo_url)
				photoCounter += 1

			#Check if Now page number achieve page max number 
			if pageNumber >= pageMax:
				break
			else:
				pageNumber += 1
				#Determine next page url
				next_url = "{0}page{1}".format(photoStream_url.rstrip('\n'), pageNumber)

				#Get Seleinum Result from next photoStream_url
				driver = getSeleinumResult(next_url)
				#time.sleep(1)

		#End Time
		endTime = time.time()

		#Create result dict
		resultDict = {}
		resultDict['Limit_Trigger'] = "{0}".format(limit_trigger)
		resultDict['Limit_Page'] = limit_page if limit_trigger else "None"
		resultDict['Time_Spend'] = round(endTime - startTime)
		resultDict['PhotoStream_Count'] = photoCounter
		resultDict['PhotoStream_Result'] = photoUrlList

		return resultDict

	def getAlbums(self, limit_trigger = True, limit_page = 1):
		
		#Start Time
		startTime = time.time()	
		
		#Determine "Albums page" url
		albums_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id, PhotosEnum.Albums.value)

		#Get Seleinum Result from albums_url
		driver = getSeleinumResult(albums_url)
		
		#Determine max page
		paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')	
		pageMax = getPageMax(paginationArea, limit_trigger, limit_page)
		
		#Create albums list
		albumsUrlList = []
		
		#Now page number
		pageNumber = 1

		#Album Counter
		albumCounter = 0

		while True:

			#Get albums elements on page
			elements = driver.find_elements_by_css_selector('.overlay')
			
			#Get albums url
			for elem in elements:
				album_data = {}

				album_url = elem.get_attribute('href')				
				album_id = album_url.split('/')[-1]			
				album_title = elem.find_element_by_xpath("..").find_element_by_xpath("..").get_attribute('title').replace('/','_').replace(',','_').replace(' ','_')

				album_data["title"] = album_title
				album_data["url"] = album_url
				albumsUrlList.append(album_data)
				albumCounter += 1
			
			#Check if Now page number achieve page max number 
			if pageNumber >= pageMax:
				break
			else:
				pageNumber += 1
				#Determine next page url
				next_url = "{0}page{1}".format(albums_url.rstrip('\n'), pageNumber)
				
				#Get Seleinum Result from next albums_url
				driver = getSeleinumResult(next_url)
				#time.sleep(1)

		#End Time
		endTime = time.time()

		#Create result dict
		resultDict = {}
		resultDict['Limit_Trigger'] = "{0}".format(limit_trigger)
		resultDict['Limit_Page'] = limit_page if limit_trigger else "None"
		resultDict['Time_Spend'] = round(endTime - startTime)
		resultDict['Albums_Count'] = albumCounter
		resultDict['Albums_Result'] = albumsUrlList

		return resultDict

	def getFaves(self, limit_trigger = True, limit_page = 1):

		#Start Time
		startTime = time.time()	
		
		#Determine "Faves page" url
		faves_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id, PhotosEnum.Favorites.value)

		#Get Seleinum Result from faves_url
		driver = getSeleinumResult(faves_url)

		#Determine max page
		paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
		pageMax = getPageMax(paginationArea, limit_trigger, limit_page)

		#Create photo list	
		photoUrlList = []

		#Now page number
		pageNumber = 1

		#Fave Counter
		faveCounter = 0

		while True:

			#Get favorite photo elements on page
			elements = driver.find_elements_by_css_selector('.overlay')

			#Get favorite photo url
			for elem in elements:
 				fave_url = elem.get_attribute('href')
 				photo_url = '/'.join(fave_url.split('/')[:-3])
 				photo_id = fave_url.split('/')[-4]
 				photoUrlList.append(photo_url)
 				faveCounter += 1
			
			#Check if Now page number achieve page max number 
			if pageNumber >= pageMax:
				break
			else:
				pageNumber += 1
				#Determine next page url
				next_url = "{0}page{1}".format(faves_url.rstrip('\n'), pageNumber)
				
				#Get Seleinum Result from next faves_url
				driver = getSeleinumResult(next_url)
				#time.sleep(1)

		#End Time
		endTime = time.time()

		#Create result dict
		resultDict = {}
		resultDict['Limit_Trigger'] = "{0}".format(limit_trigger)
		resultDict['Limit_Page'] = limit_page if limit_trigger else "None"
		resultDict['Time_Spend'] = round(endTime - startTime)
		resultDict['Faves_Count'] = faveCounter
		resultDict['Faves_Result'] = photoUrlList

		return resultDict
		
	def getGalleries(self, limit_trigger = True, limit_page = 1):
	
		#Start Time
		startTime = time.time()

		#Determine "Galleries page" url
		galleries_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.Photo.value, self.user_id, PhotosEnum.Galleries.value)

		#Get Seleinum Result from galleries_url
		driver = getSeleinumResult(galleries_url)

		#Determine max page
		paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
		pageMax = getPageMax(paginationArea, limit_trigger, limit_page)

		#Create gallery list	
		galleryUrlList = []
		
		#Now page number
		pageNumber = 1

		#Gallery Counter
		galleryCounter = 0

		while True:

			#Get gallery elements on page
			elements = driver.find_elements_by_css_selector('.Seta')
			
			#Get gallery data
			for elem in elements:

				gallery_data = {}

				gallery_url = elem.get_attribute('href')
				gallery_id = gallery_url.split('/')[-2]
				gallery_title = elem.get_attribute('title')

				gallery_data['url'] = gallery_url
				gallery_data['title'] = gallery_title

				galleryUrlList.append(gallery_data)
				galleryCounter += 1

			#Check if Now page number achieve page max number 
			if pageNumber >= pageMax:
				break
			else:
				pageNumber += 1
				#Determine next page url
				next_url = "{0}page{1}".format(galleries_url.rstrip('\n'), pageNumber)
				
				#Get Seleinum Result from next galleries_url
				driver = getSeleinumResult(next_url)
				#time.sleep(1)

		#End Time
		endTime = time.time()

		#Create result dict
		resultDict = {}
		resultDict['Limit_Trigger'] = "{0}".format(limit_trigger)
		resultDict['Limit_Page'] = limit_page if limit_trigger else "None"
		resultDict['Time_Spend'] = round(endTime - startTime)
		resultDict['Galleries_Count'] = galleryCounter
		resultDict['Galleries_Result'] = galleryUrlList

		return resultDict				

	def getGroups(self, limit_trigger = True, limit_page = 1):

		#Start Time
		startTime = time.time()
		
		#Determine "Groups page" url
		groups_url = "{0}/{1}/{2}/{3}/".format(ROOT_URL, PageEnum.People.value, self.user_id, PeopleEnum.Groups.value)
		
		#Get Seleinum Result from groups_url
		driver = getSeleinumResult(groups_url)

		#Determine max page
		paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
		pageMax = getPageMax(paginationArea, limit_trigger, limit_page)
		
		#Create group list	
		groupList = []
		
		#Now page number
		pageNumber = 1
		
		#Group Counter
		GroupCounter = 0

		while True:

			#Get gallery elements on page
			elements = driver.find_elements_by_css_selector('tbody tr')[1:]
			
			#Get group data
			for elem in elements:

				group_data = {}				
				content = elem.find_elements_by_css_selector('td a')
				
				group_id = content[0].get_attribute('href').split('/')[-2]

				group_data['url'] = content[0].get_attribute('href')
				group_data['title'] = content[0].text
				group_data['members'] = {'numbers': content[1].text, 'url': content[1].get_attribute('href')} 
				group_data['photos'] = {'numbers': content[2].text, 'url': content[2].get_attribute('href')}
				group_data['discuss'] = {'numbers': content[4].text, 'url': content[4].get_attribute('href')} 

				groupList.append(group_data)
				GroupCounter += 1

			#Check if Now page number achieve page max number 
			if pageNumber >= pageMax:
				break
			else:
				pageNumber += 1
				#Determine next page url
				next_url = "{0}page{1}".format(groups_url.rstrip('\n'), pageNumber)
				
				#Get Seleinum Result from next groups_url
				driver = getSeleinumResult(next_url)
				#time.sleep(1)

		#End Time
		endTime = time.time()
		
		#Create result dict
		resultDict = {}
		resultDict['Limit_Trigger'] = "{0}".format(limit_trigger)
		resultDict['Limit_Page'] = limit_page if limit_trigger else "None"
		resultDict['Time_Spend'] = round(endTime - startTime)
		resultDict['Groups_Count'] = GroupCounter
		resultDict['Groups_Result'] = groupList

		return resultDict

def info_english_title(title):
	zh_TW_dict = { "已加入": "Joined", "出生地": "Hometown", "目前所在城市": "Current city", '國家/地區': "Country", "網站": "Website"}
	value = zh_TW_dict.get(title)
	return title if value is None else value

#Parse class to dict
def to_dict(class_model):
	return dict((get_key(key), value)
				for key, value in class_model.__dict__.items()
				if not callable(value) and not key.startswith("__"))

#Standardize key
def get_key(key):
	return key.replace("_", "", 1) if key.startswith("_") else key

