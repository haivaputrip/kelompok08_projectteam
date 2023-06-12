import tkinter as tk
from PIL import ImageTk, Image

def tombol3():
    mainform3 = tk.Tk()
    mainform3.geometry("1080x720")
    mainform3.resizable(False,False)
    label1 = tk.Label(mainform3,text="Selamat Datang",font=("Algerian",18))
    label1.pack()
    label2 = tk.Label(mainform3,text="Di",font=("Algerian",15))
    label2.pack()
    label3 = tk.Label(mainform3,text="Tata Usaha Teknik Industri",font=("Algerian",28))
    label3.pack()

    button2 = tk.Button(mainform3,text="Masukkan Antrian Prodi",command= mainform3.destroy)
    button2.pack()
    button3 = tk.Button(mainform3,text="Konfirmasi Kaprodi")
    button3.pack()
    button4 = tk.Button(mainform3,text="Pengajuan Fakultas")
    button4.pack()
    Image1 = Image.open("logoft.PNG")
    Image1 = Image1.resize((468,242),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)

    gambar=tk.Label(mainform3,image=photo)
    gambar.pack(pady=50)

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

    button2 = tk.Button(mainform2,text="Pihak Program Studi",command= {mainform2.destroy(),tombol3()})
    button2.pack()
    button3 = tk.Button(mainform2,text="Pihak Fakultas")
    button3.pack()
    Image1 = Image.open("logoft.PNG")
    Image1 = Image1.resize((468,242),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Image1)

    gambar=tk.Label(mainform2,image=photo)
    gambar.pack(pady=50)

    mainform2.mainloop()
    
    
        

def keluar():
    mainform1.destroy()
    tombol2()
    

mainform1 = tk.Tk()
mainform1.geometry("1080x720")
mainform1.resizable(False,False)

Image1 = Image.open("logoft.PNG")
Image1 = Image1.resize((468,242),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(Image1)

gambar=tk.Label(mainform1,image=photo)
gambar.pack(pady=50)

label1 = tk.Label(mainform1,text="Selamat Datang",font=("Algerian",18))
label1.pack()
label2 = tk.Label(mainform1,text="Di",font=("Algerian",15))
label2.pack()
label3 = tk.Label(mainform1,text="Tata Usaha Teknik Industri",font=("Algerian",28))
label3.pack()

button1 = tk.Button(mainform1,text="Mulai",command=keluar)
button1.pack()
mainform1.mainloop()