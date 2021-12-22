# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open(
    "Manipulasi_BerkasTeks_LibraryMatematika_Python/Membaca_BerkasTeks_Pt_Dua/hello.txt", "r")
for line in file:
    print(line)
