def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

string = "A man, a plan, a canal: Panama"
if is_palindrome(string):
    print("String adalah palindrome.")
else:
    print("String bukan palindrome.")
# Fungsi: Memeriksa apakah string adalah palindrome.
# Kondisi: Ketika Anda ingin mengetahui apakah suatu frase tetap sama dibaca dari depan dan belakang.
