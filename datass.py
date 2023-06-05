import openpyxl

# Fungsi untuk meminta input dari pengguna


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
nama_pemohon = input("Masukkan nama pemohon: ")
nama_kegiatan = input("Masukkan nama kegiatan: ")
deadline = input("Masukkan deadline tandatangan: ")
deskripsi = input("Masukkan deskripsi kegiatan: ")
tujuan = input("Masukkan tujuan tanda tangan: ")
file_proposal = input("Masukkan nama file proposal pengajuan: ")

# Memanggil fungsi untuk menyimpan data pengajuan tandatangan dalam spreadsheet
simpan_data(nama_pemohon, nama_kegiatan, deadline, deskripsi, tujuan, file_proposal)
