import csv

def ubah_nilai_csv(file_csv, kolom_target, baris_target, nilai_baru):
    with open(file_csv, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if baris_target < len(rows):
        if kolom_target in rows[0]:
            kolom_index = rows[0].index(kolom_target)
            nilai_lama = rows[baris_target][kolom_index]
            rows[baris_target][kolom_index] = nilai_baru

            with open(file_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Nilai dalam file CSV telah diubah.")
            print("Nilai lama:", nilai_lama)
        else:
            print("Kolom target tidak ditemukan dalam file CSV.")
    else:
        print("Baris target melebihi jumlah baris dalam file CSV.")

# Contoh pemanggilan fungsi
nama_file_csv = 'hasil_pengajuan_tandatangan.csv'  # Ganti dengan nama file CSV yang sesuai
kolom_target = 'acc'     # Ganti dengan nama kolom yang ingin diubah nilainya
baris_target = 1        # Ganti dengan indeks baris yang ingin diubah (dimulai dari 0)
nilai_baru = 'tolakk'    # Ganti dengan nilai baru

ubah_nilai_csv(nama_file_csv, kolom_target, baris_target, nilai_baru)
