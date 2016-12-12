import unittest

ex1 = __import__('01')
ex2 = __import__('02')
ex3 = __import__('03')
ex4 = __import__('04')
ex5 = __import__('05')


class TestEx1(unittest.TestCase):
    def test_sum_positive(self):
        res = ex1.mysum(10, 20, 30)
        self.assertEqual(60, res, 'mysum(10,20,30) = %d (expected 60)' % res)

    def test_sum_negative(self):
        res = ex1.mysum(-10, -20, -30)
        self.assertEqual(-60, res, 'mysum(...) = %d (expected -60)' % res)

    def test_sum_with_strings(self):
        res = ex1.mysum(10, 20, 30, 'foo', 'bar', 40)
        self.assertEqual(100, res, 'mysum(...) = %d (expected 100)' % res)

    def test_mul_positive(self):
        res = ex1.mymul(1, 2, 3)
        self.assertEqual(6, res, 'mymul(1,2,3) = %d (expected 6)' % res)

    def test_mul_negative(self):
        res = ex1.mymul(-1, -2, -3)
        self.assertEqual(-6, res, 'mymul(-1,-2,-3) = %d (expected -60)' % res)

    def test_mul_with_strings(self):
        res = ex1.mymul(1, 2, 3, 'foo', 'bar', 4)
        self.assertEqual(24, res, 'mymul(...) = %d (expected 24)' % res)


class TestEx2(unittest.TestCase):
    def test_valid(self):
        ex2.take_string_and_number('x', 10)
        self.assertTrue(True)

    def test_first_not_string(self):
        with self.assertRaises(Exception):
            ex2.take_string_and_number(10, 20)

    def test_second_not_number(self):
        with self.assertRaises(Exception):
            ex2.take_string_and_number('x', 'y')


class TestEx3(unittest.TestCase):
    def test_sum_tens(self):
        res = ex3.sum_tens(120, 140, 1123)
        self.assertEqual(8, res,
                         'sum_tens(120, 140, 1123) = %d. Expected 8' % res)


class TestEx4(unittest.TestCase):
    def test_longer_than(self):
        res = ex4.longer_than(4, "foo", "bar", "fantastic", "python", "abc")
        expected = ['fantastic', 'python']
        self.assertEqual(expected, res)


class TestEx5(unittest.TestCase):
    def test_group_by(self):
        res = ex5.groupby(
                lambda s: frozenset(s),
                ['add', 'dad', 'help', 'rome', 'more'])

        self.assertIn(frozenset(['a', 'd']), res)
        self.assertIn(frozenset(['h', 'e', 'l', 'p']), res)
        self.assertIn(frozenset(['r', 'o', 'm', 'e']), res)
        self.assertIn('add', res[frozenset(['a', 'd'])])
        self.assertIn('dad', res[frozenset(['a', 'd'])])
        self.assertIn('help', res[frozenset(['h', 'e', 'l', 'p'])])
        self.assertIn('rome', res[frozenset(['r', 'o', 'm', 'e'])])
        self.assertIn('more', res[frozenset(['r', 'o', 'm', 'e'])])


if __name__ == '__main__':
    unittest.main()
