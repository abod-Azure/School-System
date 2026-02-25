"""
القسم 1: قاعدة البيانات (Database Module)
المسؤول: الشخص احمد العلو
المهمة: إدارة قاعدة البيانات والجداول
"""

import sqlite3

class Database:
    def __init__(self, db_name='school.db'):
        self.db_name = db_name
        self.create_tables()
    
    def get_connection(self):
        """إنشاء اتصال بقاعدة البيانات"""
        return sqlite3.connect(self.db_name)
    
    def create_tables(self):
        """إنشاء الجداول الأساسية"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # جدول الطلاب
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                class TEXT
            )
        ''')
        
        # جدول الدرجات
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject TEXT,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def execute_query(self, query, params=()):
        """تنفيذ استعلام SQL"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
    
    def fetch_data(self, query, params=()):
        """جلب البيانات من قاعدة البيانات"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        conn.close()
        return data
