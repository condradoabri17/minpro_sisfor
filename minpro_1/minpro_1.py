riwayat_servis = []

while True:
    print("\n Sistem Riwayat Maintenance PC/Laptop ")
    print("1. Tambah Riwayat Servis")
    print("2. Lihat Riwayat Servis")
    print("3. Update Riwayat Servis")
    print("4. Hapus Riwayat Servis")
    print("5. Keluar")

    menu = input("Pilih menu (1/2/3/4/5): ")


    if menu == "1":

        print("\n Tambah Riwayat Servis ")
        id_Perangkat = input("Masukkan ID Perangkat: ")
        nama_Perangkat = input("Masukkan Merek Perangkat: ")
        tgl_servis = input("Masukkan Tanggal Servis: ")
        kerusakan = input("Masukkan Deskripsi Kerusakan: ")
        status = input("Masukkan Status (Sedang diperbaiki / Selesai): ")

        data = (id_Perangkat, nama_Perangkat, tgl_servis, kerusakan, status)
        riwayat_servis.append(data)

        print("\n Data riwayat berhasil ditambahkan!")

    elif menu == "2":
        print("\n Lihat Riwayat Servis ")
        if len(riwayat_servis) == 0:
            print("Belum ada data riwayat servis.")
        else:
            if len(riwayat_servis) >= 1:
                data = riwayat_servis[0]
                print("\nData ke-0")
                print("ID:", data[0])
                print("Perangkat:", data[1])
                print("Tanggal:", data[2])
                print("Kerusakan:", data[3])
                print("Status:", data[4])

            if len(riwayat_servis) >= 2:
                data = riwayat_servis[1]
                print("\nData ke-1")
                print("ID:", data[0])
                print("Perangkat:", data[1])
                print("Tanggal:", data[2])
                print("Kerusakan:", data[3])
                print("Status:", data[4])

            if len(riwayat_servis) >= 3:
                data = riwayat_servis[2]
                print("\nData ke-2")
                print("ID:", data[0])
                print("Perangkat:", data[1])
                print("Tanggal:", data[2])
                print("Kerusakan:", data[3])
                print("Status:", data[4])


    elif menu == "3":
        print("\n Edit Riwayat Servis ")
        if len(riwayat_servis) == 0:
            print("Belum ada data untuk diedit.")
        else:
            index = int(input("Pilih data yang mau diedit: "))
            if index < len(riwayat_servis):
                data = riwayat_servis[index]
                print("Data lama:")
                print("ID:", data[0])
                print("Perangkat:", data[1])
                print("Tanggal:", data[2])
                print("Kerusakan:", data[3])
                print("Status:", data[4])

                print("\nMasukkan data baru (biarkan kosong jika tidak ingin diubah):")
                id_Perangkat = input("ID Perangkat baru: ") or data[0]
                nama_Perangkat = input(
                    "Nama Perangkat baru: ") or data[1]
                tgl_servis = input("Tanggal Servis baru: ") or data[2]
                kerusakan = input("Deskripsi Kerusakan baru: ") or data[3]
                status = input("Status baru: ") or data[4]

                riwayat_servis[index] = (
                    id_Perangkat, nama_Perangkat, tgl_servis, kerusakan, status)
                print("\n Data berhasil diedit!")
            else:
                print(" Data tidak ada!")

    elif menu == "4":
        print("\n Hapus Riwayat Servis ")
        if len(riwayat_servis) == 0:
            print("Tidak ada data untuk dihapus.")
        else:
            index = int(input("Pilih data yang mau dihapus : "))
            if index < len(riwayat_servis):
                riwayat_servis.pop(index)
                print("Data berhasil dihapus!")
            else:
                print(" Data tidak ada!")

    elif menu == "5":
        print("\nTerima kasih, program selesai.")
        break

    else:
        print("\n Menu tidak valid, silakan pilih lagi.")
