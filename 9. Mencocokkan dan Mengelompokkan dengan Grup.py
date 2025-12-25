pattern = r'(\d{3})-(\d{3})-(\d{4})'
string = 'My phone number is 123-456-7890.'

match = re.search(pattern, string)
if match:
    print("Kode area:", match.group(1))
    print("Nomor lokal:", match.group(2))
    print("Nomor sirkuit:", match.group(3))
# Fungsi: Mencocokkan pola dengan grup dan mengambil bagian yang cocok.
# Kondisi: Ketika Anda perlu mengambil informasi terpisah dari pola yang cocok.
