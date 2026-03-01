# ==============================
# Hospital Management System
# ==============================

class Patient:
    def __init__(self, pid, name, age, gender, condition):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition


class Doctor:
    def __init__(self, did, name, age, gender, specialty):
        self.did = did
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = specialty


class Appointment:
    def __init__(self, aid, pid, did, date):
        self.aid = aid
        self.pid = pid
        self.did = did
        self.date = date


class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def load_patients(self, filename):
        with open(filename) as f:
            for line in f:
                pid, name, age, gender, condition = line.strip().split("|")
                self.patients[pid] = Patient(pid, name, age, gender, condition)

    def load_doctors(self, filename):
        with open(filename) as f:
            for line in f:
                did, name, age, gender, specialty = line.strip().split("|")
                self.doctors[did] = Doctor(did, name, age, gender, specialty)

    def load_appointments(self, filename):
        with open(filename) as f:
            for line in f:
                aid, pid, did, date = line.strip().split("|")
                self.appointments.append(Appointment(aid, pid, did, date))

    def show_appointments(self):
        print("\n===== Appointments =====\n")
        for a in self.appointments:
            p = self.patients[a.pid]
            d = self.doctors[a.did]

            print(f"Appointment ID: {a.aid}")
            print(f"Date       : {a.date}")
            print(f"Patient    : {p.name} ({p.condition})")
            print(f"Doctor     : {d.name} ({d.specialty})")
            print("-" * 40)


if __name__ == "__main__":
    hospital = HospitalSystem()
    hospital.load_patients("patients.txt")
    hospital.load_doctors("doctors.txt")
    hospital.load_appointments("appointments.txt")
    hospital.show_appointments()
