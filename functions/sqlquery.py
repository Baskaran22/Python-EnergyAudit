import os
import sqlite3
import pandas as pd

# Clear example.db if it exists
if os.path.exists('energyaudit.db'):
    os.remove('energyaudit.db')


# Create a database
#conn = sqlite3.connect('example.db', check_same_thread=False)
conn = sqlite3.connect('energyaudit.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `energy` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, address TEXT, heatercoolerusage TEXT, lightfanusage TEXT, refrigeratorusage TEXT, waterheaterusage TEXT, washerdryerusage TEXT, energywastageareas TEXT)")

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def Database():
    global conn, cursor
    conn = sqlite3.connect('energyaudit.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `energy` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, address TEXT, heatercoolerusage TEXT, lightfanusage TEXT, refrigeratorusage TEXT, waterheaterusage TEXT, washerdryerusage TEXT, energywastageareas TEXT)")

    
def sql_query(query):
    #Database()
    #cursor.execute("SELECT * FROM `energy` ORDER BY `lastname` ASC")
    #rows = cursor.fetchall()
    #return rows
    
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    #Database()        
    #cursor.execute("INSERT INTO `energy` (firstname, lastname, address, heatercoolerusage, lightfanusage, refrigeratorusage, waterheaterusage, washerdryerusage) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
    #               ("test1", "test1", "test1", "test1", "test1", "test1", "test1", "test1"))
    #conn.commit()

    #Database()        
    #cursor.execute(query,var)
    #conn.commit()
    
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
