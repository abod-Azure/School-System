"""
القسم 3: إدارة الدرجات (Grade Management)
المسؤول: الشخص الثالث
المهمة: وظائف إضافة وعرض الدرجات
"""

from part1_database import Database

class GradeManager:
    def __init__(self):
        self.db = Database()
    
    def add_grade(self, student_id, subject, grade):
        """إضافة درجة لطالب"""
        query = "INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)"
        self.db.execute_query(query, (student_id, subject, float(grade)))
        return True
    
    def get_all_grades(self):
        """الحصول على جميع الدرجات مع أسماء الطلاب"""
        query = """
            SELECT students.name, grades.subject, grades.grade, grades.id
            FROM grades
            JOIN students ON grades.student_id = students.id
        """
        return self.db.fetch_data(query)
    
    def get_student_grades(self, student_id):
        """الحصول على درجات طالب معين"""
        query = """
            SELECT subject, grade
            FROM grades
            WHERE student_id = ?
        """
        return self.db.fetch_data(query, (student_id,))
    
    def get_student_average(self, student_id):
        """حساب معدل الطالب"""
        query = "SELECT AVG(grade) FROM grades WHERE student_id = ?"
        result = self.db.fetch_data(query, (student_id,))
        return result[0][0] if result and result[0][0] else 0
    
    def delete_grade(self, grade_id):
        """حذف درجة"""
        query = "DELETE FROM grades WHERE id = ?"
        self.db.execute_query(query, (grade_id,))
        return True
    
    def update_grade(self, grade_id, new_grade):
        """تحديث درجة"""
        query = "UPDATE grades SET grade = ? WHERE id = ?"
        self.db.execute_query(query, (float(new_grade), grade_id))
        return True
    
    def get_subject_grades(self, subject):
        """الحصول على درجات مادة معينة"""
        query = """
            SELECT students.name, grades.grade
            FROM grades
            JOIN students ON grades.student_id = students.id
            WHERE grades.subject = ?
        """
        return self.db.fetch_data(query, (subject,))
