import unittest
import subprocess
import sys

ex2 = __import__('02')

class TestEx1(unittest.TestCase):
    def test_props(self):
        command = [sys.executable, '01.py', 'props', 'name']
        p = subprocess.Popen(command,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            shell=False)
        out,err = p.communicate()
        self.assertEqual('joe', out.rstrip("\n"), '\nExpected: joe\nReceived: {}'.format(out))

    def test_regex(self):
        command = [sys.executable, '01.py', 'props', 'n.me']
        p = subprocess.Popen(command,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            shell=False)
        out,err = p.communicate()
        self.assertEqual('bar', out.rstrip("\n"), '\nExpected: bar\nReceived: {}'.format(out))

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

if __name__ == '__main__':
        unittest.main()

