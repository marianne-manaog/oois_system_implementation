import StringIO
import sys
import unittest

from doctor_surgery.src.doctor_surgery.utils import print_name_strings_from_list

empty_list = []


class DummyNamedObject:

    def __init__(self):
        self.name = 'Dr Martens'


class TestUtils(unittest.TestCase):

    def test_print_name_strings_from_list(self):

        doctor_dummy = DummyNamedObject()

        doctors_list_dummy = [{'doctor_1': doctor_dummy}]
        prefix_str_dummy = 'doctor_{}'

        recorded_out = StringIO.StringIO()
        sys.stdout = recorded_out

        print_name_strings_from_list(
            list_of_dicts=doctors_list_dummy,
            prefix_str=prefix_str_dummy
        )

        sys.stdout = sys.__stdout__

        self.assertEqual(
            recorded_out.getvalue().rstrip(),
            doctor_dummy.name
        )
