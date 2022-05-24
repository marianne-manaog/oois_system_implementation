# This Python file is used to run the 'doctor_surgery' application.

from appointments.appointment_schedule import AppointmentSchedule

from doctor_surgery.src.doctor_surgery.utils_validation import validate_int_input, validate_str_input

from patients.patient import Patient
from prescriptions.prescription import Prescription

from staff.administrative_professionals.receptionist import Receptionist
from staff.healthcare_professionals.doctor import Doctor

from doctor_surgery.src.doctor_surgery.utils import print_name_strings_from_list

from doctor_surgery.src.doctor_surgery.constants import (
    DOCTOR_W_PLACEHOLDER,
    DRUG_W_PLACEHOLDER,
    PATIENT_W_PLACEHOLDER,
    FIRST_DUMMY_DOCTOR,
    FIRST_DUMMY_PATIENT,
    LOG_IN_MSG,
    MAXIMUM_NUM_OF_PATIENTS_PER_DOCTOR,
    RECEPTIONIST_EMPLOYEE_NUMBER,
    RECEPTIONIST_NAME,
    SECOND_DUMMY_DOCTOR,
    SECOND_DUMMY_PATIENT
)

appointment_schedule = AppointmentSchedule()
patients_list = []

# Define a list of two dummy doctors to initialise the application
doctor_1 = Doctor(
    name=FIRST_DUMMY_DOCTOR,
    employee_number="90210",
    appointments_list=appointment_schedule,
    patients_list=patients_list
)
doctor_2 = Doctor(
    name=SECOND_DUMMY_DOCTOR,
    employee_number="88388",
    appointments_list=appointment_schedule,
    patients_list=patients_list
)
doctors_list = [{'doctor_1': doctor_1}, {'doctor_2': doctor_2}]

# Define a list of two dummy patients to initialise the application
list_of_prescriptions = []

patient_1 = Patient(
    name=FIRST_DUMMY_PATIENT,
    address="1630 Revello Drive",
    phone="0123456789",
    registered_doctor=doctor_1,
    list_of_prescriptions=list_of_prescriptions
)
patient_2 = Patient(
    name=SECOND_DUMMY_PATIENT,
    address="The Sky",
    phone="1329 Prescott Street",
    registered_doctor=doctor_2,
    list_of_prescriptions=list_of_prescriptions
)
patients_list = [{'patient_1': patient_1}, {'patient_2': patient_2}]

# Assign two dummy drugs as prescribed for the dummy patient no. 1
drug_1 = Prescription(
    prescription_type="Bellpepperidone", patient=patient_1, quantity=10, dosage=149.5, doctor=doctor_1
)
drug_2 = Prescription(
    prescription_type="Auberginixine", patient=patient_1, quantity=5, dosage=295.6, doctor=doctor_1
)
patient_1.list_of_prescriptions = [{'drug_1': drug_1}, {'drug_2': drug_2}]

# Assign two dummy drugs as prescribed for the dummy patient no. 2
drug_3 = Prescription(
    prescription_type="Tomatocillin", patient=patient_2, quantity=4, dosage=80., doctor=doctor_1
)
drug_4 = Prescription(
    prescription_type="Broccopril", patient=patient_2, quantity=10, dosage=197.7, doctor=doctor_2
)
patient_2.list_of_prescriptions = [{'drug_3': drug_3}, {'drug_4': drug_4}]

# Create a dummy receptionist object
receptionist = Receptionist(name=RECEPTIONIST_NAME, employee_number=RECEPTIONIST_EMPLOYEE_NUMBER)

print("The 'doctor_surgery' app is running...")


