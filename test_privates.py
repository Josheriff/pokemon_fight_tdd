import unittest

class Aritmethod:
    def ecuation(self, a, b):
        sum = self._sum(a,b)
        mult = sum * 2
        elevate = self._elevate(mult)
        return self._div_by_two(elevate)        
                     
    
    def _sum(self, a, b):
        return a + b

    def _elevate(self, num):
        return num * num

    def _div_by_two(self, num):
        return num / 2

class TestAritMethod(unittest.TestCase):
    def test_ecuation_finish_properly(self):
         # Arrange
        arit = Aritmethod()

        # ACT
        result = arit.ecuation(1,2)

        # Assert
        assert result == 18