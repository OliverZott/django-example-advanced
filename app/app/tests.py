from django.test import SimpleTestCase

from app import calc


# import calc  # for local testing


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        x = 3
        y = 5

        res = calc.add(x, y)

        self.assertEqual(res, 8)

    def test_subtract_numbers(self):
        x = 9
        y = 2

        res = calc.subtract(x, y)

        self.assertEqual(res, 7)