def landing_options():
    # type: () -> None
    """This function enables to run the entire 'doctor_surgery' application"""

    print("""Please select one of the following numbers and press 'Enter' on your keyboard:
                1 - to add a new patient
                2 - if you are a patient
                3 - if you are a healthcare professional""")

    role = validate_int_input()

    # Option 1 to add a new patient
    if role == 1:
        name = str(raw_input("Please type your full name: "))
        address = str(raw_input("Please type your full address: "))
        phone = str(raw_input("Please type your mobile number: "))

        print("Please select one of the following doctors to be registered with.")
        print_name_strings_from_list(list_of_dicts=doctors_list, prefix_str=DOCTOR_W_PLACEHOLDER)

        doctor_str_validated = validate_str_input()
        for doct in doctors_list:
            doctor_name = doct[next(iter(doct))].name
            if doctor_str_validated == doctor_name:
                selected_doctor = doct[next(iter(doct))]
                print "The doctor you selected is '{}'.".format(doctor_name)
                if len(selected_doctor.patients_list) <= MAXIMUM_NUM_OF_PATIENTS_PER_DOCTOR:
                    list_of_existing_patients = []
                    for j in range(len(patients_list)):
                        list_of_existing_patients.append(patients_list[j].values()[0].name)
                    if name not in list_of_existing_patients:
                        new_patient = Patient(
                            name=name,
                            address=address,
                            phone=phone,
                            registered_doctor=selected_doctor,
                            list_of_prescriptions=list_of_prescriptions
                        )
                        index_iter = len(list_of_existing_patients) + 1
                        patient_index_string = PATIENT_W_PLACEHOLDER.format(index_iter)
                        patients_list.append({patient_index_string: new_patient})
                        selected_doctor.patients_list = patients_list
                        print(
                            "The following patient has been registered successfully: '{}'."
                        ).format(
                            patients_list[len(patients_list) - 1].get(patient_index_string).name
                        )
                        landing_options()
                    else:
                        print("The patient '{}' already exists in the system; thus, they cannot be "
                              "registered again.").format(name)
                        landing_options()
                else:
                    print("Apologies; the selected doctor '{}' is not available. "
                          "Please select another doctor.").format(doctor_name)
                    landing_options()
            else:
                print("The name you typed '{}' does not match that of an existing doctor in the system; please "
                      "try typing it again.").format(doctor_str_validated)
                landing_options()
        landing_options()

    # Option 2 if a patient were using the application
    elif role == 2:
        print(LOG_IN_MSG)
        print_name_strings_from_list(list_of_dicts=patients_list, prefix_str=PATIENT_W_PLACEHOLDER)

        patient_str_validated = validate_str_input()
        list_of_existing_patients = []
        for j in range(len(patients_list)):
            list_of_existing_patients.append(patients_list[j].values()[0].name)
        if patient_str_validated in list_of_existing_patients:
            index_iteration = 0
            for patie in patients_list:
                index_iteration += 1
                patient_index_string = PATIENT_W_PLACEHOLDER.format(index_iteration)
                if patient_str_validated == patie.get(patient_index_string).name:
                    current_patient = patie.get(patient_index_string)
                    patient_selections(current_patient)
        else:
            print("The patient's name you entered '{}' is not recognised. "
                  "Please make sure it is correct and retry.").format(patient_str_validated)
            landing_options()

    # Option 3 if a doctor were using the application
    elif role == 3:
        print(LOG_IN_MSG)
        print_name_strings_from_list(list_of_dicts=doctors_list, prefix_str=DOCTOR_W_PLACEHOLDER)

        doct_str_validated = validate_str_input()
        for doct in doctors_list:
            doctor_name = doct[next(iter(doct))].name
            if doct_str_validated == doctor_name:
                selected_doctor = doct[next(iter(doct))]
                doctor_selections(selected_doctor)
            else:
                print("The name you typed '{}' does not match that of an existing doctor in the system; please "
                      "try typing it again.").format(doct_str_validated)
                landing_options()


