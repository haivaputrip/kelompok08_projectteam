import openpyxl

def buka_file_excel():
    nama_file = "hasil_pengajuan_tandatangan.xlsx"
    
    try:
        # Buka file Excel
        workbook = openpyxl.load_workbook(nama_file)
        
        # Mengambil sheet pertama
        sheet = workbook.active
        
        # Membaca data
        for row in sheet.iter_rows():
            for cell in row:
                print(cell.value, end="\t")
            print()
        
        # Mengizinkan pengguna mengedit file
        while True:
            baris = input("Masukkan nomor baris yang ingin diedit (atau 'selesai' untuk keluar): ")
            
            if baris.lower() == "selesai":
                break
            
            kolom = "G"
            nilai_baru = input("Masukkan nilai baru: ")
            
            # Mengubah nilai sel yang diinginkan
            sheet[kolom + baris] = nilai_baru
        
        # Menyimpan perubahan ke file
        workbook.save(nama_file)
        print("Perubahan telah disimpan.")
            
    except FileNotFoundError:
        print("File tidak ditemukan.")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

# Memanggil fungsi untuk membuka dan mengedit file Excel
