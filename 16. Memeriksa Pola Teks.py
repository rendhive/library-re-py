text = "My email is example@test.com"
pattern = r'\S+@\S+\.\S+'

match = re.search(pattern, text)
if match:
    print("Email ditemukan:", match.group())
# Fungsi: Mencari pola email dalam string.
# Kondisi: Ketika Anda ingin mencari dan memverifikasi alamat email dalam teks.
