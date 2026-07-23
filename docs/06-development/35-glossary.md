# Glossary

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan istilah-istilah bisnis, teknis, dan arsitektur yang digunakan di seluruh proyek WorthFlow.

Tujuan utama:

- Menyamakan pemahaman seluruh anggota tim.
- Menghindari ambiguitas istilah.
- Menjadi referensi bagi Product, Design, Backend, Frontend, dan QA.
- Menjaga konsistensi dokumentasi.

Apabila terdapat istilah baru selama pengembangan, glossary harus diperbarui.

---

# 2. Business Terms

## Asset

Definisi

Kekayaan yang dimiliki keluarga dan memiliki nilai ekonomi.

Contoh

- Rekening Bank
- Tabungan
- Deposito
- Emas
- Saham
- Properti
- Kendaraan

Database

assets

API

/assets

---

## Budget

Definisi

Batas pengeluaran untuk kategori tertentu dalam periode tertentu.

Contoh

Budget Makan Bulan Juli.

Database

budgets

API

/budgets

---

## Category

Definisi

Kelompok transaksi yang digunakan untuk klasifikasi pemasukan maupun pengeluaran.

Contoh

- Food
- Transport
- Education
- Entertainment
- Salary

Database

categories

---

## Family

Definisi

Sekelompok pengguna yang berbagi data keuangan dalam satu ruang kerja (workspace).

Setiap pengguna hanya dapat menjadi anggota satu Family pada MVP.

Database

families

---

## Family Member

Definisi

Pengguna yang tergabung di dalam sebuah Family.

Role

- Owner
- Admin
- Member
- Viewer

Database

family_members

---

## Transaction

Definisi

Catatan pemasukan atau pengeluaran yang tercatat di dalam sistem.

Jenis

- Income
- Expense
- Transfer (Future)

Database

transactions

API

/transactions

---

## Receipt

Definisi

Bukti transaksi dalam bentuk gambar atau dokumen yang digunakan sebagai sumber data transaksi.

Database

receipts

API

/receipts

---

## Receipt Draft

Definisi

Hasil OCR yang belum disetujui menjadi transaksi.

Status

Draft

↓

Approved

↓

Rejected

Database

receipt_drafts

---

## Email Transaction

Definisi

Transaksi yang berasal dari email notifikasi bank atau dompet digital.

Database

email_transactions

---

## Analytics

Definisi

Ringkasan data keuangan yang dihasilkan dari transaksi.

Contoh

- Monthly Expense
- Monthly Income
- Cash Flow
- Category Distribution

---

# 3. User Roles

## Owner

Hak akses tertinggi dalam Family.

Dapat.

- Menghapus Family
- Mengubah Role
- Mengelola seluruh data

---

## Admin

Membantu Owner mengelola Family.

Tidak dapat menghapus Family.

---

## Member

Dapat membuat dan mengubah transaksi miliknya.

Tidak dapat mengelola anggota Family.

---

## Viewer

Hanya dapat melihat data sesuai izin yang diberikan.

Tidak dapat membuat atau mengubah data.

---

# 4. OCR Terms

## OCR

Optical Character Recognition.

Teknologi untuk mengubah gambar struk menjadi teks.

---

## OCR Pipeline

Alur pemrosesan.

Receipt

↓

OCR

↓

Parsing

↓

Draft

↓

Approval

↓

Transaction

---

## OCR Confidence

Persentase keyakinan hasil OCR terhadap teks yang dikenali.

Semakin tinggi nilainya, semakin kecil kemungkinan kesalahan.

---

# 5. Email Processing Terms

## Email Parser

Service yang membaca email dan mengekstrak informasi transaksi.

---

## Email Sync

Proses sinkronisasi email secara otomatis.

---

## Parsed Email

Email yang berhasil diproses menjadi data terstruktur.

---

# 6. Offline Terms

## Offline First

Pendekatan yang memungkinkan aplikasi tetap dapat digunakan tanpa koneksi internet.

---

## Sync Queue

Antrian perubahan lokal yang menunggu untuk dikirim ke server.

Database

sync_queue

---

## Conflict Resolution

Proses penyelesaian apabila perubahan lokal dan server bertabrakan.

Strategi MVP.

Last Write Wins.

---

# 7. Security Terms

## JWT

JSON Web Token.

Digunakan untuk autentikasi pengguna.

---

## Refresh Token

Token untuk memperoleh Access Token baru tanpa login ulang.

---

