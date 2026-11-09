# Kelompok Binary Tree
# 1. Hidayat Sidiq R. (24670116)
# 2. Lieling Pundhi Utami (24670123)

class NodeKaryawan:
    def __init__(self, id_karyawan, nama, jabatan, gaji, ruangan, jam_masuk=None, hari_libur=None):
        # Konstruktor untuk membuat objek karyawan.
        self.id = id_karyawan
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        self.ruangan = ruangan
        self.jam_masuk = jam_masuk or "08:00"
        self.hari_libur = hari_libur or ["Sabtu", "Minggu"]
        self.kiri = None
        self.kanan = None

    def __str__(self):
        #  Representasi string dari objek NodeKaryawan.
        return (f"ID: {self.id}, Nama: {self.nama}, Jabatan: {self.jabatan}, Gaji: {self.gaji}, "
                f"Ruangan: {self.ruangan}, Jam Masuk: {self.jam_masuk}, Libur: {', '.join(self.hari_libur)}")


class Organisasi:
    # Konstruktor untuk inisialisasi struktur organisasi.
    def __init__(self):
        self.root = None        # Root dari binary tree
        self.histori = []       # Riwayat perubahan dalam organisasi

    def tambah_karyawan(self, id_karyawan, nama, jabatan, gaji, ruangan, id_atasan=None, jam_masuk=None, hari_libur=None):
        # Menambahkan karyawan baru ke dalam struktur organisasi.
        if jabatan.lower() == 'ceo':
            if self.root is not None:
                print("CEO sudah ada. Tidak bisa menambahkan lagi.")
                return
            self.root = NodeKaryawan(id_karyawan, nama, jabatan, gaji, ruangan, jam_masuk, hari_libur)
            self.histori.append(f"Tambah CEO: {nama}")
            print("CEO berhasil ditambahkan.")
            return

        if id_atasan is None:
            print("Masukkan ID atasan untuk posisi selain CEO.")
            return

        atasan_node = self.cari_karyawan(self.root, id_atasan)  # Mencari atasan
        if atasan_node is None:
            print("Atasan tidak ditemukan.")
            return
        
        # Validasi jabatan karyawan baru
        if jabatan.lower() == 'manager':
            if atasan_node.jabatan.lower() != 'ceo':
                print("Manager hanya boleh ditempatkan di bawah CEO.")
                return
        elif jabatan.lower() == 'staf':
            if atasan_node.jabatan.lower() != 'manager':
                print("Staf hanya boleh ditempatkan di bawah Manager.")
                return
        elif jabatan.lower() == 'satpam':
            if atasan_node.jabatan.lower() not in ['manager', 'staf']:
                print("Satpam hanya boleh ditempatkan di bawah Manager atau Staf.")
                return
        else:
                print("Jabatan tidak dikenali.")
                return
        
        # Menambahkan karyawan sebagai anak dari atasan
        new_node = NodeKaryawan(id_karyawan, nama, jabatan, gaji, ruangan, jam_masuk, hari_libur)

        if atasan_node.kiri is None:
            atasan_node.kiri = new_node
            print(f"{jabatan.capitalize()} ditambahkan sebagai bawahan kiri dari {atasan_node.nama}.")
        elif atasan_node.kanan is None:
            atasan_node.kanan = new_node
            print(f"{jabatan.capitalize()} ditambahkan sebagai bawahan kanan dari {atasan_node.nama}.")
        else:
            print("Atasan sudah memiliki 2 bawahan.")
            return

        self.histori.append(f"Tambah {jabatan.capitalize()}: {nama} di bawah {atasan_node.nama}")

    def cari_karyawan(self, node, id_karyawan):
        # Mencari node karyawan berdasarkan ID.
        if node is None:
            return None
        if node.id == id_karyawan:
            return node
        kiri = self.cari_karyawan(node.kiri, id_karyawan)   # Cari di sub tree kiri
        if kiri:
            return kiri
        return self.cari_karyawan(node.kanan, id_karyawan)  # Cari di sub tree kanan

    def tampilkan_struktur(self):
        # Menampilkan struktur organisasi dengan traversal preorder.
        print("\nStruktur Organisasi (Preorder):")
        self.preorder(self.root, level=0)

    def preorder(self, node, level):
        # Traversal preorder untuk mencetak struktur organisasi.
        if node:
            print("  " * level + f"↳ {node.nama} ({node.jabatan}) - ID: {node.id}, Ruangan: {node.ruangan}, Jam Masuk: {node.jam_masuk}, Libur: {', '.join(node.hari_libur)}")
            self.preorder(node.kiri, level + 1)
            self.preorder(node.kanan, level + 1)

    def tampilkan_info_gaji(self):
        # Menampilkan informasi gaji dari semua karyawan
        if self.root is None: 
            print("Organisasi masih kosong.")
            return

        self.gaji_info = {
            "total": 0,
            "jumlah": 0,
            "max": float('-inf'),
            "min": float('inf'),
            "termahal": None,
            "termurah": None,
            "per_jabatan": {}
        }
        self.kumpulkan_info_gaji(self.root) # Mengumpulkan informasi gaji

        # Menampilkan ringkasan informasi gaji
        print("\nInformasi Gaji Organisasi:")
        print(f"Total Gaji Semua Karyawan : Rp {self.gaji_info['total']:,}")
        print("Rata-rata Gaji            : Rp {:,.2f}".format(self.gaji_info["total"] / self.gaji_info["jumlah"]))
        print(f"Gaji Tertinggi            : Rp {self.gaji_info['max']:,} ({self.gaji_info['termahal']})")
        print(f"Gaji Terendah             : Rp {self.gaji_info['min']:,} ({self.gaji_info['termurah']})")

        print("\nRata-rata Gaji per Jabatan:")
        for jab, (total, jumlah) in self.gaji_info["per_jabatan"].items():
            rata2 = total / jumlah
            print(f"  - {jab.capitalize():<10}: Rp {rata2:,.2f} (jumlah: {jumlah})")

    def kumpulkan_info_gaji(self, node):
        # Mengumpulkan data gaji dari tree
        if not node:
            return
        gaji = node.gaji
        jab = node.jabatan.lower()

        # Mengupdate total dan statistik gaji
        self.gaji_info["total"] += gaji
        self.gaji_info["jumlah"] += 1

        if gaji > self.gaji_info["max"]:
            self.gaji_info["max"] = gaji
            self.gaji_info["termahal"] = f"{node.nama} ({node.jabatan})"

        if gaji < self.gaji_info["min"]:
            self.gaji_info["min"] = gaji
            self.gaji_info["termurah"] = f"{node.nama} ({node.jabatan})"

        if jab not in self.gaji_info["per_jabatan"]:
            self.gaji_info["per_jabatan"][jab] = [0, 0]

        self.gaji_info["per_jabatan"][jab][0] += gaji
        self.gaji_info["per_jabatan"][jab][1] += 1

        self.kumpulkan_info_gaji(node.kiri) # Rekursi untuk anak kiri
        self.kumpulkan_info_gaji(node.kanan)    # Rekursi untuk anak kanan

    def tampilkan_histori(self):
        # Menampilkan semua perubahan yang terjadi dalam struktur organisasi.
        print("\nRiwayat Perubahan:")
        if not self.histori:
            print("  - Tidak ada perubahan.")
        else:
            for riwayat in self.histori:
                print(f"  - {riwayat}")

    def hapus_karyawan(self, id_karyawan):
        # Menghapus karyawan dari struktur organisasi berdasarkan ID.
        if self.root is None:
            print("Struktur organisasi kosong.")
            return

        if self.root.id == id_karyawan:
            self.histori.append(f"Hapus CEO: {self.root.nama}")
            self.root = None
            print("CEO berhasil dihapus.")
            return

        success = self.hapus_node(self.root, id_karyawan)   # Memanggil fungsi hapus
        if success:
            print("Karyawan berhasil dihapus.")
        else:
            print("Karyawan tidak ditemukan.")

    def hapus_node(self, parent, id_karyawan):
        # Fungsi bantu untuk menghapus node karyawan dari tree berdasarkan ID.
        if parent.kiri:
            if parent.kiri.id == id_karyawan:
                self.histori.append(f"Hapus {parent.kiri.jabatan.capitalize()}: {parent.kiri.nama}")
                parent.kiri = None
                return True
            else:
                if self.hapus_node(parent.kiri, id_karyawan):
                    return True

        if parent.kanan:
            if parent.kanan.id == id_karyawan:
                self.histori.append(f"Hapus {parent.kanan.jabatan.capitalize()}: {parent.kanan.nama}")
                parent.kanan = None
                return True
            else:
                if self.hapus_node(parent.kanan, id_karyawan):
                    return True
        return False


    def cetak_jabatan(self, node, jabatan):
        # Mencetak semua karyawan dengan jabatan tertentu.
        if not node:
            return
        if node.jabatan.lower() == jabatan:
            print(f"  - {node.nama} (ID: {node.id}, Ruangan: {node.ruangan}, Gaji: {node.gaji})")
        self.cetak_jabatan(node.kiri, jabatan)
        self.cetak_jabatan(node.kanan, jabatan)

    def tampilkan_karyawan_libur(self, hari):
        # Menampilkan karyawan yang libur pada hari tertentu.
        print(f"\nKaryawan libur pada hari {hari.capitalize()}: ")
        self.cetak_karyawan_libur(self.root, hari.capitalize())

    def cetak_karyawan_libur(self, node, hari):
        # Mencetak karyawan yang libur pada hari tertentu.
        if not node:
            return
        if hari in node.hari_libur:
            print(f"  - {node.nama} ({node.jabatan}, ID: {node.id})")
        self.cetak_karyawan_libur(node.kiri, hari)
        self.cetak_karyawan_libur(node.kanan, hari)

    def tampilkan_karyawan_masuk_pagi(self, batas_jam="08:00"):
        # Menampilkan karyawan yang masuk kerja sebelum jam tertentu.
        print(f"\nKaryawan yang masuk sebelum jam {batas_jam}:")
        self.cetak_karyawan_masuk_pagi(self.root, batas_jam)

    def cetak_karyawan_masuk_pagi(self, node, batas_jam):
        # Mencetak nama karyawan yang jam masuknya lebih pagi dari batas yang ditentukan.
        if not node:
            return
        if node.jam_masuk < batas_jam:
            print(f"  - {node.nama} ({node.jabatan}, Jam Masuk: {node.jam_masuk})")
        self.cetak_karyawan_masuk_pagi(node.kiri, batas_jam)
        self.cetak_karyawan_masuk_pagi(node.kanan, batas_jam)
