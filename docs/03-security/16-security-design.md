# Security Design

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan arsitektur keamanan (Security Architecture) pada WorthFlow.

Tujuan utama:

- Melindungi data finansial keluarga
- Menjaga kerahasiaan informasi pengguna
- Menjamin integritas transaksi
- Mendukung audit dan pelacakan aktivitas
- Mengurangi risiko penyalahgunaan sistem

Dokumen ini melengkapi:

- 15-auth-flow.md
- 17-threat-model.md
- 18-audit-log.md

---

# 2. Security Principles

WorthFlow dibangun berdasarkan prinsip berikut.

## Confidentiality

Hanya anggota keluarga yang berhak dapat mengakses data.

---

## Integrity

Seluruh transaksi harus terlindungi dari perubahan ilegal.

---

## Availability

Data tetap dapat digunakan meskipun perangkat sedang offline.

---

## Least Privilege

Setiap pengguna hanya memperoleh hak akses minimum yang diperlukan.

---

## Defense in Depth

Keamanan diterapkan pada beberapa lapisan sekaligus.

Client

↓

API

↓

Authentication

↓

Authorization

↓

Database

↓

Infrastructure

---

# 3. Security Architecture

                Mobile / Web
                      │
                 HTTPS (TLS)
                      │
                FastAPI Backend
                      │
          JWT Authentication
                      │
          Family Authorization
                      │
          Business Validation
                      │
           PostgreSQL + RLS
                      │
             Encrypted Storage

---

# 4. Authentication Security

Authentication menggunakan:

- Supabase Auth

Backend tidak pernah:

- menyimpan password
- melakukan hash password sendiri

Seluruh proses login dikelola oleh Supabase.

---

# 5. Authorization Security

Authorization dilakukan pada dua level.

Level 1

Backend Validation

↓

Family Validation

↓

Business Rule Validation

---

Level 2

PostgreSQL Row Level Security

↓

Family Isolation

↓

Permission Enforcement

---

# 6. Data Classification

WorthFlow mengelompokkan data berdasarkan tingkat sensitivitas.

## Public

- App version
- Configuration

---

## Internal

- Category
- Asset Type

---

## Confidential

- Transaction
- Asset Balance
- Receipt
- OCR Result
- Email Message

---

## Highly Confidential

- JWT
- Refresh Token
- API Secret
- Service Role Key

---

# 7. Encryption Strategy

## Data In Transit

Seluruh komunikasi menggunakan:

HTTPS

TLS 1.3

---

## Data At Rest

Database:

Encrypted oleh Supabase.

File Storage:

Encrypted oleh Storage Provider.

---

## Local Device

Token

↓

Secure Storage

SQLite

↓

Database Encryption (Future)

---

# 8. Secret Management

Secret tidak boleh disimpan pada source code.

Semua secret berada pada:

Environment Variables

Contoh:

SUPABASE_URL

SUPABASE_ANON_KEY

SUPABASE_SERVICE_KEY

GEMINI_API_KEY

JWT_SECRET

---

# 9. API Security

Seluruh endpoint wajib melewati:

Authentication

↓

Authorization

↓

Validation

↓

Business Rule

↓

Audit

↓

Response

---

Semua request wajib menggunakan:

HTTPS

Authorization Header

JWT

---

# 10. Input Validation

Semua input divalidasi.

Contoh:

Amount

>

0

---

Transaction Date

Tidak boleh kosong

---

Category

Harus milik Family yang sama

---

Asset

Harus dimiliki Family yang sama

---

Receipt

Harus berupa gambar

---

# 11. File Upload Security

Receipt Upload

Validasi:

- MIME Type
- Maximum Size
- Image Format
- Virus Scan (Future)

File tidak boleh dieksekusi.

---

# 12. Database Security

WorthFlow menggunakan:

- Foreign Key
- Constraint
- Check Constraint
- Unique Constraint
- Row Level Security

Semua transaksi database menggunakan Transaction (ACID).

---

# 13. Offline Security

Saat offline.

Data tetap tersimpan lokal.

Token tetap berada pada Secure Storage.

Sinkronisasi hanya dilakukan ketika:

Internet tersedia.

JWT valid.

---

# 14. Logging Security

Data berikut tidak boleh masuk log.

- Password
- JWT
- Refresh Token
- API Secret
- OTP

Log hanya menyimpan metadata.

---

# 15. Error Handling

Error tidak boleh membocorkan informasi internal.

Contoh.

Salah

Database connection failed on host ...

Benar

Internal Server Error

---

# 16. Session Security

Session menggunakan:

Access Token

+

Refresh Token

Access Token memiliki umur pendek.

Refresh Token digunakan memperpanjang sesi.

---

# 17. Device Security

Mobile

Menggunakan:

flutter_secure_storage

Web

Menggunakan:

HttpOnly Cookie (Future)

Memory Session

---

# 18. OCR Security

Receipt

↓

OCR

↓

AI Extraction

↓

Draft

↓

Review

↓

Transaction

OCR tidak boleh langsung membuat transaksi.

---

# 19. Email Security

Email hanya dibaca.

Tidak pernah:

- mengirim email
- menghapus email
- mengubah email

Parser hanya mengambil informasi transaksi.

---

# 20. Rate Limiting

Authentication

10 request / menit

OCR Upload

10 request / menit

Email Sync

5 request / menit

API Normal

120 request / menit

---

# 21. Backup Strategy

Database

Automatic Backup

↓

Point In Time Recovery (Future)

---

Receipt

Cloud Storage Backup

---

# 22. Dependency Security

Seluruh dependency wajib:

- versi stabil
- rutin diperbarui
- dipindai menggunakan Dependabot
- dipindai menggunakan GitHub Security

---

# 23. Security Monitoring

Monitoring meliputi:

- Login gagal
- OCR gagal
- Sync gagal
- API Error
- Rate Limit
- Suspicious Activity

---

# 24. Security Checklist

Authentication

✓ JWT

✓ Refresh Token

✓ Secure Storage

---

Authorization

✓ Family Validation

✓ RLS

✓ Role Validation

---

Database

✓ Foreign Key

✓ Constraint

✓ Transaction

---

API

✓ Validation

✓ Rate Limit

✓ HTTPS

---

Logging

✓ Audit Log

✓ No Sensitive Data

---

Infrastructure

✓ Environment Variable

✓ Secret Management

✓ HTTPS

---

# 25. Security Roadmap

MVP

- JWT
- RLS
- HTTPS
- Secure Storage
- Audit Log

Version 2

- Two Factor Authentication
- Biometric Login
- Passkey
- Database Encryption
- Device Management

Version 3

- Hardware Security Key
- Open Banking Security
- Fraud Detection

---

# 26. Summary

WorthFlow menggunakan pendekatan Defense in Depth, yaitu keamanan diterapkan pada seluruh lapisan sistem mulai dari aplikasi mobile, backend, API, database, hingga infrastruktur.

Dengan pendekatan ini, setiap transaksi, aset, email, dan hasil OCR terlindungi melalui kombinasi Authentication, Authorization, Row Level Security, Input Validation, Audit Logging, HTTPS, Secure Storage, serta prinsip Least Privilege.

Dokumen ini menjadi fondasi implementasi keamanan sebelum dilakukan analisis ancaman pada dokumen berikutnya, yaitu **17-threat-model.md**.