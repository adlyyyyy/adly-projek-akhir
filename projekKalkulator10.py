import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def hitung():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if mode_operasi == "tambah":
            hasil = num1 + num2
        elif mode_operasi == "kurang":
            hasil = num1 - num2
        elif mode_operasi == "kali":
            hasil = num1 * num2
        elif mode_operasi == "bagi":
            if num2 == 0:
                hasil = "Tak Terhingga"
            else:
                hasil = num1 / num2
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid")

def ubah_mode_operasi(mode):
    global mode_operasi
    mode_operasi = mode
    label_mode_operasi.config(text=f"Operasi: {mode.capitalize()}")

root = tk.Tk()
root.title("Aplikasi Kalkulator")

style = Style(theme="minty")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

entry_num1 = ttk.Entry(frame)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = ttk.Entry(frame)
entry_num2.grid(row=1, column=0, padx=5, pady=5)

label_hasil = ttk.Label(frame, text="Hasil: ")
label_hasil.grid(row=3, column=0, padx=5, pady=5)

label_mode_operasi = ttk.Label(frame, text="Operasi: Tambah")
label_mode_operasi.grid(row=2, column=0, padx=5, pady=5)

btn_tambah = ttk.Button(frame, text="Pertambahan (+)", command=lambda: ubah_mode_operasi("tambah"))
btn_tambah.grid(row=2, column=1, padx=5, pady=5)

btn_kurang = ttk.Button(frame, text="Perkurangan (-)", command=lambda: ubah_mode_operasi("kurang"))
btn_kurang.grid(row=2, column=2, padx=5, pady=5)

btn_kali = ttk.Button(frame, text="Perkalian (x)", command=lambda: ubah_mode_operasi("kali"))
btn_kali.grid(row=2, column=3, padx=5, pady=5)

btn_bagi = ttk.Button(frame, text="Pembagian (:)", command=lambda: ubah_mode_operasi("bagi"))
btn_bagi.grid(row=2, column=4, padx=5, pady=5)

btn_hitung = ttk.Button(frame, text="Hitung", command=hitung)
btn_hitung.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

root.mainloop()
