import unittest
import pytest
from ..view import TrainerReciver

class TestTrainerView(unittest.TestCase):
    def test_name_capitalize(self):
        trainer = TrainerReciver()
        fake_data = [{"name":"aname"}, {"name": "anothername"}]
        expected_result = [{"name":"Aname"}, {"name": "Anothername"}]

        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)

        assert result == expected_result
    
    def test_when_name_has_a_number_capitalize_if_first_is_letter(self):
        trainer = TrainerReciver()
        fake_data = [{"name":"aname1"}, {"name": "anothername"}]
        expected_result = [{"name":"Aname1"}, {"name": "Anothername"}]

        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        assert result == expected_result

    def test_when_only_has_numbers_nothing_happens(self):
        trainer = TrainerReciver()
        fake_data = [{"name":"11111"}, {"name": "22222"}]
        expected_result = [{"name":"11111"}, {"name": "22222"}]

        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        assert result == expected_result

    def test_when_start_with_number_not_capitalize_nor_error(self):
        trainer = TrainerReciver()
        fake_data = [{"name":"11alberto"}, {"name": "22silvia"}]
        expected_result = [{"name":"11alberto"}, {"name": "22silvia"}]

        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        assert result == expected_result

    def test_when_name_come_empty_nothing_happens(self):
        trainer = TrainerReciver()
        fake_data = [{"name":""}, {"name": "22silvia"}]
        expected_result = [{"name":""}, {"name": "22silvia"}]

        result = trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)
        
        assert result == expected_result

    def test_when_is_none_raise_error(self):
        trainer = TrainerReciver()
        fake_data = [{"name": None}, {"name": "22silvia"}]
            
        with pytest.raises(AttributeError):
            assert trainer.capitalize(fake_data) # SUT (SUBJECT UNDER TEST)

    def test_when_list_is_empty_raise_error(self):
        trainer = TrainerReciver()

        with pytest.raises(IndexError):
            assert trainer.capitalize([]) # SUT (SUBJECT UNDER TEST)
       