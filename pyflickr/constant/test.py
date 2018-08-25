import requests
from bs4 import BeautifulSoup

head = {
	'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

#中央氣象局的位址
url = "https://www.cwb.gov.tw/V7/observe/radar/"
req = requests.get(url, headers = head)
content = req.content
soup = BeautifulSoup(content,'html.parser')
'''
img_url = soup.select('img')[0]['src']

full_url = "https://www.cwb.gov.tw{0}".format(img_url)

#下載雷達迴波圖
dl_img = requests.get(full_url, stream = True, headers = head)
fileName = full_url.split('/')[-1]
with open(fileName, 'wb') as f:
	for chunk in dl_img.iter_content():
		if chunk:
			f.write(chunk)
	f.close()
'''