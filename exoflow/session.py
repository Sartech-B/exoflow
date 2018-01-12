class Session():

	def __init__(self, path):
		self.path = path
		self.image = Image.open(path)
		self.width, self.height = self.image.size()

	def spill(self, x, y, tolerence):
		pass

	def save(self):
		self.image.save(self.path)

	def test(self):
		print(self.width, self.height)

	def __del__(self):
		self.image.save(self.path)
		del self.image