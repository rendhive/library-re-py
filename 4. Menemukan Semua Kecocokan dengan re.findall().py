pattern = r'\d+'  # Mencocokkan satu atau lebih digit
string = 'There are 2 cats and 3 dogs.'

matches = re.findall(pattern, string)
print("Kecocokan ditemukan:", matches)
# Fungsi: Menemukan semua kecocokan pola dalam string menggunakan re.findall().
# Kondisi: Ketika Anda ingin mendapatkan semua hasil yang cocok dengan pola tersebut.
