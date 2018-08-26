#!/usr/bin/python3
# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

'''
HEAD = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
'''
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

def FirstOrDefault(listObject):
	if len(listObject) == 0:
		return None
	#return next((f for f in listObject if listObject.index(f) == 0), None)
	return listObject[0]

def GetRequestsResult(url):
	result = requests.get(url, HEAD).content
	soup = BeautifulSoup(result, HTML_PARSER)

	return soup

def GetSeleinumResult(url, driverUri='././phantomjs', wait_second=3):
	driver = webdriver.PhantomJS(executable_path=driverUri)
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
def completeInTerminal(complete,total):
	if 	total == 0:
		return
	done = int(30 * complete / total)
	sys.stdout.write("\rCompleted：( %s / %s )[ %s%s ]" % (int(complete/total*100), int(total/total*100), '#'*done, '-'*(30 - done)))
	sys.stdout.flush()