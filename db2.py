import sqlite3 #import sqlite
from hello import staff

#create connection
conn = sqlite3.connect('example2.db')

#create a cusor object and call its execute() method to perfom SQL commands
c = conn.cursor()

#create new table
c.execute('''CREATE TABLE IF NOT EXISTS staff_records (name text, age real, dept text, basic real)''')

#insert a row of data
c.execute("INSERT INTO staff_records VALUES ('staff.s1.name', 'staff.s1.age', 'staffs1.dept', 'staff.s1.basic')")

#save the changes (commit)
conn.commit()

for row in c.execute('SELECT * FROM staff_records'):
    print(row)

#close the connection when done
conn.close()