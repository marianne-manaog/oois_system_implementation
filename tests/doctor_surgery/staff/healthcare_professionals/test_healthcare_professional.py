import unittest

from doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.healthcare_professional import \
    HealthcareProfessional

empty_list = []

hcp_dummy = HealthcareProfessional(
    name='Deena Petringa',
    employee_number='12345',
    appointments_list=empty_list,
    patients_list=empty_list
)


class DummyNamedObject:

    def __init__(self):
        self.name = 'Dr Martens'


class TestHealthCareProfessional(unittest.TestCase):

    def test_consultation(self):

        appointment_type_dummy = 'Standard consultation'
        patient_full_name_dummy = 'Martha Rodgers'

        expected_appointment_string = appointment_type_dummy

        result_appointment_string = hcp_dummy.consultation(
            appointment_type=appointment_type_dummy,
            patient_full_name=patient_full_name_dummy
        )

        self.assertEqual(expected_appointment_string, result_appointment_string)
