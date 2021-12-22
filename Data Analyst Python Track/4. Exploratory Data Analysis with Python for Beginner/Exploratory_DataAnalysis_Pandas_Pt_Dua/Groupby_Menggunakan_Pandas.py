# Kegunaan .groupby adalah mencari summary dari data frame dengan menggunakan aggregate dari kolom tertentu.

# Penggunaan .groupby
df["Score"].groupby([df["Name"]]).mean()
# Penjelasan
# komputasi diatas menggunakan kolom ‘Name’ sebagai aggregate dan kemudian menggunakan menghitung mean dari kolom ‘Score’
# pada tiap - tiap aggregate tersebut.

# Contoh lain
df["Score"].groupby([df["Name"], df["Exam"]]).sum()
# Penjelasan
# komputasi diatas menggunakan kolom ‘Name’ dan ‘Exam’ sebagai aggregate dan kemudian menggunakan menghitung mean dari kolom ‘Score’
# pada tiap - tiap aggregate tersebut.
