import StringIO
import sys
import unittest

from mock import patch

from doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.doctor import Doctor
from doctor_surgery.src.doctor_surgery.patients.patient import Patient
from doctor_surgery.src.doctor_surgery.prescriptions.prescription import Prescription

empty_list = []

dummy_doctor_name = 'Neil Melendez'
dummy_patient_name = 'Piper Halliwell'

dummy_doctor = Doctor(
    name=dummy_doctor_name,
    employee_number="6789",
    appointments_list=empty_list,
    patients_list=[dummy_patient_name]
)

dummy_patient = Patient(
    name=dummy_patient_name,
    address="1630 Revello Drive",
    phone="0123456789",
    registered_doctor=dummy_doctor,
    list_of_prescriptions=empty_list
)


class TestDoctor(unittest.TestCase):

    @patch(
        'doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.doctor.raw_input',
        return_value='Bellpepperidone'
    )
    @patch(
        'doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.doctor.validate_int_input',
        return_value=2
    )
    @patch(
        'doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.doctor.validate_float_input',
        return_value=150.5
    )
    def test_issue_prescription(self, mock_dosage, mock_quantity, mock_prescription_type):

        prescription_issued = Prescription(
          prescription_type=mock_prescription_type,
          patient=dummy_patient,
          doctor=dummy_doctor,
          quantity=mock_quantity,
          dosage=mock_dosage
        )

        expected_prescription_issued_dict = {'drug_1': prescription_issued}

        recorded_out = StringIO.StringIO()
        sys.stdout = recorded_out

        dummy_doctor.issue_prescription(dummy_patient)

        sys.stdout = sys.__stdout__

        self.assertEqual(
            recorded_out.getvalue().splitlines()[2].split(
                'The following drug has been prescribed: ')[1].split('prescription_type:')[1].split(', patient:')[0],
            str(expected_prescription_issued_dict).split(
                'The following drug has been prescribed: ')[0].split('prescription_type:')[2].split(', patient:')[0]
        )
