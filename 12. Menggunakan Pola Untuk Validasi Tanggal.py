date_pattern = r'\d{2}/\d{2}/\d{4}'  # Format dd/mm/yyyy
date_string = '12/12/2023'

if re.match(date_pattern, date_string):
    print("Tanggal valid.")
else:
    print("Tanggal tidak valid.")
# Fungsi: Memvalidasi apakah string sesuai dengan format tanggal.
# Kondisi: Ketika Anda ingin memastikan format tanggal yang dimasukkan adalah benar.
