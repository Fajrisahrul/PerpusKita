import csv
import os
from datetime import datetime as dt

filename = 'perpus.csv'

def clear():
    os.system('cls')

def Back():
    print('\n')
    input('Tekan ENTER untuk kembali ke Menu utama...')
    Menu()

def login():
    clear()
    nama = 'PerpusKita'
    sandi = '123456'
    cek = 'y'
    a = 0
    while cek == 'y' :
        print('----Silahkan Login Dahulu-----')
        print('-'*30)
        user = input('Username : ')
        passw = input('Password : ')
        print('-'*30)
        if user == nama and passw == sandi:
            print()
            break
        else :
            print('Username atau Password salah')
        a = a+1
        if a == 3:
            print('Mampusss Akun Anda Di Blokir wkwkwkwk :) ')
            exit()
            break
        print()
        cek = input('Masukkan Username dan Password lagi ? y/t : ')    
        if cek == 't':
            exit()
        elif cek != 'y':
            exit()
        print()
login()

def Daftar_Transaksi():
    clear()
    data = []

    with open(filename, 'r') as csv_file:
        buku = csv.reader(csv_file, delimiter='|')
        for bk in buku:
            data.append(bk)

    print('===========================================================Data Transaksi=========================================================')
    kolom = ['No', 'Tanggal', 'Nama', 'Tindakan', 'Judul Buku', 'Lama peminjaman', 'Denda',] 
    print("-" * 130)
    for row in kolom: 
        print("{:20}".format(row),end='') 
    print()
    print('-' * 130)
    for tabel in data: 
        list_tabel = [tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5], tabel[6]]
        for x in list_tabel:
            print("{:20}".format(x),end='') 
        print()
    print('='*130)
    
def Pinjam_Buku():
    clear()
    data = []

    with open(filename, 'r') as csv_file:
        buku = csv.reader(csv_file, delimiter='|')
        for bk in buku:
            data.append(bk)
            
    print('===========================================================Data Transaksi=========================================================')
    kolom = ['No', 'Tanggal', 'Nama', 'Tindakan', 'Judul Buku', 'Lama peminjaman', 'Denda',] 
    print("-" * 130)
    for row in kolom: 
        print("{:20}".format(row),end='') 
    print()
    print('-' * 130)
    for tabel in data: 
        list_tabel = [tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5], tabel[6]]
        for x in list_tabel:
            print("{:20}".format(x),end='') 
        print()
    print('='*130)

    No = int(input('Masukkan No : '))
    Tanggal = dt.now().strftime('%Y-%m-%d')
    Nama = input('Masukkan Nama : ')
    Tindakan = input('Masukkan Tindakan (pinjam) : ')
    Judul_Buku = input('Masukkan judul buku : ')
    Lama_peminjaman = int(input("Lama Peminjaman (Hari): "))
    Denda = int(0)
    x = Lama_peminjaman-30
    if Lama_peminjaman <= 30:
        Denda = int(0)
    elif Lama_peminjaman > 30:
        Denda = int(10000*x)
    total = Denda

    data.append([No, Tanggal, Nama, Tindakan,
                 Judul_Buku, Lama_peminjaman, Denda])

    with open(filename, "w", newline="") as csv_file:
        pinjam = csv.writer(csv_file, delimiter="|")
        pinjam.writerows(data)

    print("              PerpusKita            ")
    print("=========================================")
    print('Nama peminjam        : ', Nama)
    print('Judul Buku           : ', Judul_Buku)
    print('tindakan             : ', Tindakan)
    print('Tanggal Peminjaman   : ', Tanggal)
    print('Lama Peminjaman      : ', Lama_peminjaman, 'Hari')
    print('denda                : Rp.', total)
    print("=========================================")


def Sewa_Buku():
    data = []
    clear()

    with open(filename, 'r') as csv_file:
        buku = csv.reader(csv_file, delimiter='|')
        for bk in buku:
            data.append(bk)
    
    print('===========================================================Data Transaksi=========================================================')
    kolom = ['No', 'Tanggal', 'Nama', 'Tindakan', 'Judul Buku', 'Lama peminjaman', 'Denda',] 
    print("-" * 130)
    for row in kolom: 
        print("{:20}".format(row),end='') 
    print()
    print('-' * 130)
    for tabel in data: 
        list_tabel = [tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5], tabel[6]]
        for x in list_tabel:
            print("{:20}".format(x),end='') 
        print()
    print('='*130)
    
    No = int(input('Masukkan No : '))
    Tanggal = dt.now().strftime('%Y-%m-%d')
    Nama = input('Masukkan Nama : ')
    Tindakan = input('Masukkan Tindakan (sewa) : ')
    Judul_Buku = input('Masukkan judul buku : ')
    Lama_peminjaman = int(input("Lama Penyewaan (Bulan): "))
    Denda = int(Lama_peminjaman*20000)
    total = Denda

    data.append([No, Tanggal, Nama, Tindakan,
                 Judul_Buku, Lama_peminjaman, Denda])

    with open(filename, "w", newline="") as csv_file:
        tambah = csv.writer(csv_file, delimiter="|")
        tambah.writerows(data)

    print("              PerpusKita            ")
    print("=========================================")
    print('Nama penyewa         : ', Nama)
    print('Judul Buku           : ', Judul_Buku)
    print('tindakan             : ', Tindakan)
    print('Tanggal Penyewaan    : ', Tanggal)
    print('Lama sewa            : ', Lama_peminjaman, 'Bulan')
    print('Biaya Sewa           : Rp.', total)
    print("=========================================")