def patient_selections(patient):
    # type: (Patient) -> None
    """This function enables a patient to use the 'doctor_surgery' application"""

    print('''You have successfully logged in.

        Please select one of the following options to continue:
        1. Check your current prescriptions.
        2. Schedule your appointment.
        3. Cancel your appointment.
        4. Go back to the main options.''')

    selection_int = validate_int_input()

    # Check current prescriptions
    if selection_int == 1:
        if patient.list_of_prescriptions:
            iter_index = 0
            for i in patient.list_of_prescriptions:
                iter_index += 1
                drug_string = DRUG_W_PLACEHOLDER.format(iter_index)
                print "There are {} repeat prescriptions left for the drug '{}'.".format(
                    i.get(drug_string).quantity,
                    i.get(drug_string).prescription_type
                )
            print('''Please select one of the following options:
                1. Select one of the prescribed drugs to order.
                2. Go back to the previous options.
                3. Go back to the main options.''')

            int_input = validate_int_input()

            if int_input == 1:
                print("Please type the name of the prescribed drug you wish to order.")
                str_input = validate_str_input()
                drug_string, prescription = patient.request_repeat_prescription(str_input)
                if len(patient.list_of_prescriptions) > 0:
                    being_verb_string = ''
                    prescription_string = ''
                    if prescription.get(drug_string).quantity > 1:
                        being_verb_string = 'are'
                        prescription_string = 'prescriptions'
                    elif prescription.get(drug_string).quantity == 1:
                        being_verb_string = 'is'
                        prescription_string = 'prescription'
                    elif prescription.get(drug_string).quantity == 0:
                        print("Please note this was your last prescription of '{}' available; "
                              "if you wish to order any further ones, "
                              "please see your doctor '{}'.").format(
                            prescription.get(drug_string).prescription_type,
                            patient.registered_doctor.name)
                        patient_selections(patient)
                    print "There {} {} remaining repeat {} of '{}'.".format(
                        being_verb_string,
                        prescription.get(drug_string).quantity,
                        prescription_string,
                        prescription.get(drug_string).prescription_type)
                    patient_selections(patient)
                elif prescription.get(drug_string).quantity == 0:
                    print("There are no further prescriptions of '{}' available; "
                          "should you wish to order additional ones, "
                          "please contact your doctor '{}'.").format(
                        prescription.get(drug_string).prescription_type,
                        patient.registered_doctor.name)
                    patient_selections(patient)
                else:
                    print("There are no prescriptions available; "
                          "should you wish to order any, "
                          "please contact your doctor '{}'.").format(patient.registered_doctor.name)

            elif int_input == 2:
                patient_selections(patient)

            elif int_input == 3:
                landing_options()

        else:
            print("There are no prescriptions assigned to you.")
            patient_selections(patient)

    # Schedule appointments
    elif selection_int == 2:
        next_available_appointments = patient.registered_doctor.appointments_list.find_next_available_appointments()
        for i in next_available_appointments:
            print '{}'.format(i.get('time'))

        str_input = validate_str_input()
        for next_available_appointment in next_available_appointments:
            if str_input == next_available_appointment.get('time'):
                patient.request_appointment(next_available_appointment.get('time'))
                print("An appointment has been successfully booked "
                      "at the following time: '{}'.").format(next_available_appointment.get('time'))
                patient_selections(patient)
        print("The time you selected '{}' is not available. "
              "Please select one of the times shown instead.").format(str_input)
        patient_selections(patient)

    # Cancel appointments
    elif selection_int == 3:
        appointments_list_of_dicts = patient.registered_doctor.appointments_list
        list_of_all_appts_assigned = []
        for i in range(len(appointments_list_of_dicts.appointments)):
            if patient.name == appointments_list_of_dicts.appointments[i].get('patient_full_name'):
                list_of_all_appts_assigned.append(appointments_list_of_dicts.appointments[i])
        if list_of_all_appts_assigned:
            appt_str = ''
            have_verb = ''
            if len(list_of_all_appts_assigned) > 1:
                appt_str = 'appointments'
                have_verb = 'have'
            elif len(list_of_all_appts_assigned) == 1:
                appt_str = 'appointment'
                have_verb = 'has'
            print 'The following {} {} been previously scheduled: '.format(appt_str, have_verb)
            for appt_assigned in list_of_all_appts_assigned:
                print '{}'.format(appt_assigned.get('time'))
            print("Please type the time (e.g., 09:00) of the appointment to cancel.")

            chosen_time = validate_str_input()
            for appt_assigned in list_of_all_appts_assigned:
                if chosen_time == appt_assigned.get('time'):
                    receptionist.cancel_appointment(patient.registered_doctor, appt_assigned)
                    print("Your appointment has been cancelled.")
                    patient_selections(patient)
                else:
                    print("The time you entered '{}' does not match any existing appointments. "
                          "Please select one of the existing appointments to cancel.").format(chosen_time)
                    patient_selections(patient)
        else:
            print("There are no appointments booked.")
            patient_selections(patient)

    # Go back to the main options
    elif selection_int == 4:
        landing_options()

    else:
        print("The option you selected '{}' is invalid; "
              "please type one of the suggested ones and retry.").format(selection_int)
        patient_selections(patient)


def doctor_selections(doctor):
    # type: (Doctor) -> None
    """This function enables a doctor to use the 'doctor_surgery' application"""

    print('''You have successfully logged in. 
        
        Please select one of the following options:
        1. Check your upcoming appointments.
        2. Issue a prescription.
        3. Go back to the main options.''')

    int_input = validate_int_input()

    # Check upcoming appointments
    if int_input == 1:
        print(doctor.appointments_list)
        doctor_selections(doctor)

    # Issue prescriptions
    elif int_input == 2:
        print("Please select one of the following patients to issue a prescription: ")
        patients_lista = []
        for patien in patients_list:
            patients_lista.append(patien)
        doctor.patients_list = patients_lista
        print_name_strings_from_list(list_of_dicts=patients_lista, prefix_str=PATIENT_W_PLACEHOLDER)

        str_input = validate_str_input()
        for patient in patients_lista:
            patient_name = patient[next(iter(patient))].name
            if str_input == patient_name:
                selected_patient = patient[next(iter(patient))]
                doctor.issue_prescription(selected_patient)
                doctor_selections(doctor)

        print("The patient's name you entered ('{}') is invalid; please ensure it is correct and "
              "try typing it again.").format(str_input)
        
        doctor_selections(doctor)

    elif int_input == 3:
        landing_options()

    else:
        print("The option you selected '{}' is invalid; "
              "please type one of the suggested ones and retry.").format(int_input)
        landing_options()


landing_options()
