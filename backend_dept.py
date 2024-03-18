import sqlite3

def connect():
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS department(id INTEGER PRIMARY KEY,item TEXT,expirydate TEXT , price REAL , quantity INTEGER)")
    conn.commit()
    conn.close()

def insert(item,expirydate,price,quantity):
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO department VALUES (NULL,?,?,?,?)",(item,expirydate,price,quantity))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM department")
    rows = cur.fetchall()
    return rows

def search(item="",expirydate="",price="",quantity=""):
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM department WHERE item = ? OR expirydate = ? OR price =? OR quantity=?",(item,expirydate,price,quantity))
    rows = cur.fetchall()
    return rows

def delete(id):
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM department WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(item,expirydate,price,quantity,id):
    conn = sqlite3.connect("department_store.db")
    cur = conn.cursor()
    cur.execute("UPDATE department SET item=?,expirydate=?,price=?,quantity=? WHERE id =?",(item,expirydate,price,quantity,id))
    conn.commit()
    conn.close()

def buy(item,expirydate,price,quantity,id):
    try:
        conn =sqlite3.connect("department_store.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM department WHERE item=?",(item,))
        obj = cur.fetchall()
        qty = obj[0][-1]
        cur.execute(f"UPDATE department SET item=?,expirydate=?,price=?,quantity=? WHERE id=?",(item,expirydate,price,qty-int(quantity),id))
        conn.commit()
        conn.close()
        return obj
    except:
        pass

connect()

# print(view())