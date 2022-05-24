import unittest

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

dummy_drug_name = "Bellpepperidone"
dummy_drug_initial_quantity = 10
dummy_drug_1 = Prescription(
    prescription_type=dummy_drug_name,
    patient=dummy_patient,
    quantity=dummy_drug_initial_quantity,
    dosage=149.5,
    doctor=dummy_doctor
)

expected_drug_string = 'drug_1'
dummy_patient.list_of_prescriptions = [{expected_drug_string: dummy_drug_1}]


class TestPatient(unittest.TestCase):

    def test_request_repeat_prescription_drug_in_dict(self):

        result_drug_string, result_prescription = dummy_patient.request_repeat_prescription(dummy_drug_name)

        dummy_drug_1.quantity = 9

        self.assertEqual(expected_drug_string, result_drug_string)
        self.assertEqual(
            dummy_drug_initial_quantity - 1,
            result_prescription['drug_1'].quantity
        )
