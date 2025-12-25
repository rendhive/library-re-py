pattern = r'Hello'
string = 'Hello World'

match = re.match(pattern, string)
if match:
    print("Pola ditemukan:", match.group())
else:
    print("Pola tidak ditemukan.")
# Fungsi: Mencocokkan pola di awal string menggunakan re.match().
# Kondisi: Ketika Anda perlu memeriksa apakah string dimulai dengan pola tertentu.
