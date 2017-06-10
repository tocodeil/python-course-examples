import unittest
import re
import subprocess
from StringIO import StringIO
from mock import patch

DATA_POSITIVE_VALUES = [10, 20, 30, 40, 30, 20, 30, 25, 10, 20]
DATA_NEGATIVE_VALUES = [-20, -30, -40, -50, -40, -40, -40, -30, -20, -10]
DATA_FLOATS          = [10.1, 10.2, 10.3, 4.5, 27, 99.9, 10, 20, 30, 40]

class TestEx1(unittest.TestCase):
    @patch('__builtin__.raw_input', return_value='10')
    def test_reads_10_numbers(self, spy):
        execfile('01.py')
        self.assertEqual(spy.call_count, 10,
                         'Expected 10 numbers but got %d' % spy.call_count)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input')
    def test_prints_largest_positive(self, in_spy, out_spy):
        in_spy.side_effect = DATA_POSITIVE_VALUES
        execfile('01.py')
        self.assertIn('40', out_spy.getvalue(),
                      'Expected 40, got: %s' % out_spy.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input')
    def test_prints_largest_negative(self, in_spy, out_spy):
        in_spy.side_effect = DATA_NEGATIVE_VALUES
        execfile('01.py')
        self.assertIn('-10', out_spy.getvalue(),
                      'Expected -10, got: %s' % out_spy.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input')
    def test_prints_largest_float(self, in_spy, out_spy):
        in_spy.side_effect = DATA_FLOATS
        execfile('01.py')
        self.assertIn('99.9', out_spy.getvalue(),
                      'Expected 99.9, got: %s' % out_spy.getvalue())


class TestEx2(unittest.TestCase):
    def test_age_in_months(self):
        proc = subprocess.Popen(['python', '02.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate('12')
        self.assertEqual(out, '144\n',
                        'Expected: 144. Got: %s' % out)


class TestEx3(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.randint', return_value=2345)
    @patch('random.randrange', return_value=2345)
    def test_sum_2345(self, randrange_spy, rand_spy, out_spy):
        execfile('03.py')
        self.assertIn('14', out_spy.getvalue(),
                      'Expected 14 but got: %s' % out_spy.getvalue())

    @patch('random.randint', return_value=7)
    @patch('random.randrange', return_value=7)
    def test_randomize_in_range(self, randrange_spy, rand_spy):
        execfile('03.py')
        if randrange_spy.called:
            randrange_spy.assert_called_once_with(10000)
        else:
            rand_spy.assert_called_once_with(1, 10000)


class TestEx4(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input', return_value='10')
    def test_line_oreder(self, in_spy, out_spy):
        data = [
                'line one',
                'line two',
                'line three',
                'line four',
                ''
        ]

        in_spy.side_effect = data
        expected = '\n'.join([l for l in reversed(data[:-1])])

        execfile('04.py')
        got = out_spy.getvalue().strip()

        self.assertIn(expected, got,
                      'expected: [%s] got: [%s]' %
                      (expected, got))


class TestEx5(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_find_number(self, out_spy):
        execfile('05.py')

        m = re.search(r'(\d+)', out_spy.getvalue().strip())
        got = m.group(0)

        self.assertTrue(int(got) % 7 == 0, 'Got [%s] which does not divide by 7' % got)
        self.assertTrue(int(got) % 13 == 0, 'Got [%s] which does not divide by 13' % got)
        self.assertTrue(int(got) % 15 == 0, 'Got [%s] which does not divide by 15' % got)
        self.assertTrue(int(got) > 0, 'Got [%s] which is out of range')


class TestEx6(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.randint', return_value=10)
    @patch('random.randrange', return_value=10)
    def test_lcm_4_6(self, randrange_spy, rand_spy, out_spy):
        rand_spy.side_effect = [4, 6]
        randrange_spy.side_effect = [4, 6]
        execfile('06.py')

        got = out_spy.getvalue()
        self.assertIn('12', got, 'Expected 12, got: [%s]' % got)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.randint', return_value=10)
    @patch('random.randrange', return_value=10)
    def test_lcm_8_6(self, randrange_spy, rand_spy, out_spy):
        rand_spy.side_effect = [8, 6]
        randrange_spy.side_effect = [8, 6]
        execfile('06.py')

        got = out_spy.getvalue()
        self.assertIn('24', got, 'Expected 24, got: [%s]' % got)


if __name__ == '__main__':
    unittest.main()
