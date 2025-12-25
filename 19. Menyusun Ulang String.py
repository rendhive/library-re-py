text = "John Doe"
formatted_text = re.sub(r'(\w+) (\w+)', r'\2, \1', text)

print("String yang diformat:", formatted_text)
# Fungsi: Mengubah susunan kata dalam string.
# Kondisi: Ketika Anda ingin memformat teks dengan cara yang berbeda.
