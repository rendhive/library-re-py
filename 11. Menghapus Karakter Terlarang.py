string = 'Hello, @world! #2021'
clean_string = re.sub(r'[^a-zA-Z0-9\s]', '', string)

print("String yang dibersihkan:", clean_string)
# Fungsi: Menghapus karakter non-alfanumerik dari string.
# Kondisi: Ketika Anda ingin membersihkan string dari karakter yang tidak diinginkan.
