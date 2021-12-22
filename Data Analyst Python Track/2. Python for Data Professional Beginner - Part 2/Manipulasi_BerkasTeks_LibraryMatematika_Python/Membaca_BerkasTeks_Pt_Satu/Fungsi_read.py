# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open(
    "Manipulasi_BerkasTeks_LibraryMatematika_Python/Membaca_BerkasTeks_Pt_Satu/hello.txt", "r")
content = file.read()
file.close()
print(content)
