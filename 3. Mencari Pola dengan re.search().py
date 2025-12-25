pattern = r'World'
string = 'Hello World'

search = re.search(pattern, string)
if search:
    print("Pola ditemukan:", search.group())
else:
    print("Pola tidak ditemukan.")
# Fungsi: Mencari pola di seluruh string menggunakan re.search().
# Kondisi: Ketika Anda ingin mencari pola di mana saja dalam string.
