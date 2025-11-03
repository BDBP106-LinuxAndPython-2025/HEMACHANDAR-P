#!/usr/bin/python3

import sqlite3
import pandas as pd

# ----------------------------- #
# (1) SQLite Exercises
# ----------------------------- #

def create_database():
    conn = sqlite3.connect("IBABEmployee.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Employee (
                    ID INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    research_area TEXT,
                    designation TEXT,
                    gender TEXT
                )''')
    conn.commit()
    conn.close()
    print("Database and table created successfully!\n")

def add_records():
    conn = sqlite3.connect("IBABEmployee.db")
    cur = conn.cursor()

    while True:
        name = input("Enter employee name: ")
        research_area = input("Enter research area: ")
        designation = input("Enter designation: ")
        gender = input("Enter gender: ")

        cur.execute("INSERT INTO Employee (name, research_area, designation, gender) VALUES (?, ?, ?, ?)",
                    (name, research_area, designation, gender))
        conn.commit()

        more = input("Add another record? (y/n): ").lower()
        if more != 'y':
            break
    conn.close()

def edit_entry():
    conn = sqlite3.connect("IBABEmployee.db")
    cur = conn.cursor()

    emp_id = input("Enter ID of employee to edit: ")
    name = input("Enter new name: ")
    research_area = input("Enter new research area: ")
    designation = input("Enter new designation: ")
    gender = input("Enter new gender: ")

    cur.execute("""UPDATE Employee 
                   SET name=?, research_area=?, designation=?, gender=?
                   WHERE ID=?""", (name, research_area, designation, gender, emp_id))
    conn.commit()
    conn.close()
    print("Employee details updated!\n")

def delete_records():
    conn = sqlite3.connect("IBABEmployee.db")
    cur = conn.cursor()

    ids = input("Enter IDs to delete (space separated): ").split()
    cur.executemany("DELETE FROM Employee WHERE ID=?", [(i,) for i in ids])
    conn.commit()
    conn.close()
    print("Selected records deleted!\n")

def display_records():
    conn = sqlite3.connect("IBABEmployee.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()

    print("\n--- Employee Records ---")
    print("{:<5} {:<20} {:<20} {:<15} {:<10}".format("ID", "Name", "Research Area", "Designation", "Gender"))
    print("-" * 70)
    for row in rows:
        print("{:<5} {:<20} {:<20} {:<15} {:<10}".format(*row))
    conn.close()