## Row Level Security (RLS)

Mekanisme PostgreSQL yang membatasi akses data berdasarkan pengguna atau Family.

---

## Audit Log

Catatan aktivitas penting yang dilakukan pengguna.

Contoh.

- Login
- Delete Transaction
- OCR Approval

---

# 8. Database Terms

## Primary Key (PK)

Identitas unik suatu record.

Contoh.

```
id
```

---

## Foreign Key (FK)

Relasi antar tabel.

Contoh.

```
family_id

member_id

transaction_id
```

---

## Soft Delete

Penghapusan data tanpa menghilangkan record secara permanen.

Menggunakan.

```
deleted_at
```

---

## Migration

Perubahan struktur database yang terdokumentasi dan dapat direproduksi.

---

# 9. API Terms

## Endpoint

Alamat yang digunakan client untuk mengakses layanan backend.

Contoh.

```
GET /transactions
```

---

## REST API

Arsitektur komunikasi antara client dan server menggunakan HTTP.

---

## Pagination

Teknik membagi data menjadi beberapa halaman.

---

## Filtering

Proses menyaring data berdasarkan kriteria tertentu.

---

# 10. DevOps Terms

## CI

Continuous Integration.

Proses otomatis untuk membangun dan menguji aplikasi setiap ada perubahan kode.

---

## CD

Continuous Deployment.

Proses otomatis untuk melakukan deployment setelah aplikasi dinyatakan layak.

---

## Staging

Lingkungan pengujian sebelum Production.

---

## Production

Lingkungan yang digunakan oleh pengguna akhir.

---

# 11. UI/UX Terms

## Design Token

Nilai desain yang digunakan secara konsisten pada seluruh aplikasi.

Contoh.

- Color
- Typography
- Radius
- Spacing

---

## Component

Elemen UI yang dapat digunakan kembali.

Contoh.

- Button
- Card
- Dialog
- Snackbar

---

## Skeleton Loading

Placeholder yang ditampilkan selama data sedang dimuat.

---

# 12. Engineering Terms

## Repository

Lapisan yang bertugas mengakses database.

---

## Service

Lapisan yang berisi business logic aplikasi.

---

## Controller

Lapisan yang menerima request dan mengembalikan response.

---

## DTO

Data Transfer Object.

Objek yang digunakan untuk pertukaran data antar layer.

---

## Dependency Injection

Teknik pemberian dependency dari luar agar komponen lebih mudah diuji.

---

# 13. Performance Terms

## Response Time

Waktu yang dibutuhkan server untuk merespons request.

---

## Throughput

Jumlah request yang dapat diproses dalam satu detik.

---

## Latency

Waktu tempuh komunikasi antara client dan server.

---

## Memory Leak

Kondisi ketika memori terus bertambah tanpa dilepaskan.

---

# 14. Acronyms

| Acronym | Meaning |
|----------|---------|
| API | Application Programming Interface |
| OCR | Optical Character Recognition |
| JWT | JSON Web Token |
| RLS | Row Level Security |
| CRUD | Create Read Update Delete |
| CI | Continuous Integration |
| CD | Continuous Deployment |
| DTO | Data Transfer Object |
| ORM | Object Relational Mapping |
| SLA | Service Level Agreement |
| QA | Quality Assurance |
| UI | User Interface |
| UX | User Experience |

---

# 15. Cross References

Dokumen terkait.

| Document | Description |
|----------|-------------|
| 02-prd.md | Product Requirement |
| 11-erd.md | Entity Relationship Diagram |
| 12-schema-design.md | Database Schema |
| 14-api-spec.md | REST API |
| 16-security-design.md | Security Architecture |
| 31-design-system.md | UI Components |

---

# 16. Maintenance

Glossary diperbarui apabila.

- Ada entity baru.
- Ada fitur baru.
- Ada perubahan istilah bisnis.
- Ada perubahan arsitektur.

Glossary menjadi referensi resmi seluruh dokumentasi WorthFlow.

---

# 17. Summary

Glossary WorthFlow merupakan kamus istilah resmi yang mendefinisikan konsep bisnis, teknis, keamanan, database, API, DevOps, dan UI/UX yang digunakan di seluruh proyek.

Dengan adanya glossary ini, seluruh anggota tim memiliki pemahaman yang sama terhadap setiap istilah sehingga komunikasi, pengembangan, dan dokumentasi dapat berlangsung secara konsisten sepanjang siklus hidup aplikasi.