# Fitur .copy()
print(">>> Fitur .copy()")
info_karyawan1 = {'nama': 'Aksara',
                  'nik': '1211011',
                  'pekerjaan': 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
print(info_karyawan2)
