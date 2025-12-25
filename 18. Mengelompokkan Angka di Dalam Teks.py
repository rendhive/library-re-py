text = "I have 10 apples, 20 oranges, and 30 bananas."
numbers = re.findall(r'\d+', text)

print("Angka yang ditemukan:", numbers)
# Fungsi: Mengambil semua angka dari teks.
# Kondisi: Ketika Anda ingin mengekstrak data numerik dari string.
