# MVP Scope Definition
*Version: 0.1 Draft*

Dokumen ini mendefinisikan batasan fitur yang akan dikembangkan pada versi pertama (MVP) WorthFlow.

Tujuan utama MVP adalah memvalidasi bahwa keluarga dapat menggunakan WorthFlow sebagai pusat pencatatan dan pemantauan keuangan sehari-hari tanpa harus bergantung pada banyak aplikasi dan spreadsheet yang terpisah.

# MVP Objective
Pada akhir MVP, pengguna harus dapat:

1. Mencatat transaksi harian dengan cepat.
2. Mencatat transaksi meskipun tanpa koneksi internet.
3. Mengimpor transaksi dari email bank yang didukung.
4. Membuat transaksi dari foto struk.
5. Melihat ringkasan kondisi keuangan keluarga.
6. Melihat total aset dan net worth keluarga.
7. Mengekspor data untuk kebutuhan pelaporan.

# MVP Success Criteria
MVP dianggap berhasil apabila:

* Digunakan oleh minimal 3 anggota keluarga.
* Mampu berjalan stabil selama minimal 30 hari penggunaan nyata.
* > 90% transaksi keluarga tercatat di sistem.
* OCR berhasil membantu pencatatan transaksi dibanding input manual.
* Dashboard mampu menggantikan spreadsheet rekap keluarga yang digunakan sebelumnya.

# In Scope Features
## 1. Authentication
### Included
* Login
* Logout
* Session persistence
* Password reset sederhana
* Family workspace

### Excluded
* SSO
* OAuth login selain Gmail
* Multi-factor authentication

## 2. Family Workspace
### Included
* Membuat keluarga
* Mengundang anggota keluarga
* Role:
  * Admin
  * Member

### Excluded
* Workspace lintas keluarga tidak didukung pada MVP

## 3. Manual Transaction
### Included
* Tambah transaksi
* Edit transaksi
* Hapus transaksi
* Kategori transaksi
* Catatan transaksi
* Upload lampiran opsional

### Excluded
* Split transaction
* Recurring transaction
* Scheduled transaction

## 4. Offline First
### Included
* Penyimpanan lokal
* Input transaksi saat offline
* Queue sinkronisasi
* Auto sync saat online

## Excluded
* Conflict resolution kompleks
* Multi-device merge strategy tingkat lanjut

## 5. Receipt OCR
### Included
* Upload foto struk
* OCR extraction
* AI extraction
* Review hasil OCR
* Simpan menjadi transaksi

### Excluded
* OCR handwriting
* OCR invoice kompleks
* OCR PDF multi halaman

## 6. Email Transaction Import
### Included
* Gmail integration
* Parsing email bank
* Approval workflow
* Duplicate detection sederhana

### Initial Supported Providers
MVP hanya mendukung:

```text id="g0a5h0"
1 provider email terlebih dahulu
```

Provider tambahan ditambahkan setelah MVP stabil.

### Excluded
* Integrasi provider email tambahan tidak termasuk pada MVP.

## 7. Dashboard
### Included
#### Overview
* Total income
* Total expense
* Net cash flow
* Net worth

#### Charts

* Expense by category
* Monthly trend
* Income vs Expense

### Excluded
* Forecasting
* Predictive analytics
* AI recommendations

## 8. Asset Tracking
### Included
* Cash
* Bank account
* Deposito
* Saham
* Crypto
* Properti (manual valuation)

### Excluded
* Live market data
* Broker integration
* Auto valuation

## 9. Export
### Included
* CSV export
* Excel export
* Google Sheets sync

### Excluded
* PDF reporting
* Scheduled reporting

## 10. Audit Log
### Included
* Create transaction log
* Update transaction log
* Delete transaction log
* Login activity

### Excluded
* Security event monitoring
* SIEM integration

# Platforms
## Mobile App
### Included
Target utama MVP.
Fitur lengkap tersedia di mobile.

## Web Admin
### Included
* Dashboard
* Audit log
* User management
* Export

### Excluded
* OCR upload
* Manual transaction entry

# User Roles
## Member
Dapat:
* Melihat dashboard
* Membuat transaksi
* OCR receipt
* Mengelola aset pribadi

## Admin
Dapat:
* Semua hak Member
* Mengelola anggota keluarga
* Melihat audit log
* Mengakses admin dashboard
* Melakukan export data

# Out of Scope (Post-MVP)
Fitur berikut secara eksplisit ditunda.

## AI Features
* Financial advisor AI
* Budget recommendation
* Spending anomaly detection
* Chat assistant

## Advanced Finance
* Debt tracking
* Loan amortization
* Retirement planning
* Investment performance analytics

## Collaboration
* Real-time collaboration
* Transaction approval workflow
* Family budgeting system

## Enterprise Features
* Multi tenant
* Organization support
* Accounting module

# MVP Release Checklist
## Core Flow
* [ ] Login berhasil
* [ ] Family workspace berhasil
* [ ] Manual transaction berhasil
* [ ] Offline transaction berhasil
* [ ] Sync engine berhasil
* [ ] Dashboard berhasil

## Automation Flow
* [ ] OCR berhasil
* [ ] Review OCR berhasil
* [ ] Email parser berhasil
* [ ] Approval workflow berhasil

## Financial Flow
* [ ] Asset tracking berhasil
* [ ] Net worth calculation berhasil
* [ ] Cash flow calculation berhasil

## Administration
* [ ] Audit log berhasil
* [ ] Export CSV berhasil
* [ ] Export Excel berhasil
* [ ] Google Sheets sync berhasil

# MVP User Journey
```text
Login
↓
Join Family
↓
Input Transaction
↓
Offline Storage
↓
Auto Sync
↓
Dashboard Updated
```

## OCR Flow
```text
Receipt
↓
OCR
↓
AI Extraction
↓
Review
↓
Save Transaction
```

## Email Flow
```text
Email
↓
Parser
↓
Candidate Transaction
↓
User Approval
↓
Save Transaction
```

# Definition of Done
WorthFlow MVP dianggap selesai apabila:
1. Seluruh fitur in-scope dapat digunakan pada mobile.
2. Data tersinkronisasi dengan cloud secara stabil.
3. Dashboard menampilkan kondisi keuangan keluarga secara akurat.
4. OCR dan email ingestion dapat menghasilkan transaksi yang dapat diverifikasi pengguna.
5. Aplikasi digunakan secara nyata oleh anggota keluarga selama minimal satu bulan tanpa kehilangan data.