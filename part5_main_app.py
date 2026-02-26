"""
القسم 5: البرنامج الرئيسي (Main Application)
المسؤول: الشخص الخامس
المهمة: تجميع كل الأقسام وإنشاء الواجهة الرئيسية
"""

import tkinter as tk
from tkinter import ttk
from part2_student_manager import StudentManager
from part3_grade_manager import GradeManager
from part4_gui_windows import GUIWindows

class SchoolSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("900x650")
        
        self.student_manager = StudentManager()
        self.grade_manager = GradeManager()
        self.gui_windows = GUIWindows(root)
        
        self.create_main_interface()
    
    def create_main_interface(self):
        """إنشاء الواجهة الرئيسية"""
        # عنوان رئيسي
        title_label = tk.Label(self.root, text="School Management System",
                              font=("Arial", 22, "bold"), bg="#4CAF50", fg="white", pady=15)
        title_label.pack(fill=tk.X)
        
        # إطار الأزرار
        button_frame = tk.Frame(self.root, bg="#f0f0f0", pady=20)
        button_frame.pack(fill=tk.X)
        
        # أزرار القوائم
        btn_add_student = tk.Button(button_frame, text="Add Student",
                                    command=self.gui_windows.add_student_window,
                                    bg="#2196F3", fg="white", width=18, height=2,
                                    font=("Arial", 11, "bold"))
        btn_add_student.grid(row=0, column=0, padx=10, pady=10)
        
        btn_add_grade = tk.Button(button_frame, text="Add Grade",
                                 command=self.gui_windows.add_grade_window,
                                 bg="#FF9800", fg="white", width=18, height=2,
                                 font=("Arial", 11, "bold"))
        btn_add_grade.grid(row=0, column=1, padx=10, pady=10)
        
        btn_view_students = tk.Button(button_frame, text="View Students",
                                      command=self.view_students,
                                      bg="#9C27B0", fg="white", width=18, height=2,
                                      font=("Arial", 11, "bold"))
        btn_view_students.grid(row=1, column=0, padx=10, pady=10)
        
        btn_view_grades = tk.Button(button_frame, text="View Grades",
                                    command=self.view_grades,
                                    bg="#E91E63", fg="white", width=18, height=2,
                                    font=("Arial", 11, "bold"))
        btn_view_grades.grid(row=1, column=1, padx=10, pady=10)
        
        btn_refresh = tk.Button(button_frame, text="Refresh",
                               command=self.refresh_display,
                               bg="#607D8B", fg="white", width=18, height=2,
                               font=("Arial", 11, "bold"))
        btn_refresh.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # إطار العرض
        self.display_frame = tk.Frame(self.root, bg="white")
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # عرض رسالة ترحيب
        welcome_label = tk.Label(self.display_frame,
                                text="Welcome to School Management System\n\nSelect an option from above",
                                font=("Arial", 16), bg="white", fg="#555")
        welcome_label.pack(pady=50)
    
    def view_students(self):
        """عرض قائمة الطلاب"""
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.display_frame, text="Students List",
                font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        # إنشاء جدول
        tree = ttk.Treeview(self.display_frame, columns=("ID", "Name", "Age", "Class"),
                           show="headings", height=18)
        
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Class", text="Class")
        
        tree.column("ID", width=80, anchor="center")
        tree.column("Name", width=250)
        tree.column("Age", width=100, anchor="center")
        tree.column("Class", width=150, anchor="center")
        
        # جلب البيانات
        students = self.student_manager.get_all_students()
        
        for student in students:
            tree.insert("", tk.END, values=student)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.display_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def view_grades(self):
        """عرض الدرجات"""
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.display_frame, text="Grades & Results",
                font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        # إنشاء جدول
        tree = ttk.Treeview(self.display_frame,
                           columns=("Student", "Subject", "Grade", "ID"),
                           show="headings", height=18)
        
        tree.heading("Student", text="Student Name")
        tree.heading("Subject", text="Subject")
        tree.heading("Grade", text="Grade")
        tree.heading("ID", text="Grade ID")
        
        tree.column("Student", width=300)
        tree.column("Subject", width=200)
        tree.column("Grade", width=100, anchor="center")
        tree.column("ID", width=80, anchor="center")
        
        # جلب البيانات
        grades = self.grade_manager.get_all_grades()
        
        for grade in grades:
            tree.insert("", tk.END, values=grade)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.display_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def refresh_display(self):
        """تحديث العرض"""
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        
        welcome_label = tk.Label(self.display_frame,
                                text="Data Refreshed!\n\nSelect an option to view data",
                                font=("Arial", 16), bg="white", fg="#555")
        welcome_label.pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolSystem(root)
    root.mainloop()
