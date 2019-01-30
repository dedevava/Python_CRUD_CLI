import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="toko_mainan"
)


def insert_data(db):
    name = input("Masukan Nama: ")
    address = input("Masukan Alamat: ")
    val = (name, address)
    cursor = db.cursor()
    sql = "INSERT INTO customers (name, address) VALUES(%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak Ada data")
    else:
        for data in results:
            print(data)


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    customers_id = input("pilih id customer> ")
    name = input("Nama Baru: ")
    address = input("Alamat Baru: ")

    sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
    val = (name, address, customers_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input("pilih id customer>")
    sql = "DELETE FROM customers WHERE customer_id=%s"
    val = (customer_id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(db):
     print("=== APLIKASI DATABASE PYTHON ===")
     print("1. Insert Data")
     print("2. Tampilkan Data")
     print("3. Update Data")
     print("4. Hapus Data")
     print("5. Cari Data")
     print("0. Keluar")
     print("------------------")
     menu = input("pilih menu: ")

     #clear screen
     os.system("clear")

     if menu == "1":
         insert_data(db)
     elif menu == "2":
         show_data(db)
     elif menu == "3":
         update_data(db)
     elif menu == "4":
         delete_data(db)
     elif menu == "5":
         search_data(db)
     elif menu == "0":
         exit()
     else:
         print("Menu Salah !")

if __name__ == "__main__":
    while(True):
        show_menu(db)
