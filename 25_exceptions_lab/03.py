#!/usr/bin/python

import unittest

class InvalidImageExt(Exception): pass

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

class ImageFile(object):
	def __init__(self, name):
		self.name = name
		
		if not self.name.endswith('.png'):
			raise InvalidImageExt
		else:
			open(self.name, 'w+')
				
		
unittest.main()