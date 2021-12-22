# Fitur .issuperset()
print(">>> Fitur .issuperset()")
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian', 'Semangka', 'Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
print(parcel_C_mengandung_A)
print(parcel_C_mengandung_B)
