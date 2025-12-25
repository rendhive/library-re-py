password = "P@ssw0rd123!"
password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.match(password_pattern, password):
    print("Password valid.")
else:
    print("Password tidak valid.")
# Fungsi: Memvalidasi apakah password memenuhi kriteria keamanan.
# Kondisi: Ketika Anda ingin memeriksa kekuatan password yang dimasukkan.
