print ("selamat datang di TUTI")
print ("pilih program selanjutnya")
print ("1. Masuk sebagai Tata Usaha Teknik Industri")
print ("2. SUB Bagian Kemahasiswaan dan Alumni")
print ("3. keluar")
pilihan = int(input("masukkan pilihan anda (1-3): "))

if pilihan == 1:
    import login_tuti

    print ("selamat datang di TUTI")
    print ("pilih program selanjutnya")
    print ("1. Masukkan pengajuan tanda tangan")
    print ("2. konfirmasi berkas yang sudah ditanda tangan")
    print ("3. Melanjutkan pengajuan ke pihak Fakultas")
    print ("4. keluar")

    pilihan = int(input("masukkan pilihan anda (1-3): "))

    if pilihan == 1:
        import coba3

    elif pilihan == 2:
        import akun_kaprodi

    elif pilihan == 3:
        import akun_fakultas

    elif pilihan == 4:
        print ("Terima Kasih")

    else:
        print("angka yang anda masukkan tidak valid")

elif pilihan == 2:
    import login_fakultas
    import fakultas

elif pilihan == 3:
    print ("Terima Kasih")

else:
    print("angka yang anda masukkan tidak valid")
