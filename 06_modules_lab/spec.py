import unittest
import subprocess
import sys


class TestEx1(unittest.TestCase):
    def test_print_hello_python(self):
        proc = subprocess.Popen([sys.executable, '01.py', '5'],
                                stdout=subprocess.PIPE)
        for i in range(5):
            line = proc.stdout.readline()
            self.assertEqual('hello python', line.strip().lower())


class TestEx2(unittest.TestCase):
    def test_print_sum_positive(self):
        proc = subprocess.Popen([sys.executable, '02.py', '5', '12'],
                                stdout=subprocess.PIPE)
        line = proc.stdout.readline()
        self.assertIn('17', line)

    def test_print_sum_negative(self):
        proc = subprocess.Popen([sys.executable, '02.py', '-5', '-12'],
                                stdout=subprocess.PIPE)
        line = proc.stdout.readline()
        self.assertIn('-17', line)

class TestEx2Bonus(unittest.TestCase):
    def test_print_sum_positive(self):
        proc = subprocess.Popen([sys.executable, '02_bonus.py', '5', '12'],
                                stdout=subprocess.PIPE)
        line = proc.stdout.readline()
        self.assertIn('17', line)

    def test_print_sum_string_first(self):
        proc = subprocess.Popen([sys.executable, '02_bonus.py', 'abc', '12'],
                                stdout=subprocess.PIPE)
        line = proc.stdout.readline()
        self.assertIn('Syntax error: please enter integers only.\n', line)

    def test_print_sum_float_first(self):
        proc = subprocess.Popen([sys.executable, '02_bonus.py', '2.3', '12'],
                                stdout=subprocess.PIPE)
        line = proc.stdout.readline()
        self.assertIn('Syntax error: please enter integers only.\n', line)


if __name__ == '__main__':
    unittest.main()
