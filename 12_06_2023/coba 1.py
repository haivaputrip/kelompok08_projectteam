import tkinter as tk

mainform = tk.Tk()

judul= tk.Label(mainform)
judul['text']= 'Tata Usaha Teknik Industri'
judul['font']='Algerian',20
judul['width'] = 30
judul['height'] = 10
judul.pack()

username = tk.Label(mainform, text= 'username')
username.pack()
inputusername = tk.Entry(mainform, width=25)
inputusername.pack()

password = tk.Label(mainform, text='Password')
password.pack()
inputpass = tk.Entry(mainform,)
inputpass['width'] = 25
inputpass.pack()

tombol1 = tk.Button(mainform,
                    command=quit)
tombol1['text'] = 'Lanjut'
tombol1.pack()

mainform.wm_title('T U T I')


mainform.mainloop()


