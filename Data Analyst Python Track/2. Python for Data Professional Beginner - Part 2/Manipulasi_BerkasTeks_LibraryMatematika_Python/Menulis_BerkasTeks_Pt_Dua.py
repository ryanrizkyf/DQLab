# Menulis ke file dengan mode append
file = open("Manipulasi_BerkasTeks_LibraryMatematika_Python/hello.txt", "a")
file.writelines([
    "Sekarang kita belajar menulis dengan menggunakan Python",
    "Menulis konten file dengan mode a (append)."
])
file.close()
