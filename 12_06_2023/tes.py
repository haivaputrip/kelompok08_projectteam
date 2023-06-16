import tkinter as tk
from PIL import Image, ImageTk

def tombol3():
    mainform3 = tk.Tk()
    mainform3.geometry("1080x720")
    mainform3.resizable(False,False)
    mainform3.configure(background="#395b7d")

    Image2 = Image.open("logoti2.PNG")
    Image2 = Image2.resize((275,275),Image.ANTIALIAS)
    photo1= ImageTk.PhotoImage(Image2)
    gambar1=tk.Label(mainform3,image=photo1,background="#395b7d")
    gambar1.place(x=210,y=-30)
    gambar1.configure(highlightthickness=0, borderwidth=0,)


    kotak1 =tk.Frame(mainform3,width=300, height=30, bg= 'grey')
    kotak1.place(x=400,y=200)
    kotak2 = tk.Frame(mainform3,width=300, height=300, bg= 'white')
    kotak2.place(x=400,y=230)

    label0= tk.Label(mainform3,text= "Teknik Industri",font=("Times New Roman",44),bg="#395b7d", fg= "white")
    label0.place(x=435,y=40)
    label1= tk.Label(mainform3,text= "Universitas Sebelas Maret",font=("Times New Roman",30),bg="#395b7d", fg= "white")
    label1.place(x=435,y=110)
    label2 = tk.Label(mainform3,text= "Masukkan Username dan Password Anda",font=("Times New Roman",12),bg="grey", fg= "white")
    label2.place(x=420,y=203)
    label3 = tk.Label(mainform3,text= "Username",font=("Times New Roman",12),bg="white")
    label3.place(x=515,y=260)
    label4 = tk.Label(mainform3,text= "Password",font=("Times New Roman",12),bg="white")
    label4.place(x=515,y=320)

    ent1 = tk.Entry(mainform3,width=20, font=("Times New Roman", 15))
    ent1.place(x=450,y=290)
    ent2 = tk.Entry(mainform3,width=20, font=("Times New Roman", 15), show="*" )
    ent2.place(x=450,y=350)

    def submit1():
        input_username = ent1.get()
        input_password = ent2.get()
        login(input_username, input_password)

    button1= tk.Button(mainform3,text="Masuk",bg="blue",fg="white", font=("Times New Roman",12),command=submit1)
    button1.config(width=10,height=1)
    button1.place(x=497,y=400)
    button2= tk.Button(mainform3,text="Kembali",bg="red",fg="white", font=("Times New Roman",12),command=lambda:{mainform3.destroy(),tombol2()})
    button2.config(width=6,height=1)
    button2.place(x=515,y=440)

    mainform3.mainloop()


def login(username, password):
    username = "admin"
    password = "password"
    attempts = 3

    while attempts > 0:
        input_username = get_input("Masukkan username: ")
        input_password = get_input("Masukkan password: ")

        if {input_username} == username and input_password == password:
            print("Login berhasil!")
            
            break
        else:
            attempts -= 1
            print("Username atau password salah. Sisa percobaan:", attempts)

    if attempts == 0:
        print("Anda telah melebihi batas percobaan. Akun terkunci.")
        quit()

def get_input(prompt):
    return input(prompt)

tombol3()
