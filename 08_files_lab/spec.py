import unittest
import os
import subprocess

FILES = {
        'a.txt': '''
one
two
three
four
'''[1:],

        'b.txt': '''
red
blue
green
white
orange
blue
cyan
magenta
'''[1:],
}


def init_files():
    for fname in FILES:
        with open(fname, 'w') as fout:
            fout.write(FILES[fname])


class TestEx1(unittest.TestCase):
    def setUp(self):
        init_files()

    def tearDown(self):
        for fname in FILES:
            os.remove(fname)

    def test_concat_to_a(self):
        subprocess.call(['python', '01.py', 'a.txt', 'b.txt'])
        with open('a.txt', 'r') as f:
            got = f.read()

        expected = FILES['a.txt'] + FILES['b.txt']
        self.assertEqual(expected, got,
                         'Expected: [%s], Got: [%s]' % (expected, got))


class TestEx2(unittest.TestCase):
    def setUp(self):
        init_files()

    def tearDown(self):
        for fname in FILES:
            os.remove(fname)
        os.remove('c.txt')

    def test_concat_to_a(self):
        subprocess.call(['python', '02.py', 'a.txt', 'b.txt', 'c.txt'])
        with open('c.txt', 'r') as f:
            got = f.read()

        expected = '''
one
red
two
blue
three
green
four
white
orange
blue
cyan
magenta
'''[1:]

        self.assertEqual(expected, got,
                         'Expected: [%s], Got: [%s]' % (expected, got))

class TestEx3(unittest.TestCase):
    def test_sum(self):
        res = subprocess.check_output(['python', '03.py', 'numbers.txt']).strip()
        self.assertEqual('149', res, 'Expected: [%s]. Got: [%s]' % (149, res))


if __name__ == '__main__':
    unittest.main()
