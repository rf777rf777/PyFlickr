from pyflickr.model.enum import PhotoSizeEnum

class Photo:
	def __init__(self, photo_url):

		#Standardize photo url
		if len(photo_url.split('/')) >= 6:
			photo_url = '/'.join(photo_url.split('/')[:6])
			if photo_url[-1] != '/':
				photo_url += '/'
		
		self._title = "{0}".format(photo_url.split('/')[-2])
		self._slide_url = photo_url
		self._sq_75 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.square_75.value)
		self._q_150 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.square_150.value)
		self._t_100 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.thumbnail.value)
		self._s_240 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.small_240.value)
		self._n_320 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.small_320.value)
		self._m_500 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.medium_500.value)
		self._z_640 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.medium_640.value)
		self._c_800 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.medium_800.value)
		self._l_1024 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.large_1024.value)
		self._h_1600 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.large_1600.value)
		self._k_2048 = "{0}{1}".format(self._slide_url, PhotoSizeEnum.large_2048.value)
		self._o = "{0}{1}".format(self._slide_url, PhotoSizeEnum.original.value)

	@property
	def title(self):
		return self._title

	@property
	def slide(self):
		return self._slide_url

	@property
	def square_75(self):
		return self._sq_75

	@property
	def square_150(self):
		return self._q_150

	@property
	def thumbnail(self):
		return self._t_100

	@property
	def small_240(self):
		return self._s_240

	@property
	def small_320(self):
		return self._n_320	

	@property
	def medium_500(self):
		return self._m_500

	@property
	def medium_640(self):
		return self._z_640

	@property
	def medium_800(self):
		return self._c_800

	@property
	def large_1024(self):
		return self._l_1024

	@property
	def large_1600(self):
		return self._h_1600

	@property
	def large_2048(self):
		return self._k_2048

	@property
	def original(self):
		return self._o	