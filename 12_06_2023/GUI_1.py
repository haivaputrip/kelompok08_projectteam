import tkinter as tk
from PIL import ImageTk, Image

def tombol4():
    mainform4 = tk.Tk()
    mainform4.geometry("1080x720")
    mainform4.resizable(False,False)
    label1 = tk.Label(mainform4,text="Selamat Datang",font=("Algerian",18))
    label1.pack()
    label2 = tk.Label(mainform4,text="Di",font=("Algerian",15))
    label2.pack()
    label3 = tk.Label(mainform4,text="Tata Usaha Teknik Industri",font=("Algerian",28))
    label3.pack()

    button2 = tk.Button(mainform4,text="Masukkan Antrian Prodi",command= mainform4.destroy)
    button2.pack()
    button3 = tk.Button(mainform4,text="Konfirmasi Kaprodi")
    button3.pack()
    button4 = tk.Button(mainform4,text="Pengajuan Fakultas")
    button4.pack()
    Image1 = Image.open("logoft.PNG")
    Image1 = Image1.resize((468,242),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)

    gambar=tk.Label(mainform4,image=photo)
    gambar.pack()

    mainform4.mainloop()

def tombol3():
    mainform3 = tk.Tk()
    mainform3.geometry("1080x720")
    mainform3.resizable(False,False)
    mainform3.configure(background="#395b7d")


    Image1 = Image.open("TI.PNG")
    Image1 = Image1.resize((534,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)
    gambar=tk.Label(mainform3,image=photo)
    gambar.place(x=270)
    gambar.configure(highlightthickness=0, borderwidth=0)


    kotak1 =tk.Frame(mainform3,width=300, height=30, bg= 'grey')
    kotak1.place(x=400,y=200)
    kotak2 = tk.Frame(mainform3,width=300, height=300, bg= 'white')
    kotak2.place(x=400,y=230)

    label2 = tk.Label(mainform3,text= "Masukkan Username dan Password Anda",font=("Times New Roman",12),bg="grey", fg= "white")
    label2.place(x=420,y=203)
    label3 = tk.Label(mainform3,text= "Username",font=("Times New Roman",12),bg="white")
    label3.place(x=515,y=260)
    label4 = tk.Label(mainform3,text= "Password",font=("Times New Roman",12),bg="white")
    label4.place(x=515,y=320)

    ent1 = tk.Entry(mainform3,width=20, font=("Times New Roman", 15) )
    ent1.place(x=450,y=290)
    ent2 = tk.Entry(mainform3,width=20, font=("Times New Roman", 15), show="*" )
    ent2.place(x=450,y=350)

    button1= tk.Button(mainform3,text="Masuk",bg="blue",fg="white", font=("Times New Roman",12))
    button1.config(width=10,height=1)
    button1.place(x=497,y=400)

    button2= tk.Button(mainform3,text="Keluar",bg="red",fg="white", font=("Times New Roman",12),command=lambda:mainform3.destroy())
    button2.config(width=6,height=1)
    button2.place(x=515,y=440)

    mainform3.mainloop()



    
def tombol2():
    mainform2 = tk.Tk()
    mainform2.geometry("1080x720")
    mainform2.resizable(False,False)
    label1 = tk.Label(mainform2,text="Selamat Datang",font=("Algerian",18))
    label1.pack()
    label2 = tk.Label(mainform2,text="Di",font=("Algerian",15))
    label2.pack()
    label3 = tk.Label(mainform2,text="Tata Usaha Teknik Industri",font=("Algerian",28))
    label3.pack()

    button2 = tk.Button(mainform2,text="Pihak Program Studi",command= lambda:{mainform2.destroy(),tombol3()})
    button2.pack()
    button3 = tk.Button(mainform2,text="Pihak Fakultas")
    button3.pack()
    Image1 = Image.open("logoft.PNG")
    Image1 = Image1.resize((468,242),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)

    gambar=tk.Label(mainform2,image=photo)
    gambar.pack(pady=50)

    mainform2.mainloop()


mainform1 = tk.Tk()
mainform1.geometry("1080x720")
mainform1.resizable(False,False)

Image1 = Image.open("logoft.PNG")
Image1 = Image1.resize((234,121),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(Image1)

gambar=tk.Label(mainform1,image=photo)
gambar.pack(pady=50)

label1 = tk.Label(mainform1,text="Selamat Datang",font=("Algerian",18))
label1.pack()
label2 = tk.Label(mainform1,text="Di",font=("Algerian",15))
label2.pack()
label3 = tk.Label(mainform1,text="ADMINISTRASI FAKULTAS TEKNIK",font=("Algerian",28))
label3.pack()

button1 = tk.Button(mainform1,text="Mulai",command=lambda:{mainform1.destroy(),tombol2()})
button1.pack()
mainform1.mainloop()