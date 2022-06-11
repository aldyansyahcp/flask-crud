import sqlite3

try:
    con = sqlite3.connect("db/db.db")
    con.execute("create table dapatan(id INTEGER NOT NULL, nama TEXT NOT NULL, tanggal TEXT NOT NULL, hasil INTEGER NOT NULL, keluaran INTEGER NOT NULL)")
    print("Table berhasil")
    con.close()
except Exception as e:
    print("Table gagal",e)
