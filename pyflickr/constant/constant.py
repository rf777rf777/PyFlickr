#!/usr/bin/python3
# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import sys

HEAD = {
	"Accept": "application/json"
}

PHOTO_SIZE = {
	"square_75" : "sizes/sq",
	"square_150" : "sizes/q",
	"thumbnail" : "sizes/t",
	"small_240" : "sizes/s",
	"small_320" : "sizes/n",
	"medium_500" : "sizes/m",
	"medium_640" : "sizes/z",
	"medium_800" : "sizes/c",
	"large_1024" : "sizes/l",
	"large_1600" : "sizes/h",
	"large_2048" : "sizes/k",
	"original" : "sizes/o"
}

HTML_PARSER = 'html.parser'

HTTPS_TITLE = 'https:'

ROOT_URL = "https://www.flickr.com"

#DRIVER_URI = 'driver/phantomjs'
DRIVER_URI = 'driver/chromedriver'

def firstOrDefault(listObject):
	if len(listObject) == 0:
		return None
	#return next((f for f in listObject if listObject.index(f) == 0), None)
	return listObject[0]

def getRequestsResult(url):
	result = requests.get(url, headers=HEAD).content
	soup = BeautifulSoup(result, HTML_PARSER)

	return soup

def getSeleinumResult(url, driverUri=DRIVER_URI, wait_second=3):
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--no-sandbox')  
	#driver = webdriver.Chrome(driver_path='<path-to-driver>/chromedriver', chrome_options=chrome_options,
  	#service_args=['--verbose', '--log-path=<path-to-log>/chromedriver.log'])
	driver = webdriver.Chrome(executable_path = driverUri, chrome_options=chrome_options)
	#driver = webdriver.PhantomJS(executable_path=driverUri)

	print("\nDriver is Now Loading...")

	driver.get(url)

	driver.maximize_window()

	js = "window.scrollTo(0, document.body.scrollHeight);"

	for i in range(1,5):
		driver.execute_script(js)
		time.sleep(wait_second)

	return driver

#get pageMax number
def getPageMax(paginationArea, upperlimit, pagelimit):
	pageParent = []
	if len(paginationArea) != 0:
		pageFilter = ["paginationRightClick","paginationLeftClick"]
		for i in paginationArea:
			if i.find_element_by_xpath("..").get_attribute('data-track') not in pageFilter and i.text != '1':
				pageParent.append(i.text)

	pageMax = 0 if len(pageParent) == 0 else int(pageParent[-1])
	if upperlimit and pagelimit < pageMax:
		pageMax = pagelimit

	return pageMax


#ProgressBar on Terminal  
def singlePhotoCompleteInAlbum(complete,total):
	if total == 0:
		return
	done = int(30 * complete / total)
	sys.stdout.write("\rCompleted：( %s / %s )[ %s%s ]" % (complete, total, '#'*done, '-'*(30 - done)))
	sys.stdout.flush()

#ProgressBar on Terminal  
def singlePhotoComplete(complete,total):
	if total == 0:
		return
	percent = complete / total
	done = int(30 * percent)
	sys.stdout.write("\rCompleted：[ %s%s ] %s%s" % ('#'*done,' '*(30-done), int(percent*100), '%'))
	sys.stdout.flush()
