# Product Requirements Document
*Version: 0.1 Draft*

# 1. Product Overview
WorthFlow adalah platform manajemen keuangan keluarga berbasis mobile dan web yang membantu keluarga mengonsolidasikan transaksi, aset, struk belanja, dan data keuangan lainnya ke dalam satu dashboard terpadu. Produk ini dirancang dengan pendekatan offline-first, sehingga pengguna tetap dapat mencatat transaksi tanpa koneksi internet dan melakukan sinkronisasi otomatis saat online kembali.

# 2. Problem Statement
1. Data keuangan keluarga tersebar di banyak tempat (mobile banking, email, catatan manual, spreadsheet, struk).
2. Pengeluaran tunai sering terlupakan karena proses pencatatan tidak praktis.
3. Sulit mengetahui total pengeluaran, cash flow, dan net worth keluarga secara menyeluruh.
4. Tidak ada sistem terpusat yang menyimpan histori transaksi dan aset keluarga.
5. Proses rekap bulanan masih manual dan memakan waktu.

# 3. Goals
1. Menyediakan satu tempat untuk seluruh data keuangan keluarga.
2. Mempermudah pencatatan transaksi harian.
3. Mendukung penggunaan offline dan sinkronisasi otomatis.
4. Menyediakan dashboard keuangan yang mudah dipahami.
5. Mengurangi pekerjaan manual dalam rekap dan pelaporan.

# 4. Non-Goals
Versi awal produk tidak mencakup:
* Transfer uang antar pengguna.
* Pembayaran tagihan.
* Fitur investasi otomatis.
* Chatbot keuangan.
* Workspace lintas keluarga tidak termasuk pada MVP.

# 5. Target Users
## Primary Users
Anggota keluarga yang ingin mencatat dan memantau keuangan harian.

## Secondary Users
Administrator keluarga yang membutuhkan akses penuh untuk monitoring, audit, dan ekspor data.

# 6. User Personas
## Ayah
* Usia sekitar 50–60 tahun.
* Ingin pencatatan transaksi yang cepat dan sederhana.
* Sering melakukan pengeluaran tunai.
* Tidak ingin bergantung pada koneksi internet saat mencatat transaksi.

## Ibu
* Usia sekitar 45–55 tahun.
* Sering melihat rekap bulanan dan kategori pengeluaran.
* Menggunakan aplikasi mobile setiap hari.

## Admin
* Mengelola konfigurasi sistem.
* Melihat audit log dan sinkronisasi.
* Mengekspor data ke spreadsheet.
* Membantu anggota keluarga jika terjadi masalah.

# 7. User Stories
* Sebagai anggota keluarga, saya ingin mencatat pengeluaran meskipun offline agar transaksi tidak terlupakan.
* Sebagai pengguna, saya ingin mengunggah foto struk agar data transaksi dapat diisi otomatis.
* Sebagai pengguna, saya ingin melihat total pengeluaran bulanan agar bisa mengontrol keuangan.
* Sebagai admin, saya ingin melihat seluruh transaksi keluarga agar dapat membuat rekap tahunan.
* Sebagai admin, saya ingin mengekspor data ke spreadsheet agar mudah dibagikan dan dianalisis lebih lanjut.

# 8. Functional Requirements
## 8.1 Authentication & Family Workspace
| ID    | Requirement                                 |
| ----- | ------------------------------------------- |
| FR-01 | User dapat login dan logout.                |
| FR-02 | User dapat bergabung ke workspace keluarga. |
| FR-03 | Admin dapat mengelola anggota keluarga.     |

## 8.2 Manual Transaction
| ID    | Requirement                                               |
| ----- | --------------------------------------------------------- |
| FR-04 | User dapat menambah transaksi pemasukan atau pengeluaran. |
| FR-05 | User dapat mengedit dan menghapus transaksi.              |
| FR-06 | Transaksi dapat diberi kategori dan catatan.              |
| FR-07 | Transaksi dapat disimpan saat offline.                    |

## 8.3 Offline Sync Engine
| ID    | Requirement                                                   |
| ----- | ------------------------------------------------------------- |
| FR-08 | Aplikasi menyimpan transaksi offline di database lokal.       |
| FR-09 | Sistem melakukan sinkronisasi otomatis saat koneksi tersedia. |
| FR-10 | User dapat melihat status sinkronisasi transaksi.             |

## 8.4 Receipt OCR
| ID    | Requirement                                                     |
| ----- | --------------------------------------------------------------- |
| FR-11 | User dapat mengunggah foto struk.                               |
| FR-12 | Sistem melakukan OCR pada gambar.                               |
| FR-13 | Sistem menampilkan hasil ekstraksi untuk diverifikasi pengguna. |
| FR-14 | User dapat memperbaiki hasil OCR sebelum disimpan.              |

