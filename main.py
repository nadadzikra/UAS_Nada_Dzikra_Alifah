import csv
from collections import deque

FILE_CSV = "pegadaian.csv"

# ==========================
# INISIALISASI FILE CSV
# ==========================
def init_file():
    try:
        with open(FILE_CSV, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID_Transaksi",
                "Nama_Nasabah",
                "Barang_Gadai",
                "Nilai_Taksiran",
                "Pinjaman",
                "Status"
            ])
    except FileExistsError:
        pass


# ==========================
# LOAD DATA
# ==========================
def load_data():
    data = []
    try:
        with open(FILE_CSV, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


# ==========================
# SIMPAN DATA
# ==========================
def save_data(data):
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID_Transaksi",
            "Nama_Nasabah",
            "Barang_Gadai",
            "Nilai_Taksiran",
            "Pinjaman",
            "Status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# ==========================
# CREATE
# ==========================
def tambah_data():
    data = load_data()

    transaksi = {
        "ID_Transaksi": input("ID Transaksi : "),
        "Nama_Nasabah": input("Nama Nasabah : "),
        "Barang_Gadai": input("Barang Gadai : "),
        "Nilai_Taksiran": input("Nilai Taksiran : "),
        "Pinjaman": input("Jumlah Pinjaman : "),
        "Status": "Aktif"
    }

    data.append(transaksi)
    save_data(data)

    print("Data berhasil ditambahkan.")


# ==========================
# READ
# ==========================
def tampilkan_data():
    data = load_data()

    if not data:
        print("Tidak ada data.")
        return

    print("\n=== DATA PEGADAIAN ===")
    for item in data:
        print("-" * 40)
        for key, value in item.items():
            print(f"{key} : {value}")


# ==========================
# UPDATE
# ==========================
def update_data():
    data = load_data()

    kode = input("Masukkan ID Transaksi : ")

    ditemukan = False

    for item in data:
        if item["ID_Transaksi"] == kode:
            item["Status"] = input("Status Baru (Aktif/Lunas): ")
            ditemukan = True
            break

    if ditemukan:
        save_data(data)
        print("Data berhasil diupdate.")
    else:
        print("Data tidak ditemukan.")


# ==========================
# DELETE
# ==========================
def hapus_data():
    data = load_data()

    kode = input("Masukkan ID Transaksi : ")

    data_baru = [
        item for item in data
        if item["ID_Transaksi"] != kode
    ]

    save_data(data_baru)

    print("Data berhasil dihapus.")


# ==========================
# SEARCHING (HASH MAP)
# ==========================
def cari_data():
    data = load_data()

    hashmap = {}

    for item in data:
        hashmap[item["ID_Transaksi"]] = item

    kode = input("Masukkan ID Transaksi : ")

    if kode in hashmap:
        print("\nDATA DITEMUKAN")
        for k, v in hashmap[kode].items():
            print(f"{k} : {v}")
    else:
        print("Data tidak ditemukan.")


# ==========================
# SORTING
# ==========================
def sorting_data():
    data = load_data()

    data.sort(
        key=lambda x: int(x["Pinjaman"]),
        reverse=True
    )

    print("\n=== DATA BERDASARKAN PINJAMAN TERBESAR ===")

    for item in data:
        print(
            item["ID_Transaksi"],
            item["Nama_Nasabah"],
            item["Pinjaman"]
        )


# ==========================
# QUEUE ANTRIAN
# ==========================
antrian = deque()

def tambah_antrian():
    nama = input("Nama Nasabah : ")
    antrian.append(nama)

    print("Masuk antrian.")


def panggil_antrian():
    if antrian:
        print("Memanggil :", antrian.popleft())
    else:
        print("Antrian kosong.")


def lihat_antrian():
    if not antrian:
        print("Antrian kosong.")
    else:
        print("\n=== ANTRIAN ===")
        for i, nama in enumerate(antrian, start=1):
            print(f"{i}. {nama}")


# ==========================
# MENU
# ==========================
def menu():
    init_file()

    while True:
        print("\n===== SISTEM PEGADAIAN =====")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Update Status")
        print("5. Hapus Data")
        print("6. Sorting Pinjaman")
        print("7. Tambah Antrian")
        print("8. Panggil Antrian")
        print("9. Lihat Antrian")
        print("0. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_data()

        elif pilih == "2":
            tampilkan_data()

        elif pilih == "3":
            cari_data()

        elif pilih == "4":
            update_data()

        elif pilih == "5":
            hapus_data()

        elif pilih == "6":
            sorting_data()

        elif pilih == "7":
            tambah_antrian()

        elif pilih == "8":
            panggil_antrian()

        elif pilih == "9":
            lihat_antrian()

        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


menu()