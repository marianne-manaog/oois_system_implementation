# This Python file contains the definition of the class 'HealthcareProfessional', who can provide a
# consultation.

import logging

healthcare_professional_log = logging.getLogger(__name__)


class HealthcareProfessional:
    """
    This class defines a healthcare professional, such as a doctor or a nurse, by their full name, employee number,
    list of appointments, and a list of patients assigned.
    """

    def __init__(self, name, employee_number, appointments_list, patients_list):
        # type: (str, str, List[Dict], List[Patient]) -> None
        self.name = name
        self.employee_number = employee_number
        self.appointments_list = appointments_list
        self.patients_list = patients_list

    def __str__(self):  # pragma: no cover
        return "<Healthcare professional whose name is '{}' and employee number is '{}', with the list of " \
               "appointments '{}' and the list of patients assigned '{}'>".format(self.name,
                                                                                  self.employee_number,
                                                                                  self.appointments_list,
                                                                                  self.patients_list)

    def __repr__(self):  # pragma: no cover
        return "Healthcare professional: (name: {}, employee number: {}, appointments_list: {}, " \
               "patients_list: {})".format(self.name, self.employee_number, self.appointments_list, self.patients_list)

    def consultation(self, appointment_type, patient_full_name):
        # type: (str, str) -> str
        """
        Provide a consultation to a patient.

        Args:
            appointment_type: str
                    The type of appointment for which a consultation is performed.
            patient_full_name: str
                    The full name of the patient undergoing a consultation.

        Returns:
            the appointment_type (str) itself, as this is a dummy method to satisfy the OOP-related design in the
            assignment.

        Notes:
            An info log is also output with details on the consultation in question.
        """

        healthcare_professional_log.info(
            "The healthcare professional '{}' conducts a consultation for the patient '{}' of the "
            "following type: '{}'.".format(self.name, patient_full_name, appointment_type)
        )

        return appointment_type