## 8.5 Email Transaction Ingestion
| ID    | Requirement                                                         |
| ----- | ------------------------------------------------------------------- |
| FR-15 | Sistem dapat membaca email transaksi dari provider tertentu.        |
| FR-16 | Sistem mengekstrak nominal, tanggal, merchant, dan jenis transaksi. |
| FR-17 | Hasil parsing dapat ditinjau sebelum menjadi transaksi permanen.    |

## 8.6 Asset Tracking
| ID    | Requirement                                                           |
| ----- | --------------------------------------------------------------------- |
| FR-18 | User dapat menambah aset seperti tabungan, deposito, saham, dan emas. |
| FR-19 | Sistem menghitung total nilai aset dan net worth.                     |

## 8.7 Dashboard & Analytics
| ID    | Requirement                                           |
| ----- | ----------------------------------------------------- |
| FR-20 | Dashboard menampilkan cash flow bulanan.              |
| FR-21 | Dashboard menampilkan kategori pengeluaran terbesar.  |
| FR-22 | Dashboard menampilkan tren pengeluaran dan net worth. |

## 8.8 Admin Web Panel
| ID    | Requirement                                             |
| ----- | ------------------------------------------------------- |
| FR-23 | Admin dapat melihat seluruh transaksi keluarga.         |
| FR-24 | Admin dapat melihat audit log aktivitas pengguna.       |
| FR-25 | Admin dapat melihat log sinkronisasi dan OCR.           |
| FR-26 | Admin dapat mengekspor data ke Excel/CSV/Google Sheets. |

# 9. Non-Functional Requirements
## 9.1 Availability
* Aplikasi mobile tetap dapat digunakan saat offline.
* Data lokal harus tetap tersedia setelah aplikasi ditutup.

## 9.2 Performance
* Dashboard dimuat dalam waktu kurang dari 3 detik pada koneksi normal.
* Penyimpanan transaksi offline harus terasa instan bagi pengguna.

## 9.3 Security
* Password disimpan menggunakan hashing yang aman.
* Seluruh komunikasi jaringan menggunakan HTTPS.
* Data sensitif memiliki kontrol akses berbasis peran.

## 9.4 Reliability
* Transaksi offline tidak boleh hilang meskipun aplikasi tertutup.
* Sistem harus dapat melakukan retry sinkronisasi otomatis saat gagal.

## 9.5 Usability
* Penambahan transaksi manual dapat diselesaikan dalam maksimal 3 langkah.
* Antarmuka harus mudah digunakan oleh pengguna non-teknis.

# 10. User Flows
## 10.1 Manual Transaction (Offline First)

### Alur
1. User membuka aplikasi mobile.
2. User memilih Tambah Transaksi.
3. User mengisi nominal, kategori, dan catatan.
4. Sistem menyimpan data ke database lokal dengan status pending sync.
5. Saat koneksi tersedia, sistem menyinkronkan data ke server dan spreadsheet.

## 10.2 Receipt OCR
### Alur
1. User mengunggah foto struk.
2. Sistem melakukan OCR dan ekstraksi data.
3. Sistem menampilkan draft transaksi.
4. User meninjau dan mengedit jika diperlukan.
5. Transaksi disimpan ke database.

## 10.3 Email Transaction Import
### Alur
1. Sistem membaca email baru dari akun yang terhubung.
2. Parser mengekstrak informasi transaksi.
3. Sistem membuat draft transaksi.
4. User/admin meninjau hasil parsing.
5. Transaksi dikonfirmasi dan disimpan.

# 11. MVP Scope
Fitur yang wajib ada untuk versi pertama yang dapat digunakan keluarga:
* Authentication dan family workspace.
* Manual transaction dengan offline-first.
* Sync engine dasar.
* Dashboard cash flow sederhana.
* Receipt OCR dengan review manual.
* Email parser minimal untuk satu bank/provider.
* Asset tracking dasar.
* Admin web panel dan export spreadsheet.

# 12. Success Metrics
| Metric                                      | Target     |
| ------------------------------------------- | ---------- |
| Anggota keluarga aktif menggunakan aplikasi | ≥ 3 orang  |
| Persentase transaksi yang tercatat          | ≥ 90%      |
| Keberhasilan sinkronisasi otomatis          | ≥ 95%      |
| Akurasi ekstraksi OCR                       | ≥ 80%      |
| Waktu input transaksi manual                | < 15 detik |

# 13. Open Questions
1. Provider email mana yang akan didukung pertama kali?
2. Apakah spreadsheet sinkronisasi bersifat otomatis real-time atau manual export?
3. Apakah OCR diproses sepenuhnya di device atau melalui worker backend?
4. Bagaimana strategi conflict resolution jika transaksi diubah di dua device berbeda?

# 14. Future Enhancements
* Kategori otomatis berbasis AI.
* Forecast cash flow dan net worth.
* Budget recommendation.
* Multi-device real-time collaboration.
* Import rekening koran PDF.
* Insight dan notifikasi keuangan berbasis AI.