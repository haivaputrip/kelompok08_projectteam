import tkinter as tk
from tkinter import filedialog
import shutil

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        destination_path = "C:/Users/ASUS A442U/Documents/tubes/kelompok08_projectteam/KumpulanPDF"  # Ganti dengan path file tujuan
        save_pdf_to_storage(file_path, destination_path)

def save_pdf_to_storage(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print("File PDF berhasil disimpan di", destination_path)
    except IOError as e:
        print("Terjadi kesalahan saat menyimpan file PDF:", str(e))

# Membuat jendela aplikasi menggunakan Tkinter
window = tk.Tk()
window.title("Program Penyimpanan File PDF")

# Membuat tombol "Pilih File PDF"
select_file_button = tk.Button(window, text="Pilih File PDF", command=select_pdf_file)
select_file_button.pack()

# Menjalankan loop utama aplikasi
window.mainloop()