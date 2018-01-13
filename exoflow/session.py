from __future__ import absolute_import
import time

from PIL import Image
import math

from image_processing import *

class Session():

	def __init__(self, path, output_path):
		self.path = path
		self.output_path = output_path

		self.image = Image.open(path)
		self.width, self.height = self.image.size

		self.output = Image.open(output_path)
		self.pixel = self.output.load()

	def spill(self, x, y, tolerence):
		'''if(x!=1 or y!=1):
			if(x>y):
				x = math.ceil(x/y)
				y = 1
			else:
				y = math.ceil(y/x)
				x = 1'''



		for k in range(self.width):
			i = self.height-1
			j = k
			prev = self.image.getpixel((j, i))
			while(i>=0 and j<self.width):
				if(x==1):
					i -= 1
					for c in range(y-1):
						if(i<0):
							break

						current_pixel = self.image.getpixel((j, i))
						if(compare_pixel(prev, current_pixel, tolerence)):
							self.pixel[j, i] = prev
						else:
							self.pixel[j, i] = self.image.getpixel((j, i))
							prev = self.image.getpixel((j, i))
						i -= 1

					j += 1
				else:
					j += 1
					for c in range(x-1):
						if(j>=self.width):
							break

						current_pixel = self.image.getpixel((j, i))
						if(compare_pixel(prev, current_pixel, tolerence)):
							self.pixel[j, i] = prev
						else:
							self.pixel[j, i] = self.image.getpixel((j, i))
							prev = self.image.getpixel((j, i))

						j += 1

					i -= 1

		for k in range(self.height-1, -1, -1):
			i = k
			j = 0
			prev = self.image.getpixel((j, i))
			while(i>=0 and j<self.width):
				if(x==1):
					i -= 1
					for c in range(y-1):
						if(i<0):
							break

						current_pixel = self.image.getpixel((j, i))
						if(compare_pixel(prev, current_pixel, tolerence)):
							self.pixel[j, i] = prev
						else:
							self.pixel[j, i] = self.image.getpixel((j, i))
							prev = self.image.getpixel((j, i))

						i -= 1

					j += 1
				else:
					j += 1
					for c in range(x-1):
						if(j>=self.width):
							break

						current_pixel = self.image.getpixel((j, i))
						if(compare_pixel(prev, current_pixel, tolerence)):
							self.pixel[j, i] = prev
						else:
							self.pixel[j, i] = self.image.getpixel((j, i))
							prev = self.image.getpixel((j, i))

						j += 1

					i -= 1

		'''
		for i in range(0, self.height, y):
			for j in range(k, self.width, x):
				current_pixel = image.getpixel((i, j))

		for k in range(self.height-1, -1, -1):
			for i in range(k, self.height, y):
				for j in range(0, self.width, x):
					current_pixel = image.getpixel((i, j))
		'''

	def save(self):
		#self.image.save(self.path)
		self.output.save(self.output_path)

	def test(self):
		print(self.width, self.height)

	'''
	def __del__(self):
		self.image.save(self.path)
		self.output.save(self.path)
		del self.image
		del self.output
	'''
