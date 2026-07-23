# User Stories
*Version: 0.1 Draft*

Dokumen ini mendefinisikan kebutuhan pengguna dari perspektif pengguna akhir (user-centric).

Format:
> Sebagai [role], saya ingin [goal], sehingga [benefit].

## 1. Family Member Stories

### Authentication
### US-001
Sebagai anggota keluarga,

saya ingin login ke aplikasi,

sehingga saya dapat mengakses data keuangan saya dengan aman.

### US-002
Sebagai anggota keluarga,

saya ingin tetap login setelah aplikasi ditutup,

sehingga saya tidak perlu login berulang kali.

## 2. Manual Transaction Stories
### US-003
Sebagai anggota keluarga,

saya ingin menambahkan transaksi pemasukan,

sehingga seluruh pemasukan saya dapat tercatat.

### US-004
Sebagai anggota keluarga,

saya ingin menambahkan transaksi pengeluaran,

sehingga saya mengetahui ke mana uang saya digunakan.

### US-005
Sebagai anggota keluarga,

saya ingin memilih kategori transaksi,

sehingga pengeluaran dapat dikelompokkan dengan baik.

### US-006
Sebagai anggota keluarga,

saya ingin mengedit transaksi yang salah,

sehingga data tetap akurat.

### US-007
Sebagai anggota keluarga,

saya ingin menghapus transaksi yang tidak valid,

sehingga laporan keuangan tetap bersih.


## 3. Offline First Stories
### US-008
Sebagai anggota keluarga,

saya ingin mencatat transaksi tanpa koneksi internet,

sehingga transaksi tidak terlupakan.

### US-009
Sebagai anggota keluarga,

saya ingin aplikasi menyinkronkan data secara otomatis saat internet tersedia,

sehingga saya tidak perlu melakukan sinkronisasi manual.

### US-010
Sebagai anggota keluarga,

saya ingin mengetahui status sinkronisasi data,

sehingga saya yakin transaksi sudah tersimpan di cloud.

## 4. Receipt OCR Stories
### US-011
Sebagai anggota keluarga,

saya ingin memfoto atau mengunggah struk belanja,

sehingga saya tidak perlu mengisi data transaksi secara manual.

### US-012
Sebagai anggota keluarga,

saya ingin sistem mengisi merchant, nominal, dan tanggal secara otomatis,

sehingga proses pencatatan menjadi lebih cepat.

### US-013
Sebagai anggota keluarga,

saya ingin memeriksa dan memperbaiki hasil OCR,

sehingga kesalahan ekstraksi dapat diperbaiki sebelum disimpan.

### US-014
Sebagai anggota keluarga,

saya ingin melihat foto struk yang tersimpan,

sehingga saya dapat melakukan verifikasi di kemudian hari.

## 5. Email Transaction Stories
### US-015
Sebagai anggota keluarga,

saya ingin menghubungkan akun email saya,

sehingga transaksi dari bank dapat diimpor secara otomatis.


### US-016
Sebagai anggota keluarga,

saya ingin melihat transaksi hasil impor email sebelum disimpan,

sehingga saya dapat memverifikasi kebenarannya.

### US-017
Sebagai anggota keluarga,

saya ingin menyetujui atau menolak transaksi hasil impor,

sehingga data yang masuk tetap akurat.

### US-018
Sebagai anggota keluarga,

saya ingin mengetahui email mana yang gagal diproses,

sehingga saya dapat melakukan pengecekan manual.

## 6. Asset Tracking Stories
### US-019
Sebagai anggota keluarga,

saya ingin mencatat saldo rekening saya,

sehingga saya mengetahui posisi dana yang dimiliki.

### US-020
Sebagai anggota keluarga,

saya ingin mencatat aset investasi saya,

sehingga seluruh aset dapat dipantau dalam satu tempat.

### US-021
Sebagai anggota keluarga,

saya ingin memperbarui nilai aset secara berkala,

sehingga perhitungan net worth tetap relevan.

### US-022
Sebagai anggota keluarga,

