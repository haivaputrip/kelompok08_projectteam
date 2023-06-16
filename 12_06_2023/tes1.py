import pandas as pd
import tkinter as tk
from tkinter import ttk

def get_input(prompt):
    return input(prompt)

def simpan_data(nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal, keterangan_pengajuan):
    data = {
        'Nama Pemohon': [nama_pemohon],
        'Nama Kegiatan': [nama_kegiatan],
        'Deadline Tandatangan': [deadline],
        'Deskripsi Kegiatan': [deskripsi],
        'Tujuan Tanda Tangan': [tujuan],
        'File Proposal Pengajuan': [file_proposal],
        'Keterangan Pengajuan': [keterangan_pengajuan]
    }

    df = pd.DataFrame(data)

    # Menyimpan data dalam format CSV
    df.to_csv('hasil_pengajuan_tandatangan.csv', index=False)
    print('Data pengajuan tandatangan telah disimpan dalam file hasil_pengajuan_tandatangan.csv')

def tampilkan_data():
    df = pd.read_csv('hasil_pengajuan_tandatangan.csv')

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Data Pengajuan Tandatangan")

    treeview = ttk.Treeview(root, columns=list(df.columns), show='headings')

    for column in df.columns:
        treeview.heading(column, text=column)

    for row in df.itertuples(index=False):
        treeview.insert('', 'end', values=row)

    treeview.pack(expand=True, fill='both')

    # Membaca file Excel
    

    def excel_to_csv(hasil_pengajuan_tandatangan, nama_file_csv):
        df = pd.read_excel(hasil_pengajuan_tandatangan)  # Membaca file Excel menjadi DataFrame
        df.to_csv(nama_file_csv, index=False)  # Menulis DataFrame ke file CSV

        print("File Excel berhasil diubah menjadi CSV.")

        # Contoh pemanggilan fungsi
    nama_file_excel = 'hasil_pengajuan_tandatangan.xlsx'  # Ganti dengan nama file Excel yang ingin diubah
    nama_file_csv = 'hasil_pengajuan_tandatangan.csv'     # Nama file CSV yang dihasilkan

    excel_to_csv(nama_file_excel, nama_file_csv)

    
    root.mainloop()

# Meminta input dari pengguna


# Memanggil fungsi untuk menyimpan data pengajuan tandatangan dalam file CSV
#simpan_data(nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal, keterangan_pengajuan)

# Menampilkan data pengajuan tandatangan
tampilkan_data()


