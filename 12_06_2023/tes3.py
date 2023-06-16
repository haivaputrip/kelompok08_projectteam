import pandas as pd
import tkinter as tk
from tkinter import ttk

# Membaca file CSV
df = pd.read_csv('hasil_pengajuan_tandatangan.csv')

mainform6 = tk.Tk()
mainform6.geometry("1080x720")
mainform6.resizable(False,False)
mainform6.configure(background="#395b7d")
# Menampilkan data dalam Treeview atau DataFrame
def tampilkan_data():
    # Menampilkan data dalam Treeview
    treeview.delete(*treeview.get_children())
    for index, row in df.iterrows():
        treeview.insert('', 'end', values=row.tolist())
    
    # Menampilkan data dalam DataFrame
    print("Data pengajuan tandatangan:")
    print(df)

# Fungsi untuk mengubah nilai sel
def ubah_nilai_sel():
    baris = int(ent_baris.get()) - 1
    kolom = ent_kolom.get()
    nilai = ent_nilai.get()

    # Memperbarui nilai sel dalam DataFrame
    df.at[baris, kolom] = nilai

    # Memperbarui nilai sel dalam Treeview
    treeview.item(baris, values=df.iloc[baris].tolist())

    # Menyimpan perubahan ke dalam file CSV
    df.to_csv('hasil_pengajuan_tandatangan.csv', index=False)
    print('Nilai sel berhasil diubah dan disimpan.')

# Menampilkan data awal
tampilkan_data()

# Membuat input untuk memasukkan baris, kolom, dan nilai baru
label_baris = tk.Label(mainform6, text="Baris:", font=("Times New Roman", 12), bg="white")
label_baris.place(x=170, y=505)
ent_baris = tk.Entry(mainform6, width=5, font=("Times New Roman", 12))
ent_baris.place(x=220, y=505)

label_kolom = tk.Label(mainform6, text="Kolom:", font=("Times New Roman", 12), bg="white")
label_kolom.place(x=260, y=505)
ent_kolom = tk.Entry(mainform6, width=5, font=("Times New Roman", 12))
ent_kolom.place(x=320, y=505)

label_nilai = tk.Label(mainform6, text="Nilai:", font=("Times New Roman", 12), bg="white")
label_nilai.place(x=360, y=505)
ent_nilai = tk.Entry(mainform6, width=10, font=("Times New Roman", 12))
ent_nilai.place(x=415, y=505)

button_ubah = tk.Button(mainform6, text="Ubah Nilai", bg="green", fg="white", font=("Times New Roman", 12), command=ubah_nilai_sel)
button_ubah.config(width=10, height=1)
button_ubah.place(x=470, y=500)
