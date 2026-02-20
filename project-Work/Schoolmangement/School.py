import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hashlib
import os
from datetime import datetime

# ---------------- USER LOGIN DATA ---------------- #
USERS = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "teacher": hashlib.sha256("teacher123".encode()).hexdigest()
}

# ---------------- MAIN ERP CLASS ---------------- #
class SmartSchoolERP:

    def __init__(self, root, role):
        self.root = root
        self.role = role
        self.root.title(f"Smart School ERP - Logged in as {role}")
        self.root.geometry("1200x650")

        self.load_data()
        self.create_gui()

    # ---------------- DATA HANDLING ---------------- #
    def load_csv(self, file, columns):
        if os.path.exists(file):
            return pd.read_csv(file)
        return pd.DataFrame(columns=columns)

    def load_data(self):
        self.students = self.load_csv("students.csv",
                                      ["ID","Name","Class","Section","Maths","Science","English","Total","Grade"])
        self.teachers = self.load_csv("teachers.csv",
                                      ["ID","Name","Subject","Salary"])
        self.fees = self.load_csv("fees.csv",
                                  ["Receipt_ID","Student_ID","Amount","Date"])
        self.attendance = self.load_csv("attendance.csv",
                                        ["Student_ID","Date","Status"])

    def save_all(self):
        self.students.to_csv("students.csv", index=False)
        self.teachers.to_csv("teachers.csv", index=False)
        self.fees.to_csv("fees.csv", index=False)
        self.attendance.to_csv("attendance.csv", index=False)

    # ---------------- GRADE LOGIC ---------------- #
    def calculate_grade(self, total):
        if total >= 270: return "A"
        elif total >= 240: return "B"
        elif total >= 180: return "C"
        else: return "D"

    # ---------------- STUDENT MODULE ---------------- #
    def add_student(self):
        try:
            sid = self.sid.get()
            name = self.sname.get()
            cls = self.sclass.get()
            sec = self.ssection.get()
            maths = int(self.smaths.get())
            sci = int(self.sscience.get())
            eng = int(self.senglish.get())

            total = np.sum([maths, sci, eng])
            grade = self.calculate_grade(total)

            new = pd.DataFrame([[sid,name,cls,sec,maths,sci,eng,total,grade]],
                               columns=self.students.columns)

            self.students = pd.concat([self.students,new],ignore_index=True)
            self.save_all()
            self.refresh_students()
            messagebox.showinfo("Success","Student Added")

        except:
            messagebox.showerror("Error","Invalid Input")

    def refresh_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for _,row in self.students.iterrows():
            self.tree.insert("", "end", values=list(row))

    # ---------------- TEACHER MODULE ---------------- #
    def add_teacher(self):
        tid = self.tid.get()
        name = self.tname.get()
        subject = self.tsubject.get()
        salary = self.tsalary.get()

        new = pd.DataFrame([[tid,name,subject,salary]],
                           columns=self.teachers.columns)

        self.teachers = pd.concat([self.teachers,new],ignore_index=True)
        self.save_all()
        messagebox.showinfo("Success","Teacher Added")

    # ---------------- FEE MODULE ---------------- #
    def collect_fee(self):
        rid = self.rid.get()
        sid = self.fsid.get()
        amount = float(self.famount.get())
        date = datetime.now().strftime("%Y-%m-%d")

        new = pd.DataFrame([[rid,sid,amount,date]],
                           columns=self.fees.columns)

        self.fees = pd.concat([self.fees,new],ignore_index=True)
        self.save_all()
        messagebox.showinfo("Success","Fee Collected")

    # ---------------- ANALYTICS ---------------- #
    def show_dashboard(self):
        if self.students.empty:
            messagebox.showwarning("Warning","No Student Data")
            return

        totals = np.array(self.students["Total"].astype(int))
        avg = np.mean(totals)

        topper = self.students.loc[self.students["Total"].idxmax()]

        revenue = self.fees["Amount"].astype(float).sum()

        messagebox.showinfo("Dashboard",
                            f"Average Marks: {avg}\n"
                            f"Topper: {topper['Name']}\n"
                            f"Total Revenue: ₹{revenue}")

        # Chart
        plt.figure(figsize=(10,5))
        plt.bar(self.students["Name"], self.students["Total"])
        plt.xticks(rotation=45)
        plt.title("Student Performance")
        plt.tight_layout()
        plt.show()

    # ---------------- GUI ---------------- #
    def create_gui(self):

        frame1 = tk.LabelFrame(self.root, text="Add Student", padx=10, pady=10)
        frame1.place(x=20,y=20,width=350,height=300)

        labels = ["ID","Name","Class","Section","Maths","Science","English"]
        entries = []

        for i,l in enumerate(labels):
            tk.Label(frame1,text=l).grid(row=i,column=0)
            e = tk.Entry(frame1)
            e.grid(row=i,column=1)
            entries.append(e)

        self.sid,self.sname,self.sclass,self.ssection,\
        self.smaths,self.sscience,self.senglish = entries

        tk.Button(frame1,text="Add Student",command=self.add_student).grid(row=7,column=0,columnspan=2,pady=10)

        # Table
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"]=self.students.columns.tolist()
        self.tree.place(x=400,y=20,width=750,height=500)

        for col in self.students.columns:
            self.tree.heading(col,text=col)
            self.tree.column(col,width=80)

        self.refresh_students()

        # Dashboard Button
        tk.Button(self.root,text="Open Dashboard",
                  command=self.show_dashboard).place(x=150,y=350)

# ---------------- LOGIN WINDOW ---------------- #
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        tk.Label(root,text="Username").pack()
        self.username=tk.Entry(root)
        self.username.pack()

        tk.Label(root,text="Password").pack()
        self.password=tk.Entry(root,show="*")
        self.password.pack()

        tk.Button(root,text="Login",command=self.check_login).pack(pady=20)

    def check_login(self):
        user=self.username.get()
        pwd=hashlib.sha256(self.password.get().encode()).hexdigest()

        if user in USERS and USERS[user]==pwd:
            self.root.destroy()
            main_app(user)
        else:
            messagebox.showerror("Error","Invalid Login")

# ---------------- START ---------------- #
def main_app(role):
    root=tk.Tk()
    app=SmartSchoolERP(root,role)
    root.mainloop()

if __name__=="__main__":
    root=tk.Tk()
    LoginWindow(root)
    root.mainloop()
