#Program 10.1: Tuples dan Sets

#Kode Program:

# LIST
# menggunakan kurung siku
data_list = [10, 2, 4, 3, 2]
print(data_list)

# tuples
data_tuples = (7, 8, 10, 11)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets (himpunan)
data_sets = {10, 4, 3, 2, 7, 6, 5}
print(data_sets)
# print(data_sets[0])

# Program 10.2: Dictionary

# Kode Program:

## Dictionary
# list -> array, mengakses dengan menggunakan index
data_list = ['ucup', 'rendi', 'salsa']
print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key
data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'rd': 'rendi',
    'sl': 'salsa',
    'nmbr': 100,
    'list': data_list
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])


# Program 10.3: Operasi Dictionary

# Kode Program:

## Operasi Dictionary
data_dict = {
    "cup": "ucup surucup",
    "pet": "opet saripet",
    "ndo": "nando surundo"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan"))

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"iwn": "iwan mang keren"})
print(data_dict)

# menghapus data
del data_dict["iwn"]
print(data_dict)


# Program 10.4: Looping Dictionary

# Kode Program:

## Looping Dictionary
teman_teman = {
    "cup": "ucup surucup",
    "tong": "sotong surotong",
    "lur": "lur sedulur",
    "wel": "bung towel"
}

# looping first try (yang keluar hanya key)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")


# Latihan 10.1: Tuple dan Set

# Kode Program:

## Latihan 1: Tuple dan Set
# a. Membuat tuple mahasiswa berisi ("Nama", "NIM", "Prodi")
mahasiswa = ("[Nama Mahasiswa]", "[NIM Mahasiswa]", "[Prodi Mahasiswa]")

# b. Menampilkan data NIM dan Prodi dengan mengakses indeksnya
print("NIM   :", mahasiswa[1])
print("Prodi :", mahasiswa[2])

# c. Mencoba mengubah elemen tuple pada indeks ke-2
# mahasiswa[2] = "Teknologi Informasi"

# d. Membuat set nilai_angka dan mencetak ke layar
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Isi set nilai_angka:", nilai_angka)


## Latihan 2: Manipulasi Dictionary
# a. Membuat dictionary data_mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

# b. Mengubah nilai "prodi" sekaligus menambahkan key baru "angkatan"
data_mahasiswa.update({
    "prodi": "Sastra Mesin ",
    "angkatan": 2026
})

# c. Menghapus data "nim" dan menampilkan hasil akhir dictionary
del data_mahasiswa["nim"]
print("Hasil akhir data_mahasiswa:", data_mahasiswa)

## Latihan 3: Perulangan pada Dictionary
# a. Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Perulangan untuk menampilkan setiap barang dan harganya
total_belanja = 0
for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")
    total_belanja += harga

# c. Menampilkan total belanja
print(f"Total belanja: Rp {total_belanja}")
