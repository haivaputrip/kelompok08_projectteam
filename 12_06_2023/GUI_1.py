import tkinter as tk
from PIL import ImageTk, Image

def tombol6():
    mainform6 = tk.Tk()
    mainform6.geometry("1080x720")
    mainform6.resizable(False,False)
    mainform6.configure(background="#395b7d")

    Image2 = Image.open("logoti2.PNG")
    Image2 = Image2.resize((275,275),Image.ANTIALIAS)
    photo1= ImageTk.PhotoImage(Image2)
    gambar1=tk.Label(mainform6,image=photo1,background="#395b7d")
    gambar1.place(x=210,y=-30)
    gambar1.configure(highlightthickness=0, borderwidth=0,)

    kotak1 =tk.Frame(mainform6,width=905, height=400, bg= 'white')
    kotak1.place(x=90,y=210)

    label1= tk.Label(mainform6,text= "Teknik Industri",font=("Times New Roman",44),bg="#395b7d", fg= "white")
    label1.place(x=435,y=40)
    label2= tk.Label(mainform6,text= "Universitas Sebelas Maret",font=("Times New Roman",30),bg="#395b7d", fg= "white")
    label2.place(x=435,y=110)
    label3= tk.Label(mainform6,text= "Masukkan Data Pemohon",font=("Times New Roman",14),bg="grey", fg= "white",width=90)
    label3.place(x=90,y=210)


    ent1 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent1.place(x=170,y=290)
    label4=tk.Label(mainform6,text= "Nama Pemohon",font=("Times New Roman",12), bg="white")
    label4.place(x=170,y=265)

    ent2 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent2.place(x=170,y=370)
    label5=tk.Label(mainform6,text= "Nama Kegiatan",font=("Times New Roman",12), bg="white")
    label5.place(x=170,y=345)

    ent3 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent3.place(x=170,y=450)
    label6=tk.Label(mainform6,text= "Deadline Tanda Tangan",font=("Times New Roman",12), bg="white")
    label6.place(x=170,y=425)

    ent4 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent4.place(x=600,y=290)
    label7=tk.Label(mainform6,text= "Nama Dosen Tujuan",font=("Times New Roman",12), bg="white")
    label7.place(x=600,y=265)

    ent5 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent5.place(x=600,y=370)
    label8=tk.Label(mainform6,text= "Nama File Pengajuan (Pdf)",font=("Times New Roman",12), bg="white")
    label8.place(x=600,y=345)

    ent6 =tk.Entry(mainform6,width=35, font=("Times New Roman", 12))
    ent6.place(x=600,y=450)
    label9=tk.Label(mainform6,text= "Keterangan",font=("Times New Roman",12), bg="white")
    label9.place(x=600,y=425)

    ent7 =tk.Entry(mainform6, font=("Times New Roman", 12))
    ent7.place(x=350,y=510,width=400, height=30)
    label10=tk.Label(mainform6,text= "Deskripsi Kegiatan",font=("Times New Roman",12), bg="white")
    label10.place(x=350,y=485)

    button1 = button1= tk.Button(mainform6,text="Masuk",bg="blue",fg="white", font=("Times New Roman",12))
    button1.config(width=10,height=1)
    button1.place(x=870,y=560)
    button2 = tk.Button(mainform6,text="Kembali",bg="red",fg="white", font=("Times New Roman",12))
    button2.config(width=10,height=1)
    button2.place(x=120,y=560)

    mainform6.mainloop()


