#Task 2 Chapter 17

#17.2.1 A books Database
#connection to the Database in Python
import sqlite3

connection = sqlite3.connect('books.db')

#viewing the author Table's Contents

import pandas as pd 

pd.options.display.max_columns = 10

pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])

#viewing titles table's cotents:
pd.read_sql('SELECT * FROM titles', connection)

#viewing author_ISBN Table

df = pd.read_sql('SELECT * FROM author_ISBN', connection)

df.head

#17.2.2 SELECT Queries 
df = pd.read_sql('SELECT first, last FROM authors', connection)

#17.2.3 WHERE Clause
pd.read_sql("""SELECT title, edition, copyright
            FROM titles
            WHERE copyright > '2016'""", connection)
#Pattern Matching 0 or more Characters
pd.read_sql("""SELECT id, first, last
FROM authors
WHERE last LIKE 'D%'""",
            connection, index_col=['id']) 

#Pattern Matching: Any Character(_)
pd.read_sql("""SELECT id, first, last
FROM authors 
WHERE first LIKE '_b%'""", connection, index_col=['id'])

#17.2.4 ORDER BY Clause
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)

#Sorting By Multiple Columns

pd.read_sql("""SELECT id, first, last
            FROM authors
            ORDER BY last, first""",
            connection, index_col=['id'])

pd.read_sql("""SELECT id, first, last
            FROM authors
            ORDER BY last DESC, first ASC""",
            connection, index_col=['id'])

#Combining the WHERE and ORDER BY Clauses
pd.read_sql("""SELECT isbn, title, edition, copyright
            FROM titles
            WHERE title LIKE '%How to Program'
            ORDER BY title""", connection)

#17.2.5 Merging Data from Multiple Tables: INNER JOIN

pd.read_sql("""SELECT first, last, isbn
            FROM authors
            INNER JOIN author_ISBN
            ON authors.id = author_ISBN.id
            ORDER BY last, first""", connection).head()

#17.2.6 INSERT INTO Statement

cursor = connection.cursor()

cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Sue', 'Red')""")

pd.read_sql('SELECT id, first, last FROM authors', 
            connection, index_col=['id'])

#17.2.7 Update Statement

cursor.execute("""UPDATE authors SET last='Black'
            WHERE last='Red' AND first='Sue'""")

pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])

#17.2.8 DELETE FROM Statement

cursor = cursor.execute('DELETE FROM authors WHERE id=6')

cursor.rowcount

pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])

#Closing the Database
#connection.close()



