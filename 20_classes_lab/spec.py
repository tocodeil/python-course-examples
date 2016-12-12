import unittest
from mock import patch
from StringIO import StringIO

ex1 = __import__('01')
ex2 = __import__('02')
ex3 = __import__('03')


class TestEx1(unittest.TestCase):
    def test_sum_positive(self):
        summer = ex1.Summer()
        summer.add(10)
        summer.add(20, 30)
        self.assertEqual(60, summer.total())

    def test_sum_negative(self):
        summer = ex1.Summer()
        summer.add(-10)
        summer.add(-20, -30)
        self.assertEqual(-60, summer.total())


class TestEx2(unittest.TestCase):
    def test_count(self):
        for _ in range(10):
            c1 = ex2.MyCounter()
        self.assertEqual(10, ex2.MyCounter.count)

class TestEx3(unittest.TestCase):

    #@patch('sys.stdout', new_callable=StringIO)
    #@patch('__builtin__.raw_input')
    #def test_no(self, std_in, std_out):
    #    luke    = ex3.Widget("Luke")
    #    luke.build()
    #    expected = ''
    #    received = std_out.getvalue().rstrip("\n")
    #    self.assertEqual(expected, received,
    #        '\nExpected: {}\nReceived: {}'.format(expected, received))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input')
    def test_two(self, std_in, std_out):
        luke    = ex3.Widget("Luke")
        leia    = ex3.Widget("Leia")
        luke.add_dependency(leia)
        _all    = ex3.Widget("All")
        _all.add_dependency(luke, leia)

        _all.build()
        expected = 'Luke, Leia'
        received = std_out.getvalue().rstrip("\n")
        self.assertEqual(expected, received,
            '\nExpected: {}\nReceived: {}'.format(expected, received))


    @patch('sys.stdout', new_callable=StringIO)
    @patch('__builtin__.raw_input')
    def test_example(self, std_in, std_out):
        luke    = ex3.Widget("Luke")
        hansolo = ex3.Widget("Han Solo")
        leia    = ex3.Widget("Leia")
        yoda    = ex3.Widget("Yoda")
        padme   = ex3.Widget("Padme Amidala")
        anakin  = ex3.Widget("Anakin Skywalker")
        obi     = ex3.Widget("Obi-Wan")
        darth   = ex3.Widget("Darth Vader")
        _all    = ex3.Widget("All")
        
        luke.add_dependency(hansolo, leia, yoda)
        leia.add_dependency(padme, anakin)
        obi.add_dependency(yoda)
        darth.add_dependency(anakin)
        
        _all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)

        _all.build()
        expected = 'Darth Vader, Luke, Padme Amidala, Anakin Skywalker, Obi-Wan, Leia, Yoda, Han Solo'
        received = std_out.getvalue().rstrip("\n")
        self.assertEqual(expected, received,
            '\nExpected: {}\nReceived: {}'.format(expected, received))



if __name__ == '__main__':
    unittest.main()
