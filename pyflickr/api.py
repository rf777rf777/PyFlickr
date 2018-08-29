import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pyflickr.constant.constant import *
from pyflickr.model.user import User
from pyflickr.model.photo import Photo
import os

class PyFlickr:

	#Get user data
	@staticmethod
	def getUser(user_id):
		return User(user_id)
	
	#Get photo size page
	@staticmethod
	def getPhoto(photo_url):
		return Photo(photo_url)

	#Get photo direct url from size page
	@staticmethod
	def getPhotoDirectUrl(size_page_url):
		#Find photo direct url
		soup = getRequestsResult(size_page_url)
		photo_element = firstOrDefault(soup.select('#allsizes-photo img'))
		photo_direct_url = photo_element['src'] if photo_element is not None else "None"
		return photo_direct_url

	#Download single photo
	@staticmethod
	def singlePhoto_DL(photo_url, photo_name_to_save='', photo_size='medium_800', folder_path='', chunk_size= 512):
		try:
			#Handle if size page
			keyword = 'sizes'	
			if keyword in photo_url:
				sizes = photo_url.split('/')[-2] if photo_url.endswith('/') else photo_url.split('/')[-1]
				sizes_value = '{0}/{1}'.format(keyword, sizes)
				photo_size_key = firstOrDefault([key for key, value in PHOTO_SIZE.items() if value == sizes_value])
				if photo_size_key is not None:
					photo_size = photo_size_key

			#Standardize photo url
			if len(photo_url.split('/')) >= 6:
				photo_url = '/'.join(photo_url.split('/')[:6])
				if photo_url[-1] != '/':
					photo_url += '/'

			#Determine target folder
			if not len(folder_path) == 0:
				folder_path = createFolder(folder_path)

			#Determine photo name
			photo_fullname = photo_name_to_save
			if len(photo_fullname) == 0:
				photo_fullname = "{0}.jpg".format(photo_url.split('/')[-2])
			else:
				if not photo_fullname.endswith('.jpg'):
					photo_fullname = "{0}.jpg".format(photo_fullname)

			#Determine photo save path
			photo_savePath = "{0}{1}".format(folder_path, photo_fullname)

			#Determine photo size url
			photo_size_url = "{0}{1}".format(photo_url, PHOTO_SIZE[photo_size])

			#Find photo direct url
			soup = getRequestsResult(photo_size_url)
			photo_direct_url = firstOrDefault(soup.select('#allsizes-photo img'))['src']
		
		except Exception as e:
			#if photo_size not in PHOTO_SIZE.keys():
				#errorMessage = "<Error> Please enter correct photo_size <Error>"
			#else:
			#errorMessage = e

			#print("\n{0}\n{1}\n{0}".format('='*len(errorMessage), errorMessage))
			print("\n{0}".format(e))
			return			

		#Get Photo Stream
		dl_request = requests.get(photo_direct_url, stream = True)
		
		#Get Target Content Length
		total_length = int(dl_request.headers.get("Content-Length"))

		print("{0}\nDownload Start: {1}".format('='*50, photo_fullname))

		#Save photo to file
		with open(photo_savePath, 'wb') as f:
			complete = 0
			for chunk in dl_request.iter_content(chunk_size):
				if 	chunk:
					f.write(chunk)
					complete += len(chunk)
					singlePhotoComplete(complete, total_length)
			f.close()

		print("\n{0}".format('='*50))
	
	#Download single album
	@staticmethod
	def singleAlbum_DL(album_url, album_name_to_save='', album_photo_size='medium_800', folder_path='', limit_trigger = True, limit_page = 1, chunk_size=512):
		try:	
			#Standardize album url
			if len(album_url.split('/')) >= 7:
				album_url = '/'.join(album_url.split('/')[:7])
				if not album_url.endswith('/'):
					album_url = "{0}/".format(album_url)

			print("\nSeleinum Preparing...Please Wait!")

			#Get SeleinumResult
			driver = getSeleinumResult(album_url)

			#Determine max page
			paginationArea = driver.find_elements_by_css_selector('.view.pagination-view a span')
			pageMax = getPageMax(paginationArea, limit_trigger, limit_page)
			#print(pageMax)
			
			#Get & Parse album title
			album_title = firstOrDefault(driver.find_elements_by_css_selector('.album-title')).text.replace('/','_').replace(',','_').replace(' ','_')

			#Determine target folder
			if len(album_name_to_save) == 0:
				album_name_to_save = album_title
			if not len(folder_path) == 0:
				if not folder_path.endswith('/'):
					folder_path = "{0}/".format(folder_path)
				folder_path = "{0}{1}".format(folder_path, album_name_to_save)
			else:
				folder_path = album_name_to_save			
			folder_path = createFolder(folder_path)

		except Exception as e:
			#errorMessage = "<Error> Please enter correct album url <Error>"
			#errorMessage = e
			#print("\n{0}\n{1}\n{0}".format('='*len(errorMessage), errorMessage))
			print("\n{0}".format(e))

			return
		
		#Now page number
		pageNumber = 1

		while True:

			print("{0}\nDownload Album Start: {1}, Page Number: {2}".format("="*50, album_name_to_save, pageNumber))

			elements = driver.find_elements_by_css_selector('.overlay')
			
			#Photo complete counter
			completed = 0
			total_photo = len(elements)
			
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
				photo_savePath = '{0}{1}'.format(folder_path, photo_fullname) 

				#Determine photo size url
				photo_size_url = "{0}{1}".format(slide_url, PHOTO_SIZE[album_photo_size])

				#Find photo direct url
				soup = getRequestsResult(photo_size_url)
				photo_direct_url = soup.select('#allsizes-photo img')[0]['src']

				#Get Photo Stream
				dl_request = requests.get(photo_direct_url, stream = True)
				with open(photo_savePath, 'wb') as f:
					#complete = 0
					for chunk in dl_request.iter_content(chunk_size):
						if 	chunk:
							f.write(chunk)
							#complete+=1
					f.close()
				completed += 1
				singlePhotoCompleteInAlbum(completed, total_photo)

			print("\n{0}".format('='*50))

			if pageNumber >= pageMax:
				break
			else:

				pageNumber += 1
				newUrl = "{0}page{1}".format(album_url.rstrip('\n'), pageNumber)
				
				print("\nSeleinum Preparing...Please Wait!")
				driver = getSeleinumResult(newUrl)


#Create folder
def createFolder(folder_path):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
	if not folder_path.endswith('/'):
		folder_path = "{0}/".format(folder_path)
	return folder_path