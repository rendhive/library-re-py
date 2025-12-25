phone_pattern = r'^\+?1?\d{9,15}$'
phone_number = '+14155552671'

if re.match(phone_pattern, phone_number):
    print("Nomor telepon valid.")
else:
    print("Nomor telepon tidak valid.")
# Fungsi: Memvalidasi format nomor telepon dengan pola yang ditentukan.
# Kondisi: Ketika Anda ingin memastikan format nomor telepon yang dimasukkan adalah valid.
