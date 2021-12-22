# Membaca file hello.txt dengan fungsi readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open(
    "Manipulasi_BerkasTeks_LibraryMatematika_Python/Membaca_BerkasTeks_Pt_Satu/hello.txt", "r")
first_line = file.readline()
second_line = file.readline()
file.close()
print(first_line)
print(second_line)
