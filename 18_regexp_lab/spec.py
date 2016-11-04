import unittest

ex2 = __import__('02')


class TestEx2(unittest.TestCase):
    def test_tocamelcase(self):
        self.assertEqual(ex2.toCamelCase('welcome'), 'welcome')
        self.assertEqual(ex2.toCamelCase('hello_world'), 'helloWorld')
        self.assertEqual(ex2.toCamelCase('get_name'), 'getName')
        self.assertEqual(ex2.toCamelCase('no_more_shall_we_part'), 'noMoreShallWePart')

    def test_tosnakecase(self):
        self.assertEqual(ex2.to_underscore('welcome'), 'welcome')
        self.assertEqual(ex2.to_underscore('helloWorld'), 'hello_world')
        self.assertEqual(ex2.to_underscore('getName'), 'get_name')
        self.assertEqual(ex2.to_underscore('noMoreShallWePart'), 'no_more_shall_we_part')
