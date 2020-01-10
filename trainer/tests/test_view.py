import unittest
import pytest
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

    def test_when_only_has_numbers(self):
        # Arrange
        trainer = TrainerReciver()
        fake_data = [{"name":"11111"}, {"name": "22222"}]
        expected_result = [{"name":"11111"}, {"name": "22222"}]

        # ACT
        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        # ASSERT
        assert result == expected_result

    def test_when_start_with_number(self):
        # Arrange
        trainer = TrainerReciver()
        fake_data = [{"name":"11alberto"}, {"name": "22silvia"}]
        expected_result = [{"name":"11alberto"}, {"name": "22silvia"}]

        # ACT
        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        # ASSERT
        assert result == expected_result

    def test_when_name_come_empty(self):
        # Arrange
        trainer = TrainerReciver()
        fake_data = [{"name":""}, {"name": "22silvia"}]
        expected_result = [{"name":""}, {"name": "22silvia"}]

        # ACT
        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        # ASSERT
        assert result == expected_result