"""
القسم 4: نوافذ الواجهة (GUI Windows)
المسؤول: الشخص الرابع
المهمة: إنشاء النوافذ المنبثقة لإدخال البيانات
"""

import tkinter as tk
from tkinter import ttk, messagebox
from part2_student_manager import StudentManager
from part3_grade_manager import GradeManager

class GUIWindows:
    def __init__(self, parent):
        self.parent = parent
        self.student_manager = StudentManager()
        self.grade_manager = GradeManager()
    
    def add_student_window(self):
        """نافذة إضافة طالب جديد"""
        window = tk.Toplevel(self.parent)
        window.title("Add New Student")
        window.geometry("400x300")
        
        tk.Label(window, text="Student Name:", font=("Arial", 12)).pack(pady=10)
        name_entry = tk.Entry(window, font=("Arial", 12), width=30)
        name_entry.pack(pady=5)
        
        tk.Label(window, text="Age:", font=("Arial", 12)).pack(pady=10)
        age_entry = tk.Entry(window, font=("Arial", 12), width=30)
        age_entry.pack(pady=5)
        
        tk.Label(window, text="Class:", font=("Arial", 12)).pack(pady=10)
        class_entry = tk.Entry(window, font=("Arial", 12), width=30)
        class_entry.pack(pady=5)
        
        def save_student():
            name = name_entry.get()
            age = age_entry.get()
            class_name = class_entry.get()
            
            if not name or not age or not class_name:
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            try:
                self.student_manager.add_student(name, age, class_name)
                messagebox.showinfo("Success", "Student added successfully")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(window, text="Save", command=save_student,
                 bg="#4CAF50", fg="white", width=15, height=2).pack(pady=20)
    
    def add_grade_window(self):
        """نافذة إضافة درجة"""
        window = tk.Toplevel(self.parent)
        window.title("Add Grade")
        window.geometry("400x350")
        
        students = self.student_manager.get_all_students()
        
        if not students:
            messagebox.showwarning("Warning", "No students registered")
            window.destroy()
            return
        
        tk.Label(window, text="Select Student:", font=("Arial", 12)).pack(pady=10)
        student_var = tk.StringVar()
        student_combo = ttk.Combobox(window, textvariable=student_var,
                                    values=[f"{s[0]} - {s[1]}" for s in students],
                                    font=("Arial", 10), width=30)
        student_combo.pack(pady=5)
        
        tk.Label(window, text="Subject:", font=("Arial", 12)).pack(pady=10)
        subject_entry = tk.Entry(window, font=("Arial", 12), width=30)
        subject_entry.pack(pady=5)
        
        tk.Label(window, text="Grade:", font=("Arial", 12)).pack(pady=10)
        grade_entry = tk.Entry(window, font=("Arial", 12), width=30)
        grade_entry.pack(pady=5)
        
        def save_grade():
            student_selection = student_var.get()
            subject = subject_entry.get()
            grade = grade_entry.get()
            
            if not student_selection or not subject or not grade:
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            try:
                student_id = int(student_selection.split(" - ")[0])
                self.grade_manager.add_grade(student_id, subject, grade)
                messagebox.showinfo("Success", "Grade added successfully")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(window, text="Save", command=save_grade,
                 bg="#4CAF50", fg="white", width=15, height=2).pack(pady=20)
