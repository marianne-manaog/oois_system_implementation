import unittest

from mock import patch

from doctor_surgery.src.doctor_surgery.utils_validation import (
    validate_float_input,
    validate_int_input,
    validate_str_input
)

valid_float = 2.
valid_int = 2
valid_str = 'Carmen'


class TestUtilsValidation(unittest.TestCase):

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_float)
    def test_validate_float_input_valid(self, _):

        expected_float = valid_float
        result_float = validate_float_input()

        self.assertEqual(expected_float, result_float)

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_str)
    def test_validate_float_input_invalid(self, _):
        self.assertRaises(ValueError, validate_float_input())

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_int)
    def test_validate_int_input_valid(self, _):

        expected_int = valid_int
        result_int = validate_int_input()

        self.assertEqual(expected_int, result_int)

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_str)
    def test_validate_int_input_invalid(self, _):
        self.assertRaises(ValueError, validate_int_input())

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_str)
    def test_validate_str_input_valid(self, _):

        expected_str = valid_str
        result_str = validate_str_input()

        self.assertEqual(expected_str, result_str)

    @patch('doctor_surgery.src.doctor_surgery.utils_validation.raw_input', return_value=valid_int)
    def test_validate_str_input_invalid(self, _):
        self.assertRaises(TypeError, validate_str_input())
