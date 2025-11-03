import sqlite3

# ----------------------------
# (i) Create database and table
# ----------------------------
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
''')

# ----------------------------
# (ii) Insert records
# ----------------------------
students_data = [
    (1, 'Ravi', 'Math', 85),
    (2, 'Meena', 'Science', 90),
    (3, 'Arjun', 'English', 78),
    (4, 'Priya', 'Math', 92),
    (5, 'Suresh', 'Science', 65)
]

cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)', students_data)
conn.commit()

print("✅ Database and table created, records inserted successfully!")

# ----------------------------
# (iii) SQL Queries
# ----------------------------

print("\n(a) All records:")
for row in cursor.execute('SELECT * FROM students'):
    print(row)

print("\n(b) Students who scored above 80:")
for row in cursor.execute('SELECT name, marks FROM students WHERE marks > 80'):
    print(row)

print("\n(c) Average marks in each subject:")
for row in cursor.execute('SELECT subject, AVG(marks) AS average FROM students GROUP BY subject'):
    print(row)

# ----------------------------
# (iv) Update Suresh's marks
# ----------------------------
cursor.execute("UPDATE students SET marks = 75 WHERE name = 'Suresh'")
conn.commit()
print("\n✅ Updated Suresh's marks to 75")

# ----------------------------
# (v) Delete lowest marks in English
# ----------------------------
cursor.execute('''
DELETE FROM students
WHERE subject = 'English' 
AND marks = (SELECT MIN(marks) FROM students WHERE subject = 'English')
''')
conn.commit()
print("✅ Deleted student with lowest marks in English")

# ----------------------------
# (vi) Add grade column and assign grades
# ----------------------------
cursor.execute("ALTER TABLE students ADD COLUMN grade TEXT")

# Assign grades based on marks
cursor.execute("UPDATE students SET grade = 'A' WHERE marks >= 85")
cursor.execute("UPDATE students SET grade = 'B' WHERE marks BETWEEN 70 AND 84")
cursor.execute("UPDATE students SET grade = 'C' WHERE marks < 70")
conn.commit()

print("\n✅ Grade column added and updated!")

# Display final table
print("\nFinal table contents:")
for row in cursor.execute('SELECT * FROM students'):
    print(row)

# Close connection
conn.close()
