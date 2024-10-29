from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import io

# Membuka dialog untuk memilih gambar
root = tk.Tk()
root.withdraw()  # Menyembunyikan jendela utama
input_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image files", "*.jpg *.jpeg *.png")])

# Jika gambar dipilih, lanjutkan proses
if input_path:
    output_path = 'output_image.png'
    with open(input_path, 'rb') as img_file:
        input_data = img_file.read()

    # Hapus latar belakang
    output_data = remove(input_data)

    # Simpan hasilnya
    output_image = Image.open(io.BytesIO(output_data))
    output_image.save(output_path)
    print(f"Gambar disimpan sebagai {output_path}")
else:
    print("Tidak ada gambar yang dipilih.")
