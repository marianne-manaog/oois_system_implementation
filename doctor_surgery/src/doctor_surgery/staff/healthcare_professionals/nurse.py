# This Python file contains the definition of the class 'Nurse', which inherits the attributes and the methods of the
# class 'HealthcareProfessional'.

from healthcare_professional import HealthcareProfessional


class Nurse(HealthcareProfessional):

    def __init__(self, name, employee_number, appointments_list, patients_list):  # pragma: no cover
        # type: (str, str, List[Dict], List[Patient]) -> None
        HealthcareProfessional.__init__(self, name, employee_number, appointments_list, patients_list)

    def __str__(self):  # pragma: no cover
        return "<Nurse whose name is '{}' and employee number is '{}', with the list of appointments '{}' and " \
               "the list of patients '{}'>".format(self.name,
                                                   self.employee_number,
                                                   self.appointments_list,
                                                   self.patients_list)

    def __repr__(self):  # pragma: no cover
        return "Nurse: (name: {}, employee number: {}, appointments_list: {}, patients_list: {})".format(
            self.name, self.employee_number, self.appointments_list, self.patients_list
        )