def Edit_data():
    clear()
    data = []
    with open(filename, 'r') as csv_file:
        buku = csv.reader(csv_file, delimiter='|')
        for bk in buku:
            data.append(bk)
            print(bk)
    print('===========================================================Data Transaksi=========================================================')
    kolom = ['No', 'Tanggal', 'Nama', 'Tindakan', 'Judul Buku', 'Lama peminjaman', 'Denda',] 
    print("-" * 130)
    for row in kolom: 
        print("{:20}".format(row),end='') 
    print()
    print('-' * 130)
    for tabel in data: 
        list_tabel = [tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5], tabel[6]]
        for x in list_tabel:
            print("{:20}".format(x),end='') 
        print()
    print('='*130)
    
    no = input('Masukkan No yang akan diubah> ')
    tanggal = dt.now().strftime('%Y-%m-%d')
    nama = input('Masukkan nama baru : ')
    tindakan = input('Masukkan Tindakan baru : ')
    judul_buku = input('Masukkan Judul Buku : ')
    lama_peminjaman = int(input('Masukkan lama peminjaman : '))
    if tindakan == 'pinjam':
        x = lama_peminjaman-30
        if lama_peminjaman <= 30:
            Denda = int(0)
        elif lama_peminjaman > 30:
            Denda = int(10000*x)
            total = Denda
    elif tindakan == 'sewa':
        Denda = lama_peminjaman*20000
        total = Denda

    indeks = 0
    for ubah in data:
        if (ubah[0] == no):
            data[indeks][1] = tanggal
            data[indeks][2] = nama
            data[indeks][3] = tindakan
            data[indeks][4] = judul_buku
            data[indeks][5] = lama_peminjaman
            data[indeks][6] = Denda
        indeks = indeks + 1

    with open(filename, 'w', newline="") as csv_file:
        fieldnames = ['No', 'Tanggal', 'Nama', 'Tindakan',
                      'Judul Buku', 'Lama peminjaman', 'Denda']
        tambah = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
        for new_data in data:
            tambah.writerow(
                {
                    'No': new_data[0],
                    'Tanggal': new_data[1],
                    'Nama': new_data[2],
                    'Tindakan': new_data[3],
                    'Judul Buku': new_data[4],
                    'Lama peminjaman': new_data[5],
                    'Denda': new_data[6]
                }
            )

def Hapus_data():
    clear()
    data = []
    with open(filename, 'r') as csv_file:
        buku = csv.reader(csv_file, delimiter='|')
        for bk in buku:
            data.append(bk)
    
    print('===========================================================Data Transaksi=========================================================')
    kolom = ['No', 'Tanggal', 'Nama', 'Tindakan', 'Judul Buku', 'Lama peminjaman', 'Denda',] 
    print("-" * 130)
    for row in kolom: 
        print("{:20}".format(row),end='') 
    print()
    print('-' * 130)
    for tabel in data: 
        list_tabel = [tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5], tabel[6]]
        for x in list_tabel:
            print("{:20}".format(x),end='') 
        print()
    print('='*130)

    No = input('Masukkan No yang akan dihapus > ')
    indeks = 0
    for hapus in data:
        if hapus[0] == No:
            data.remove(data[indeks])

        indeks = indeks + 1
    print('Data berhasil di hapus')

    with open(filename, 'w', newline="") as csv_file:
        fieldnames = ['No', 'Tanggal', 'Nama', 'Tindakan',
                      'Judul Buku', 'Lama peminjaman', 'Denda']
        hapus = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
        for new_data in data:
            print(new_data)
            hapus.writerow(
                {
                    'No': new_data[0],
                    'Tanggal': new_data[1],
                    'Nama': new_data[2],
                    'Tindakan': new_data[3],
                    'Judul Buku': new_data[4],
                    'Lama peminjaman': new_data[5],
                    'Denda': new_data[6]
                }
            )

def Menu():
    clear()
    print(
        """
    ====Data Transaksi=====
    Masukkan Pilihan Anda
    (1). Daftar Transaksi
    (2). Pinjam Buku     
    (3). Sewa Buku       
    (4). Edit data      
    (5). Hapus data       
    (0). Exit            
    =======================
    """
    )

    pilihan = int(input('Masukkan pilihan : '))

    if pilihan == 1:
        Daftar_Transaksi()
    elif pilihan == 2:
        Pinjam_Buku()
    elif pilihan == 3:
        Sewa_Buku()
    elif pilihan == 4:
        Edit_data()
    elif pilihan == 5:
        Hapus_data()
    elif pilihan == 0:
        print('===Terima Kasih===')
        exit()
    else:
        print(f'Maaf, pilihan {pilihan} yang anda masukkan tidak tersedia')
    Back()


if __name__ == "__main__":
    while True:
        Menu()
