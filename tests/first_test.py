import pytest

from app.calculator import Calculator

if __init__ == '__init__':
   unittest.main()

class TestCalc:

    def setup(self):
        self.calc = Calculator()

    def test_multiply_ok(self):
        assert self.calc.multiply(2, 3) == 2 * 3

    def test_division_ok(self):
        assert self.calc.division(2, 3) == 2 / 3

    def test_subtraction_ok(self):
        assert self.calc.subtraction(2, 3) == 2 - 3

    def test_adding_ok(self):
        assert self.calc.adding(2, 3) == 2 + 3
