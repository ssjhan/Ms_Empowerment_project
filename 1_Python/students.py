import sqlite3

def create_table():
    connection = sqlite3.connect("students.db")
    cusor= connection.cursor()

    cusor.execute('''CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        major TEXT)''')

    connection.commit()
    connection.close()

create_table()

def insert_student(name, age, major):
    connection = sqlite3.connect("students.db")
    cusor= connection.cursor()

    cusor.execute('''INSERT INTO students (name, age, major) 
    VALUES(?,?,?)''', (name, age, major)
    )

    connection.commit()
    connection.close()

#insert_student("hi", 19, "programmer")


def query_student():
    connection = sqlite3.connect("students.db")
    cusor= connection.cursor()

    cusor.execute('''SELECT * FROM students''')
    rows = cusor.fetchall()

    connection.close()

    return rows

#print(query_student())   


def update_student(student_id, name, age, major):
     connection = sqlite3.connect("students.db")
     cusor= connection.cursor()

     cusor.execute('''UPDATE students SET name = ?, age =?, major = ? WHERE id = ?''',(name, age, major, student_id))

     connection.commit()
     connection.close()

#update_student(1, "hello", 22, "web programmer")
#print(query_student())


def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cusor= connection.cursor()
    
    cusor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    
    connection.commit()
    connection.close()

delete_student(2)
print(query_student())