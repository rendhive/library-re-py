ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
string = 'The server is located at 192.168.0.1 and backup at 10.0.0.2.'

matches = re.findall(ip_pattern, string)
print("Alamat IP yang ditemukan:", matches)
# Fungsi: Mengambil semua alamat IP dari string.
# Kondisi: Ketika Anda ingin menemukan alamat IP dalam teks.
