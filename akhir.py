from tkinter import *
from tkinter import messagebox
import random

kesempatan = 3

# score = ["100", "80", "60", "50"]

nomorJawaban = random.randint(1, 10)

def mainLagi():
   global nomorJawaban
   global kesempatan

   nomorJawaban = random.randint(1, 10)
   kesempatan = 3
   text.set("Kamu punya 3 kesempatan!")
   messagebox.showinfo("RESET", "Silahkan main lagi")
   tombolCek.place(x=105, y=70)
   kotakJawaban.delete(0, END)

def cekJawaban():
   global kesempatan
   global text

   kesempatan -= 1

   try:
      nomorTebakan = float(kotakJawaban.get())
   except ValueError:
      text.set("Coba gunakan angka!\n kamu punya sisa " + str(kesempatan) +" kesempatan")
      kotakJawaban.delete(0, END)
      if kesempatan == 0:
          text.set("GAME OVER!\nkamu tidak memberikan jawaban yang benar\njawaban yang benar = " + str(nomorJawaban))
          tombolCek.place_forget()

   if nomorJawaban == nomorTebakan:
      text.set("Selamat! Kamu menang! \njawaban yang benar = " + str(nomorJawaban))
      tombolCek.place_forget()
      # if kesempatan > 2:
      #    text2.set("Karena kamu menang dengan sisa " + str(kesempatan) + "\n kesempatan kamu mendapatkan score " + score[1])
      # elif kesempatan > 1:
      #    text2.set("Karena kamu menang dengan sisa " + str(kesempatan) + "\n kesempatan kamu mendapatkan score " + score[2])
      # elif kesempatan > 0:
      #    text2.set("Karena kamu menang dengan sisa " + str(kesempatan) + "\n kesempatan kamu mendapatkan score " + score[3])
   elif kesempatan == 0:
      text.set("GAME OVER!\nKamu kehabisan kesempatan menebak \njawaban yang benar = " + str(nomorJawaban))
      tombolCek.place_forget()
      kotakJawaban.delete(0, END)
   elif nomorTebakan < nomorJawaban:
      text.set(" Jawaban salah - kamu punya sisa " + str(kesempatan) + " kesempatan - \nHINT: Coba nomor lebih tinggi")
      kotakJawaban.delete(0, END)
   elif nomorTebakan > nomorJawaban:
      text.set(" Jawaban salah - kamu punya sisa " + str(kesempatan) + " kesempatan - \nHINT: Coba nomor lebih rendah")
      kotakJawaban.delete(0, END)

root = Tk() # variable root untuk windows utama
root.title("GAME TEBAK NOMOR") # judul dari programnya
root.geometry("325x250") # lebar dan tinggi dari programnya
root.resizable(False, False)


judulan = Label(root, text="SELAMAT DATANG DI GAME TEBAK NOMOR")
instruksi = Label(root, text="Tebaklah nomor dari 1 sampai 10")
kotakJawaban = Entry(root, width=5, borderwidth=4)
tombolCek = Button(root,bg="#15e650", text="CEK", width=6, command=cekJawaban)
Main = Button(root, text="Reset",bg="yellow", width=6, command=mainLagi)


text = StringVar()
text.set("Kamu punya 3 kesempatan!")
# text2 = StringVar()

textUpdate = Label(root, textvariable=text)
# textScore = Label(root, textvariable=text2)
versiGame = Label(root, text="v0.0.2\ndibuat oleh kelompok 1")

judulan.pack()
instruksi.pack()
kotakJawaban.pack()
tombolCek.place(x=90, y=70)
Main.place(x=160, y=70)
textUpdate.pack(pady=30)
# textScore.pack()
versiGame.pack(pady=20)

root.mainloop()