def login():
    username = "admin"
    password = "password"
    attempts = 3

    while attempts > 0:
        input_username = input("Masukkan username: ")
        input_password = input("Masukkan password: ")

        if input_username == username and input_password == password:
            print("Login berhasil!")
            break
        else:
            attempts -= 1
            print("Username atau password salah. Sisa percobaan:", attempts)

    if attempts == 0:
        print("Anda telah melebihi batas percobaan. Akun terkunci.")
    
    


    
import openpyxl

# Fungsi untuk meminta input dari pengguna
def get_input(prompt):
    return input(prompt)

# Fungsi untuk menyimpan data pengajuan tandatangan dalam spreadsheet
def simpan_data(nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal):
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Menyimpan header
    sheet['A1'] = 'Nama Pemohon'
    sheet['B1'] = 'Nama Kegiatan'
    sheet['C1'] = 'Deadline Tandatangan'
    sheet['D1'] = 'Deskripsi Kegiatan'
    sheet['E1'] = 'Tujuan Tanda Tangan'
    sheet['F1'] = 'File Proposal Pengajuan'

    # Menyimpan data pengajuan tandatangan
    sheet.append([nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal])

    # Menyimpan file spreadsheet
    wb.save('hasil_pengajuan_tandatangan.xlsx')
    print('Data pengajuan tandatangan telah disimpan dalam file hasil_pengajuan_tandatangan.xlsx')

# Meminta input dari pengguna
nama_pemohon = get_input("Masukkan nama pemohon: ")
nama_kegiatan = get_input("Masukkan nama kegiatan: ")
deadline = get_input("Masukkan deadline tandatangan: ")
deskripsi = get_input("Masukkan deskripsi kegiatan: ")
tujuan = get_input("Masukkan tujuan tanda tangan: ")
file_proposal = get_input("Masukkan nama file proposal pengajuan: ")

# Memanggil fungsi untuk menyimpan data pengajuan tandatangan dalam spreadsheet
simpan_data(nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal)



