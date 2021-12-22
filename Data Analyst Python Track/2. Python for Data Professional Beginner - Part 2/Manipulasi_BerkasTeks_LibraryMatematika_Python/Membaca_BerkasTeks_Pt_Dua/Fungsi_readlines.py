# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open(
    "Manipulasi_BerkasTeks_LibraryMatematika_Python/Membaca_BerkasTeks_Pt_Dua/hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
