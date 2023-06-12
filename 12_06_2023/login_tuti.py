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
        quit()
login()