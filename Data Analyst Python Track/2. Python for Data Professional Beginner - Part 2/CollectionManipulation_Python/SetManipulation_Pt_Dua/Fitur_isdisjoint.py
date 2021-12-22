# Fitur .isdisjoint()
print(">>> Fitur .isdisjoint()")
parcel1 = {'Anggur', 'Apel', 'Jeruk'}
parcel2 = {'Kiwi', 'Melon', 'Pisang'}
parcel3 = {'Apel', 'Srikaya', 'Semangka'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)
