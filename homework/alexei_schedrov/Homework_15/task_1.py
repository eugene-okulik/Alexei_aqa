import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Billy', 'Baggins')
cursor.execute(query, values)
db.commit()
print(student_id := cursor.lastrowid)

query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [
    ('Windows 98 v2', student_id),
    ('Windows NT for dummies', student_id),
    ('Windows 7 for geeks', student_id)
]
cursor.executemany(query, values)
db.commit()

query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values = ('Rich people', 'mar 2025', 'mar 2037')
cursor.execute(query, values)
db.commit()
print(group_id := cursor.lastrowid)

query = 'UPDATE students SET group_id = %s WHERE id= %s'
cursor.execute(query, (group_id, student_id))
db.commit()

subject_ids = []
values = [
    ('Piano'),
    ('Lirycs'),
    ('Geometry'),
    ('Poetry')
]

for value in values:
    query = 'INSERT INTO subjets (title) VALUES (%s)'
    cursor.execute(query, (value,))
    db.commit()
    subject_ids.append(cursor.lastrowid)

print("subject_ids", subject_ids)

lesson_ids = []
values = [
    ('Piano_lesson', subject_ids[0]),
    ('Piano_lesson', subject_ids[0]),
    ('Lirycs_lesson', subject_ids[1]),
    ('Lirycs_lesson', subject_ids[1]),
    ('Geometry_lesson', subject_ids[2]),
    ('Geometry_lesson', subject_ids[2]),
    ('Poetry_lesson', subject_ids[3]),
    ('Poetry_lesson', subject_ids[3])
]
for value in values:
    query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    cursor.execute(query, value)
    db.commit()
    lesson_ids.append(cursor.lastrowid)
print("lesson_ids", lesson_ids)

query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values = [
    (5, lesson_ids[0], student_id),
    (6, lesson_ids[1], student_id),
    (10, lesson_ids[2], student_id),
    (8, lesson_ids[3], student_id),
    (8, lesson_ids[4], student_id),
    (7, lesson_ids[5], student_id),
    (10, lesson_ids[6], student_id),
    (8, lesson_ids[7], student_id)
]
cursor.executemany(query, values)
db.commit()

# Получаем итоговые данные
# Все оценки студента
query = 'SELECT value FROM marks WHERE student_id = %s'
cursor.execute(query, (student_id,))
rows = cursor.fetchall()
print("Students marks are :")
for row in rows:
    print(row)

# Все Все книги, которые находятся у студента
query = 'SELECT title from books WHERE taken_by_student_id = %s'
cursor.execute(query, (student_id,))
rows = cursor.fetchall()
print("Students taken books are :")
for row in rows:
    print(row)

# Вся информация про студента
query = '''SELECT
    s.name AS student_name,
    s.second_name AS student_second_name,
    g.title,
    (SELECT GROUP_CONCAT(DISTINCT b.title SEPARATOR ', ')
     FROM books b
     WHERE b.taken_by_student_id = s.id) AS books,
    m.value,
    l.id,
    sub.title
FROM
    students s
JOIN
    `groups` g ON s.group_id = g.id
LEFT JOIN
    marks m ON s.id = m.student_id
LEFT JOIN
    lessons l ON m.lesson_id = l.id
LEFT JOIN
    subjets sub ON l.subject_id = sub.id
WHERE
    s.id = %s'''
cursor.execute(query, (student_id,))
print("All info about student :")
while True:
    rows = cursor.fetchmany(size=3)
    if not rows:
        break
    for row in rows:
        print(row)

db.close()
