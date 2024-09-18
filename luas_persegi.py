import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung luas persegi
def hitung_luas():
    try:
        sisi = float(entry_sisi.get())
        luas = sisi ** 2
        messagebox.showinfo("Hasil", f"Luas persegi dengan sisi {sisi} adalah {luas}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai sisi yang valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Diaz Yanita | Hitung Luas Persegi")

# Label untuk sisi
label_sisi = tk.Label(root, text="Masukkan panjang sisi:")
label_sisi.pack(pady=10)

# Entry untuk sisi
entry_sisi = tk.Entry(root)
entry_sisi.pack(pady=5)

# Tombol untuk menghitung luas
button_hitung = tk.Button(root, text="Hitung Luas", command=hitung_luas)
button_hitung.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
