import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
         assert self.calc.multiply(self, 2, 4) == 8

    def test_adding_success(self):
        assert self.calc.division(self,6,2) == 3

    def test_adding_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 5) == 7

    def teardown(self):
        print('Выполнение метода Teardown')