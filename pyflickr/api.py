import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from pyflickr.constant.constant import *
from pyflickr.model.user import User
from pyflickr.model.photo import Photo

import re
import os

class PyFlickr:

	#Get user data
	@staticmethod
	def getUser(user_id):
		return User(user_id)
	
	#Get user data
	@staticmethod
	def getPhotoLink(photo_url):
		return Photo(photo_url)

	#Download single photo
	@staticmethod
	def singlePhoto_DL(photo_url, photo_name='', photo_size='medium_800', folderPath='', chunk_size= 512):
		try:
			#Handle if size page
			keyword = 'sizes'	
			if keyword in photo_url:
				sizes = photo_url.split('/')[-2] if photo_url.endswith('/') else photo_url.split('/')[-1]
				sizes_value = '{0}/{1}'.format(keyword, sizes)
				photo_size_key = FirstOrDefault([key for key, value in PHOTO_SIZE.items() if value == sizes_value])
				if photo_size_key is not None:
					photo_size = photo_size_key

			#Standardize photo url
			if len(photo_url.split('/')) >= 6:
				photo_url = '/'.join(photo_url.split('/')[:6])
				if photo_url[-1] != '/':
					photo_url += '/'

			#Determine target folder
			if not len(folderPath) == 0:
				folderPath = createFolder(folderPath)

			#Determine photo name
			photo_fullname = photo_name
			if len(photo_fullname) == 0:
				photo_fullname = "{0}.jpg".format(photo_url.split('/')[-2])
			else:
				if not photo_fullname.endswith('.jpg'):
					photo_fullname = "{0}.jpg".format(photo_fullname)

			#Determine photo save path
			photo_savePath = "{0}{1}".format(folderPath, photo_fullname)

			#Determine photo size url
			photo_size_url = "{0}{1}".format(photo_url, PHOTO_SIZE[photo_size])

			#Find photo direct url
			soup = GetRequestsResult(photo_size_url)
			photo_direct_url = FirstOrDefault(soup.select('#allsizes-photo img'))['src']
		
		except:
			if photo_size not in PHOTO_SIZE.keys():
				errorMessage = "<Error> Please enter correct photo_size <Error>"
			else:
				errorMessage = "<Error> Please enter correct photo url <Error>"

			print("\n{0}\n{1}\n{0}".format('='*len(errorMessage), errorMessage))

			return			

		#Get Photo Stream
		dl_request = requests.get(photo_direct_url, stream = True)
		with open(photo_savePath, 'wb') as f:
			#complete = 0
			#PyFlickrDL.completeInTerminal(complete,fileSize)
			for chunk in dl_request.iter_content(chunk_size):
				if 	chunk:
					f.write(chunk)
					#complete+=1
					#PyFlickrDL.completeInTerminal(complete,fileSize)
			f.close()
	
	#Download single album
	@staticmethod
	def singleAlbum_DL(album_url, album_name='', album_photo_size='medium_800', driverUri='./phantomjs', folderPath='', upperlimit = False, pagelimit = 5, chunk_size=512):
		try:	
			#Standardize album url
			if len(album_url.split('/')) >= 7:
				album_url = '/'.join(album_url.split('/')[:7])
				if not album_url.endswith('/'):
					album_url = "{0}/".format(album_url)

			#Get SeleinumResult
			driver = GetSeleinumResult(album_url)

			#Determine max page
			paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
			pageMax = getPageMax(paginationArea, upperlimit, pagelimit)
			#print(pageMax)
			
			#Get & Parse album title
			album_title = FirstOrDefault(driver.find_elements_by_css_selector('.album-title')).text.replace('/','_').replace(',','_').replace(' ','_')

			#Determine target folder
			if len(album_name) == 0:
				album_name = album_title
			if not len(folderPath) == 0:
				if not folderPath.endswith('/'):
					folderPath = "{0}/".format(folderPath)
				folderPath = "{0}{1}".format(folderPath, album_name)
			else:
				folderPath = album_name			
			folderPath = createFolder(folderPath)

		except:
			errorMessage = "<Error> Please enter correct album url <Error>"
			print("\n{0}\n{1}\n{0}".format('='*len(errorMessage), errorMessage))
			return

		count = 0
		pageNumber = 1

		while True:
			elements = driver.find_elements_by_css_selector('.overlay')
			for elem in elements:			
				slide_url = elem.get_attribute('href')

				#Standardize photo url
				if len(slide_url.split('/')) >= 6:
					slide_url = '/'.join(slide_url.split('/')[:6])
					if slide_url[-1] != '/':
						slide_url += '/'

				#Determine photo name
				photo_fullname = ''
				photo_fullname = "{0}.jpg".format(slide_url.split('/')[-2])

				#Determine photo save path
				photo_savePath = '{0}{1}'.format(folderPath, photo_fullname) 

				#Determine photo size url
				photo_url = "{0}{1}".format(slide_url, PHOTO_SIZE[album_photo_size])

				#Find photo direct url
				soup = GetRequestsResult(photo_url)
				photo_direct_url = soup.select('#allsizes-photo img')[0]['src']

				#Get Photo Stream
				dl_request = requests.get(photo_direct_url, stream = True)
				with open(photo_savePath, 'wb') as f:
					#complete = 0
					#PyFlickrDL.completeInTerminal(complete,fileSize)
					for chunk in dl_request.iter_content(chunk_size):
						if 	chunk:
							f.write(chunk)
							#complete+=1
							#PyFlickrDL.completeInTerminal(complete,fileSize)
					f.close()
				count += 1			
			if pageNumber >= pageMax: #or pageNumber >= pagelimit:
				break
			else:
				pageNumber += 1
				newUrl = "{0}page{1}".format(album_url.rstrip('\n'), pageNumber)
				driver = GetSeleinumResult(newUrl)

#Create folder
def createFolder(folderPath):
	if not os.path.exists(folderPath):
		os.makedirs(folderPath)
	if not folderPath.endswith('/'):
		folderPath = "{0}/".format(folderPath)
	return folderPath


