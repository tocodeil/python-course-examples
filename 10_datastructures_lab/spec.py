import unittest
import subprocess
import re


def trycredentials(user, pwd):
    proc = subprocess.Popen(
            ['python', '01.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    outs, errs = proc.communicate('%s\n%s\n' % (user, pwd))
    return outs + errs


class TestEx1(unittest.TestCase):
    def test_correct_credentials(self):
        res = trycredentials('apple', 'red')
        self.assertIn('welcome master', res.lower(),
                      'No welcome banner in: [%s]' % res)

    def test_incorrect_credentials(self):
        res = trycredentials('foo', 'bar')
        self.assertIn('intruder alert', res.lower(),
                      'No error banner in: [%s]' % res)

    def test_correct_username_wrong_password(self):
        res = trycredentials('apple', 'blue')
        self.assertIn('intruder alert', res.lower(),
                      'No error banner in: [%s]' % res)


class TestEx3(unittest.TestCase):
    def test_3(self):
        proc = subprocess.Popen(
                ['python', '03.py', 'mycar', 'home', 'none'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE)

        outs, errs = proc.communicate()
        lines = outs.split('\n')
        self.assertIn('10.0.0.5', lines[0], 'mycar should have IP 10.0.0.5')
        self.assertIn('194.90.2.1', lines[1], 'home should have IP 194.90.2.1')
        self.assertEqual(re.search(r'\d', lines[2]), None,
                         'none should not have IP')

if __name__ == '__main__':
    unittest.main()
