
print('\n')
biodata = { 'nama'  : 'Ajeng Niwahintan Pratiwi',
'nim'   : '231031108',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'PAREPARE,09 juni 2004',
'jenis kelamin' : 'perempuan',
'agama' : 'islam',
'alamat': 'perumnas wekke e jl jati blok e',
'email' : 'ajenggniwahintanp11@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:4])
print(selected_biodata)




