from flask import *
import sqlite3 as skl

app = Flask(__name__)

@app.route("/")
def hom():
    con = skl.connect("db/db.db")
    con.row_factory = skl.Row
    cur = con.cursor()                                                                
    cur.execute("SELECT * FROM dapatan")                                              
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)
    con.close()
    #return render_template("index.html")

@app.route("/isibaru")
def tambah():
    return render_template("tambah.html")

@app.route("/save", methods=["POST", "GET"])
def savee():
    if request.method == "POST" or request.method == "GET":
        with skl.connect("db/db.db") as con:
            try:
                ied = request.form["id"]
                nama = request.form["nama"]
                tgl = request.form["tanggal"]
                has = request.form["hasil"]
                kl = request.form["keluar"]
                consor = con.cursor()
                consor.execute("INSERT INTO dapatan (id,nama,tanggal,hasil,keluaran) VALUES (?,?,?,?,?)", (ied,nama,tgl,has,kl))
                con.commit()
                msg = "Berhasil"
            except Exception as e:
                con.rollback()
                msg = f"gagal {e.__traceback__.tb_lineno} {e}"
            return render_template("cek.html", msg=msg)
            con.close()
            
@app.route("/lihat")
def lihat():
    con = skl.connect("db/db.db")
    con.row_factory = skl.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM dapatan")
    rows = cur.fetchall()
    return render_template("hasil.html", rows=rows)
    con.close()

@app.route("/hapusdata", methods=["POST", "GET"])
def hapus():
    return render_template("hapus.html")
    
@app.route("/hapusrec", methods=["POST", "GET"])
def hapuss():
    ied = request.form["id"]
    with skl.connect("db/db.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from dapatan where id=?", ied)
            msg = f"id={ied} berhasil dihapus"
        except Exception as e:
            msg = f" {e}\n{ied} gagal dihapus"
        return render_template("hapusrec.html", msg=msg)
        con.close()
        
@app.route("/editada", methods=["POST","GET"])
def edit():
    return render_template("edit.html")
@app.route("/editadarec/<id>", methods=["POST", "GET"])
def editin():
    with skl.connect("db/db.db") as con:
        cur = con.cursor()
        try:
            if request.method == "POST":
                ied = request.form["id"]
                nm = request.form["nama"]
                tgl = request.form["tanggal"]
                has = request.form["hasil"]
                kel = request.form["keluar"]
                cur.execute("UPDATE dapatan SET nama=?, tanggal=?, hasil=?, keluaran=? WHERE id=?", (nm,tgl,has,kel,ied))
                con.commit()
                msg = "Berhasil update data"
        except Exception as e:
            msg = "Gagal"
        return render_template("editrec.html", msg=msg)
        con.close()
            
if __name__ =="__main__":
    app.run(debug=True)
