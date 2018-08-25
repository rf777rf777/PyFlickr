class About:
	@property
	def title(self):
		return self._title
	@title.setter
	def title(self, title):
		self._title = title

	@property
	def subtitle(self):
		return self._subtitle
	@subtitle.setter
	def subtitle(self, subtitle):
		self._subtitle = subtitle

	@property
	def avatar(self):
		return self._avatar
	@avatar.setter
	def avatar(self,avatar):
		self._avatar = avatar

	@property
	def followers(self):
		return self._followers
	@followers.setter
	def followers(self, followers):
		self._followers = followers

	@property
	def following(self):
		return self._following
	@following.setter
	def following(self,following):
		self._following = following

	@property
	def description(self):
		return self._description
	@description.setter
	def description(self,description):
		self._description = description

	@property
	def infos(self):
		return self._infos
	@infos.setter
	def infos(self,infos):
		self._infos = infos

	@property
	def general_stats(self):
		return self._general_stats
	@general_stats.setter
	def general_stats(self,general_stats):
		self._general_stats = general_stats

	@property
	def showcase_photos(self):
		return self._showcase_photos
	@showcase_photos.setter
	def showcase_photos(self,showcase_photos):
		self._showcase_photos = showcase_photos

	@property
	def popular_photos(self):
		return self._popular_photos
	@popular_photos.setter
	def popular_photos(self,popular_photos):
		self._popular_photos = popular_photos
		
		
		

