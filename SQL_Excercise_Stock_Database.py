# import sqlite3
# from sqlite3.dbapi2 import Cursor
# Connect to database
# conn = sqlite3.connect('stock.db')
# Create cursor
# c: Cursor = conn.cursor()

# Create a table
# c.execute("""CREATE TABLE stock (
#    part_number integer,
#    part_description text,
#    stock_amount integer
#    )""")

# ----------------------------------------------------

# Insert 1 value at a time
# c.execute("INSERT INTO stock VALUES (001, 'Plug', 100)")
# c.execute("INSERT INTO stock VALUES (002, 'Wire', 50)")
# c.execute("INSERT INTO stock VALUES (003, 'Sensor', 500)")

# ----------------------------------------------------


# Insert multiple values at a time
# many_stock = [
#    (0o04, 'Valve', 30),
#    (0o05, 'LCD', 50),
#    (0o06, 'Quadrature Encoder', 4000),
# ]
# c.executemany("INSERT INTO stock VALUES (?,?,?)", many_stock)

# ----------------------------------------------------


# Query the database
# c.execute("SELECT * FROM stock")
# print(c.fetchone()[0])

# print(c.fetchall())

# ----------------------------------------------------


# List the database lines
# items = c.fetchall()

# for item in items:
#    print(item)


# ----------------------------------------------------

# Update Records
# c.execute("""UPDATE stock SET part_description = 'PNP Sensor'
#               WHERE part_number = 0o01
#               """)

# c.execute("SELECT * FROM stock WHERE part_description = 'Wire'")
# c.execute("SELECT * FROM stock WHERE stock_amount < 100")
# <= >= LIKE etc etc

# ----------------------------------------------------


# Delete Records   .   Delete Quadrature Encoder
# c.execute("DELETE from stock WHERE rowid = 6")
# conn.commit()

# ----------------------------------------------------

# Query the Database: Order by
# c.execute("SELECT stock_amount, * FROM stock ORDER BY stock_amount ASC")
# items = c.fetchall()

# ----------------------------------------------------

# Query the Database: AND/OR
# c.execute("SELECT part_number, * FROM stock WHERE stock_amount >=50 or rowid = 5")
# items = c.fetchall()

# ----------------------------------------------------

# Query the Database: AND/OR  (with Limits)
# c.execute("SELECT part_number, * FROM stock LIMIT 3")
# items = c.fetchall()

# for item in items:
#    print(item)

# ----------------------------------------------------

# Delete/Drop the table
# c.execute("DROP TABLE stock")
# conn.commit


# -------------
# Print when adding to database to confirm command has been executed.
# print("Command executed. ")
# Commit command
# conn.commit()

# Close connection
# conn.close()


# ----------------------------------------------------


# Functions to use with "stock_app

# 1. Query the Database "stock" and Return ALL records
import sqlite3


# stock_app functions

def show_all():
    # Connect to database
    conn = sqlite3.connect('stock.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM stock")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit command
    conn.commit()
    # Close connection
    conn.close()


# Add a New Record to the Table
def add_one(part_number, part_description, stock_amount):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute("Insert INTO stock VALUES (?,?,?)", (part_number, part_description, stock_amount))
    conn.commit()
    conn.close()


# Delete a Record from the Table
def delete_one(id):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute("DELETE from stock WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


# Add Many Records to Table
def add_many(list):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.executemany("Insert INTO stock VALUES (?,?,?)", list)
    conn.commit()
    conn.close()


# Lookup with Where
def part_lookup(part_description):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.executemany('SELECT rowid, * from stock WHERE part_description = (?)', part_description)
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()
