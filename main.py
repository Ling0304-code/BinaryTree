import binarytree

if __name__ == "__main__":
    org = binarytree.Organisasi()
    def input_karyawan():
        id_karyawan = int(input("Masukkan ID karyawan: "))
        nama = input("Masukkan nama: ")
        jabatan = input("Masukkan jabatan (CEO/Manager/Staf/Satpam): ")
        gaji = float(input("Masukkan gaji: "))
        ruangan = input("Masukkan ruangan: ")
        jam_masuk = input("Masukkan jam masuk (default 08:00): ") or "08:00"
        libur = input("Masukkan hari libur (pisahkan dengan koma, default Sabtu,Minggu): ") or "Sabtu,Minggu"
        hari_libur = [h.strip().capitalize() for h in libur.split(",")]
        id_atasan = None
        if jabatan.lower() != 'ceo':
            id_atasan = int(input("Masukkan ID atasan: "))
        org.tambah_karyawan(id_karyawan, nama, jabatan, gaji, ruangan, id_atasan, jam_masuk, hari_libur)

    def hapus_karyawan():
        id_hapus = int(input("Masukkan ID karyawan yang akan dihapus: "))
        konfirmasi = input(f"Yakin ingin menghapus karyawan dengan ID {id_hapus}? (y/n): ").lower()
        if konfirmasi == 'y':
            org.hapus_karyawan(id_hapus)
        else:
            print("Penghapusan dibatalkan.")

    while True:
        print("\n==== MENU ====")
        print("1. Tambah karyawan")
        print("2. Tampilkan struktur organisasi")
        print("3. Tampilkan informasi gaji")
        print("4. Hapus Karyawan")
        print("5. Tampilkan riwayat perubahan")
        print("6. Tampilkan karyawan libur di hari tertentu")
        print("7. Tampilkan karyawan yang masuk pagi")
        print("0. Keluar")
        pilihan = input("\nPilih menu: ")

        if pilihan == '1':
            input_karyawan()
        elif pilihan == '2':
            org.tampilkan_struktur()
        elif pilihan == '3':
            org.tampilkan_info_gaji()
        elif pilihan == '4':
            hapus_karyawan()
        elif pilihan == '5':
            org.tampilkan_histori()
        elif pilihan == '6':
            hari = input("Masukkan hari (cth: Senin): ")
            org.tampilkan_karyawan_libur(hari)
        elif pilihan == '7':
            jam = input("Masukkan batas jam masuk (default 08:00): ") or "08:00"
            org.tampilkan_karyawan_masuk_pagi(jam)
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")