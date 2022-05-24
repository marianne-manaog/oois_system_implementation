# This Python file contains the definition of the class 'Doctor', which inherits the attributes and the methods of the
# class 'HealthcareProfessional' and extends it by enabling to issue a prescription.

import logging

from doctor_surgery.src.doctor_surgery.constants import DRUG_W_PLACEHOLDER
from doctor_surgery.src.doctor_surgery.utils_validation import validate_float_input, validate_int_input
from .healthcare_professional import HealthcareProfessional
from doctor_surgery.src.doctor_surgery.prescriptions.prescription import Prescription

doctor_log = logging.getLogger(__name__)


class Doctor(HealthcareProfessional):
    """
    This class defines a doctor, which inherits the attributes and the methods of the class 'HealthcareProfessional'
    and extends it by enabling to issue a prescription.
    """

    def __init__(self, name, employee_number, appointments_list, patients_list):  # pragma: no cover
        # type: (str, str, List[Dict], List[Patient]) -> None
        HealthcareProfessional.__init__(self, name, employee_number, appointments_list, patients_list)

    def __str__(self):  # pragma: no cover
        return "<Doctor whose name is '{}' and employee number is '{}', with the list of appointments '{}' " \
               "and the list of patients '{}'>".format(
            self.name, self.employee_number, self.appointments_list, self.patients_list
        )

    def __repr__(self):  # pragma: no cover
        return "Doctor: (name: {}, employee number: {}, appointments_list: {}, patients_list: {})".format(
            self.name, self.employee_number, self.appointments_list, self.patients_list
        )

    def issue_prescription(self, patient):
        # type: (Patient) -> None
        """
        Issue a prescription for a patient.

        Args:
            patient: Patient
                    The patient for whom a prescription is issued.
        """

        prescription_type = raw_input("Please enter the name of the drug to prescribe: ")

        print("Please enter the number of items to be prescribed: ")
        quantity = validate_int_input()

        print("Please enter the dosage in mg: ")
        dosage = validate_float_input()

        prescription_issued = Prescription(
          prescription_type=prescription_type,
          patient=patient,
          doctor=self.name,
          quantity=quantity,
          dosage=dosage
        )

        drug_num = len(patient.list_of_prescriptions) + 1
        drug_string = DRUG_W_PLACEHOLDER.format(drug_num)
        prescription_issued_dict = {drug_string: prescription_issued}

        patient.list_of_prescriptions.append(prescription_issued_dict)

        doctor_log.info("The following drug has been prescribed: {}".format(prescription_issued_dict))

        print("The following drug has been prescribed: {}".format(prescription_issued_dict))