def tombol5():
    mainform5 = tk.Tk()
    mainform5.geometry("1080x720")
    mainform5.resizable(False,False)
   

    Image1 = Image.open("logoft.PNG")
    Image1 = Image1.resize((434,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)
    gambar=tk.Label(mainform5,image=photo)
    gambar.place(x=270)
    gambar.configure(highlightthickness=0, borderwidth=0)
    gambar.place(x=325, y=0)


    kotak1 =tk.Frame(mainform5,width=300, height=30, bg= 'grey')
    kotak1.place(x=400,y=210)
    kotak2 = tk.Frame(mainform5,width=300, height=300, bg= 'white')
    kotak2.place(x=400,y=240)

    label2 = tk.Label(mainform5,text= "Masukkan Username dan Password Anda",font=("Times New Roman",12),bg="grey", fg= "white")
    label2.place(x=420,y=213)
    label3 = tk.Label(mainform5,text= "Username",font=("Times New Roman",12),bg="white")
    label3.place(x=515,y=270)
    label4 = tk.Label(mainform5,text= "Password",font=("Times New Roman",12),bg="white")
    label4.place(x=515,y=330)

    ent1 = tk.Entry(mainform5,width=20, font=("Times New Roman", 15) )
    ent1.place(x=450,y=300)
    ent2 = tk.Entry(mainform5,width=20, font=("Times New Roman", 15), show="*" )
    ent2.place(x=450,y=360)

    button1= tk.Button(mainform5,text="Masuk",bg="blue",fg="white", font=("Times New Roman",12))
    button1.config(width=10,height=1)
    button1.place(x=497,y=410)
    button2= tk.Button(mainform5,text="Kembali",bg="red",fg="white", font=("Times New Roman",12),command=lambda:{mainform5.destroy(),tombol2()})
    button2.config(width=6,height=1)
    button2.place(x=515,y=450)

    mainform5.mainloop()


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

    button1= tk.Button(mainform3,text="Masuk",bg="blue",fg="white", font=("Times New Roman",12),command=lambda:{mainform3.destroy(),tombol6()})
    button1.config(width=10,height=1)
    button1.place(x=497,y=400)
    button2= tk.Button(mainform3,text="Kembali",bg="red",fg="white", font=("Times New Roman",12),command=lambda:{mainform3.destroy(),tombol2()})
    button2.config(width=6,height=1)
    button2.place(x=515,y=440)

    mainform3.mainloop()

    
def tombol2():
    
    mainform2 = tk.Tk()
    mainform2.geometry("1080x720")
    mainform2.resizable(False,False)
    
    Image1 = Image.open("FT1.JPG")
    Image1 = Image1.resize((1080,720),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)
    gambar=tk.Label(mainform2,image=photo)
    gambar.place(x=0,y=0)

    label1 = tk.Label(mainform2,text="Selamat Datang",font=("Algerian",18))
    label1.place(x=460,y=120)
    label2 = tk.Label(mainform2,text="Di",font=("Algerian",15))
    label2.place(x=555,y=160)
    label3 = tk.Label(mainform2,text="Tata Usaha Teknik Industri",font=("Algerian",28))
    label3.place(x=300,y=200)

    button2 = tk.Button(mainform2,text="Pihak Program Studi",command= lambda:{mainform2.destroy(), tombol3()})
    button2.config(width=30,height=1)
    button2.place(x=465,y=340)
    button3 = tk.Button(mainform2,text="Pihak Fakultas", command= lambda:{mainform2.destroy(),tombol5()})
    button3.config(width=20,height=1)
    button3.place(x=500,y=290)

    mainform2.mainloop()    


mainform1 = tk.Tk()
mainform1.geometry("1080x720")
mainform1.resizable(False,False)

Image1 = Image.open("FT1.JPG")
Image1 = Image1.resize((1080,720),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(Image1)

gambar=tk.Label(mainform1,image=photo)
gambar.place(x=0,y=0)

label1 = tk.Label(mainform1,text="Selamat Datang",font=("Algerian",18))
label1.place(x=460,y=120)
label2 = tk.Label(mainform1,text="Di",font=("Algerian",15))
label2.place(x=555,y=160)
label3 = tk.Label(mainform1,text="ADMINISTRASI FAKULTAS TEKNIK",font=("Algerian",28))
label3.place(x=270,y=200)

button1 = tk.Button(mainform1,text="Mulai",command=lambda:{mainform1.destroy(),tombol2()})
button1.config(width=10,height=2)
button1.place(x=515,y=320)

mainform1.mainloop()