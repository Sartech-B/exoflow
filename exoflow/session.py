from PIL import Image

class Session():

	def __init__(self, path):
		self.path = path
		self.image = Image.open(path)
		self.width, self.height = self.image.size
		self.pixel = self.image.load()
		self.output = Image.open(path)

	def spill(self, x, y, tolerence):
		if(x>=0):
			if(y>=0):
				pass
			else:
				pass
		else:
			if(y>=0):
				pass
			else:
				pass

		for k in range(self.width):
			for i in range(0, self.height, y):
				for j in range(k, self.width, x):
					current_pixel = image.getpixel((i, j))
		for k in range(self.height):
			for i in range(k, self.height, y):
				for j in range(0, self.width, x):
					current_pixel = image.getpixel((i, j))

	def save(self):
		self.image.save(self.path)

	def test(self):
		print(self.width, self.height)

	def __del__(self):
		self.image.save(self.path)
		del self.image