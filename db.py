import sqlite3 #import sqlite
from hello import staff

#create connection
conn = sqlite3.connect('example.db')

#create a cusor object and call its execute() method to perfom SQL commands
c = conn.cursor()

#create new table
c.execute('''CREATE TABLE IF NOT EXISTS stocks (date text, trans text, symbol text, qty real, price real)''')

#insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

#save the changes (commit)
conn.commit()

for row in c.execute('SELECT * FROM stocks'):
    print(row)

#close the connection when done
conn.close()