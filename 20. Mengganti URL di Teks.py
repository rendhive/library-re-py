text = "Visit us at http://example.com or at https://example.org"
new_text = re.sub(r'https?://[a-zA-Z0-9./-]+', 'https://new-url.com', text)

print("Teks yang diperbarui:", new_text)
# Fungsi: Mengganti semua URL dalam string dengan yang baru.
# Kondisi: Ketika Anda ingin memperbarui referensi URL dalam teks.
