url = 'https://www.example.com/page'
domain_pattern = r'https?://(www\.)?([a-zA-Z0-9-]+(\.[a-z]{2,})+)'

match = re.search(domain_pattern, url)
if match:
    print("Domain:", match.group(2))
# Fungsi: Mengambil nama domain dari string URL.
# Kondisi: Ketika Anda ingin mengekstrak domain dari URL lengkap.
