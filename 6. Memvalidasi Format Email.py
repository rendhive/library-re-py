email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email = 'example@example.com'

if re.match(email_pattern, email):
    print(f"{email} valid.")
else:
    print(f"{email} tidak valid.")
# Fungsi: Memvalidasi apakah string sesuai dengan format email.
# Kondisi: Ketika Anda ingin memastikan format email yang dimasukkan adalah benar.