saya ingin melihat total aset keluarga,

sehingga saya memahami kondisi keuangan secara keseluruhan.

## 7. Dashboard Stories
### US-023
Sebagai anggota keluarga,

saya ingin melihat total pengeluaran bulan ini,

sehingga saya dapat mengontrol pengeluaran.

### US-024
Sebagai anggota keluarga,

saya ingin melihat total pemasukan bulan ini,

sehingga saya memahami kondisi cash flow.

### US-025
Sebagai anggota keluarga,

saya ingin melihat net worth keluarga,

sehingga saya mengetahui perkembangan kekayaan keluarga.

### US-026
Sebagai anggota keluarga,

saya ingin melihat grafik pengeluaran berdasarkan kategori,

sehingga saya mengetahui pola pengeluaran.

### US-027
Sebagai anggota keluarga,

saya ingin memfilter transaksi berdasarkan tanggal dan kategori,

sehingga saya dapat menemukan transaksi tertentu dengan cepat.

3# 8. Spreadsheet Export Stories

### US-028
Sebagai admin keluarga,

saya ingin mengekspor data ke Excel,

sehingga saya dapat membuat laporan tambahan di luar aplikasi.

### US-029
Sebagai admin keluarga,

saya ingin menyinkronkan data ke Google Sheets,

sehingga anggota keluarga yang lebih nyaman menggunakan spreadsheet tetap dapat mengakses data.

## 9. Audit & Security Stories
### US-030
Sebagai admin keluarga,

saya ingin melihat riwayat aktivitas pengguna,

sehingga perubahan data dapat ditelusuri.

### US-031
Sebagai admin keluarga,

saya ingin mengetahui siapa yang mengubah transaksi,

sehingga saya dapat melakukan audit data.

### US-032
Sebagai anggota keluarga,

saya ingin data keuangan saya hanya dapat diakses oleh anggota keluarga yang berwenang,

sehingga privasi tetap terjaga.

## 10. Admin Web Stories
### US-033
Sebagai admin keluarga,

saya ingin melihat seluruh transaksi keluarga dalam satu dashboard,

sehingga saya dapat melakukan monitoring.

### US-034
Sebagai admin keluarga,

saya ingin melihat status sinkronisasi seluruh pengguna,

sehingga saya dapat mendeteksi masalah lebih awal.

### US-035
Sebagai admin keluarga,

saya ingin melihat statistik penggunaan aplikasi,

sehingga saya mengetahui apakah aplikasi benar-benar digunakan.

### US-036
Sebagai admin keluarga,

saya ingin melihat antrean OCR dan email ingestion,

sehingga saya dapat memantau proses otomatisasi.

## 11. Future Stories (Post-MVP)
### US-037

Sebagai anggota keluarga,

saya ingin mendapatkan insight pengeluaran bulanan,

sehingga saya dapat mengambil keputusan finansial yang lebih baik.

### US-038
Sebagai anggota keluarga,

saya ingin menerima rekomendasi penghematan,

sehingga saya dapat meningkatkan savings rate.

### US-039
Sebagai anggota keluarga,

saya ingin melihat proyeksi saldo di masa depan,

sehingga saya dapat merencanakan kebutuhan finansial dengan lebih baik.

## Story Prioritization
### Must Have (MVP)

```text
US-001 sampai US-032
```

### Should Have

```text
US-033 sampai US-036
```

### Could Have

```text
US-037 sampai US-039
```

## Acceptance Criteria Summary

MVP dianggap memenuhi kebutuhan pengguna apabila:

* Pengguna dapat mencatat transaksi saat offline.
* Transaksi tersinkronisasi otomatis saat online.
* Pengguna dapat mengunggah struk dan memverifikasi hasil OCR.
* Pengguna dapat mengimpor transaksi dari email.
* Dashboard dapat menampilkan cash flow dan net worth.
* Admin dapat melakukan audit dan ekspor data.
* Seluruh fitur inti dapat digunakan oleh anggota keluarga non-teknis tanpa pelatihan khusus.