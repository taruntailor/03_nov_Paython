import pandas as pd
import numpy as np
import os
from datetime import datetime

class HospitalManagementSystem:

    def __init__(self):
        self.load_data()

    # ---------------- LOAD / SAVE ---------------- #
    def load_data(self):
        self.patients = self.load_csv("patients.csv", 
                                      ["Patient_ID", "Name", "Age", "Gender", "Disease"])
        self.doctors = self.load_csv("doctors.csv", 
                                     ["Doctor_ID", "Name", "Specialization", "Consultation_Fee"])
        self.appointments = self.load_csv("appointments.csv", 
                                          ["Appointment_ID", "Patient_ID", "Doctor_ID", "Date"])
        self.billing = self.load_csv("billing.csv", 
                                     ["Bill_ID", "Patient_ID", "Doctor_ID", "Medicine_Cost", "Total_Bill", "Date"])

    def load_csv(self, file, columns):
        if os.path.exists(file):
            return pd.read_csv(file)
        else:
            return pd.DataFrame(columns=columns)

    def save_data(self):
        self.patients.to_csv("patients.csv", index=False)
        self.doctors.to_csv("doctors.csv", index=False)
        self.appointments.to_csv("appointments.csv", index=False)
        self.billing.to_csv("billing.csv", index=False)

    # ---------------- PATIENT ---------------- #
    def add_patient(self, pid, name, age, gender, disease):
        if pid in self.patients["Patient_ID"].values:
            print("Patient ID already exists!")
            return

        new = pd.DataFrame([[pid, name, age, gender, disease]],
                           columns=self.patients.columns)
        self.patients = pd.concat([self.patients, new], ignore_index=True)
        self.save_data()
        print("Patient Added Successfully!")

    # ---------------- DOCTOR ---------------- #
    def add_doctor(self, did, name, specialization, fee):
        new = pd.DataFrame([[did, name, specialization, fee]],
                           columns=self.doctors.columns)
        self.doctors = pd.concat([self.doctors, new], ignore_index=True)
        self.save_data()
        print("Doctor Added Successfully!")

    # ---------------- APPOINTMENT ---------------- #
    def book_appointment(self, aid, pid, did):
        date = datetime.now().strftime("%Y-%m-%d")

        new = pd.DataFrame([[aid, pid, did, date]],
                           columns=self.appointments.columns)
        self.appointments = pd.concat([self.appointments, new], ignore_index=True)
        self.save_data()
        print("Appointment Booked!")

    # ---------------- BILLING ---------------- #
    def generate_bill(self, bid, pid, did, medicine_cost):
        doctor = self.doctors[self.doctors["Doctor_ID"] == did]

        if doctor.empty:
            print("Doctor not found!")
            return

        consultation_fee = float(doctor["Consultation_Fee"].values[0])

        total = np.sum(np.array([consultation_fee, medicine_cost]))
        date = datetime.now().strftime("%Y-%m-%d")

        new = pd.DataFrame([[bid, pid, did, medicine_cost, total, date]],
                           columns=self.billing.columns)

        self.billing = pd.concat([self.billing, new], ignore_index=True)
        self.save_data()
        print(f"Bill Generated! Total = {total}")

    # ---------------- ANALYTICS ---------------- #
    def analytics_dashboard(self):
        print("\n📊 HOSPITAL ANALYTICS DASHBOARD")

        if self.billing.empty:
            print("No billing data available.")
            return

        total_revenue = self.billing["Total_Bill"].astype(float).sum()
        avg_bill = self.billing["Total_Bill"].astype(float).mean()

        print(f"Total Revenue: ₹{total_revenue}")
        print(f"Average Bill Value: ₹{avg_bill}")

        # Doctor-wise revenue
        doctor_revenue = self.billing.groupby("Doctor_ID")["Total_Bill"].sum()
        print("\nDoctor Wise Revenue:")
        print(doctor_revenue)

        # Most frequent disease
        if not self.patients.empty:
            print("\nMost Common Disease:")
            print(self.patients["Disease"].value_counts().head(1))

        # Age statistics using NumPy
        if not self.patients.empty:
            ages = np.array(self.patients["Age"].astype(int))
            print("\nPatient Age Statistics:")
            print("Average Age:", np.mean(ages))
            print("Minimum Age:", np.min(ages))
            print("Maximum Age:", np.max(ages))


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    hms = HospitalManagementSystem()

    while True:
        print("\n===== HOSPITAL SYSTEM =====")
        print("1 Add Patient")
        print("2 Add Doctor")
        print("3 Book Appointment")
        print("4 Generate Bill")
        print("5 Analytics Dashboard")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            hms.add_patient(input("ID: "), input("Name: "), 
                            int(input("Age: ")), input("Gender: "), input("Disease: "))

        elif choice == "2":
            hms.add_doctor(input("ID: "), input("Name: "),
                           input("Specialization: "), float(input("Fee: ")))

        elif choice == "3":
            hms.book_appointment(input("Appointment ID: "),
                                 input("Patient ID: "),
                                 input("Doctor ID: "))

        elif choice == "4":
            hms.generate_bill(input("Bill ID: "),
                              input("Patient ID: "),
                              input("Doctor ID: "),
                              float(input("Medicine Cost: ")))

        elif choice == "5":
            hms.analytics_dashboard()

        elif choice == "6":
            break

        else:
            print("Invalid Choice!")
