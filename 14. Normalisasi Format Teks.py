text = "Apple, apple, APPLE"
normalized_text = re.sub(r'apple', 'Apple', text, flags=re.IGNORECASE)

print("Teks yang dinormalisasi:", normalized_text)
# Fungsi: Mengubah format teks agar konsisten.
# Kondisi: Ketika Anda ingin memastikan semua penyebutan kata sama.
