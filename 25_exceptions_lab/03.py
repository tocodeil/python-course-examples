"""
Write code to make the following unit test pass
"""

class InvalidImageExt(Exception):
    print "Wrong extantion"
    pass

class ImageFile(object):
    def __init__(self, filename):
        if filename[-4:] != ".png":
            raise InvalidImageExt


import unittest

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()




