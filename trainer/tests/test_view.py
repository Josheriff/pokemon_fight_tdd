import unittest
from ..view import TrainerReciver

class testTrainerView(unittest.TestCase):
    def test_name_capitalize(self):
        # Arrange
        trainer = TrainerReciver()
        fake_data = [{"name":"aname"}, {"name": "anothername"}]
        expected_result = [{"name":"Aname"}, {"name": "Anothername"}]

        # ACT
        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)

        # ASSERT
        assert result == expected_result
    
    def test_when_name_has_a_number(self):
        # Arrange
        trainer = TrainerReciver()
        fake_data = [{"name":"aname1"}, {"name": "anothername"}]
        expected_result = [{"name":"Aname1"}, {"name": "Anothername"}]

        # ACT
        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        # ASSERT
        assert result == expected_result
