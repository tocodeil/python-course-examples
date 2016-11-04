import unittest

ex1 = __import__('01')
ex2 = __import__('02')


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


if __name__ == '__main__':
    unittest.main()
