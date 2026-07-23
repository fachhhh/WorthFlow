# Security Testing

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi Security Testing pada WorthFlow.

Tujuan utama:

- Mengidentifikasi kerentanan keamanan.
- Memastikan implementasi Authentication & Authorization berjalan benar.
- Mengurangi risiko kebocoran data.
- Memastikan aplikasi memenuhi prinsip Secure by Design.
- Mendukung proses Secure Software Development Lifecycle (SSDLC).

Dokumen ini melengkapi:

- 16-security-design.md
- 17-threat-model.md
- 18-audit-log.md
- 27-api-testing.md

---

# 2. Security Objectives

WorthFlow harus mampu melindungi:

- Data finansial keluarga
- Riwayat transaksi
- Asset
- Receipt
- Email
- Session pengguna
- JWT
- Audit Log

Seluruh pengujian keamanan dilakukan sebelum setiap release Production.

---

# 3. Security Testing Scope

Komponen yang diuji.

Frontend

- Flutter Mobile
- Flutter Web

Backend

- FastAPI

Database

- PostgreSQL
- Row Level Security

Infrastructure

- Supabase
- Koyeb
- Vercel

Business Feature

- Authentication
- OCR
- Email Parser
- Offline Sync

---

# 4. Security Principles

WorthFlow menerapkan prinsip.

- Least Privilege
- Defense in Depth
- Secure by Default
- Fail Secure
- Zero Trust
- Principle of Least Knowledge

---

# 5. Authentication Testing

Pengujian.

✓ Login berhasil

✓ Password salah

✓ Email tidak terdaftar

✓ Expired JWT

✓ Invalid JWT

✓ Refresh Token

✓ Logout

✓ Session Expired

Expected.

Semua akses tanpa autentikasi ditolak.

---

# 6. Authorization Testing

Role yang diuji.

Owner

↓

Admin

↓

Member

↓

Viewer

Contoh.

Member mencoba.

DELETE /members/{id}

Expected.

403 Forbidden

---

# 7. Input Validation

Semua endpoint diuji terhadap.

- Empty Value
- Invalid Type
- Invalid Enum
- Long String
- Unicode
- HTML Injection
- Script Injection

Expected.

422 Validation Error.

---

# 8. SQL Injection Testing

Contoh input.

```
' OR 1=1 --
```

Expected.

Request ditolak.

Database tetap aman.

Semua query menggunakan parameterized query melalui ORM.

---

# 9. Cross Site Scripting (XSS)

Contoh.

```html
<script>alert("xss")</script>
```

Expected.

Input disanitasi.

Script tidak pernah dieksekusi.

---

# 10. Cross Site Request Forgery (CSRF)

Pengujian khusus Flutter Web.

Expected.

Request tanpa token CSRF ditolak apabila mekanisme cookie digunakan.

Untuk MVP yang menggunakan Bearer Token, risiko CSRF lebih rendah namun tetap didokumentasikan.

---

# 11. Broken Authentication

Pengujian.

✓ JWT Manipulation

✓ Expired JWT

✓ Invalid Signature

✓ Replay Token

✓ Missing Token

Expected.

401 Unauthorized.

---

# 12. Broken Access Control

Pengujian.

Member mencoba.

- Membaca transaksi milik keluarga lain
- Mengakses Asset keluarga lain
- Menghapus Budget keluarga lain

Expected.

403 Forbidden.

Row Level Security tetap aktif.

---

# 13. IDOR Testing

Pengujian.

User mengganti UUID resource.

```
GET /transactions/{uuid}
```

UUID milik keluarga lain.

Expected.

404 Not Found

atau

403 Forbidden.

Tidak boleh mengembalikan data.

---

# 14. Rate Limiting

Pengujian.

100 Login Request.

↓

Dalam waktu singkat.

Expected.

429 Too Many Requests.

---

# 15. Sensitive Data Exposure

Pastikan.

Password

↓

Tidak pernah dikirim kembali.

JWT

↓

Tidak muncul pada log.

Receipt

↓

Private Bucket.

Database Backup

↓

Encrypted.

---

# 16. File Upload Security

Receipt diuji terhadap.

✓ File terlalu besar

✓ Format salah

✓ File kosong

✓ Double Extension

✓ Executable File

Expected.

Upload ditolak.

---

# 17. API Security

Semua endpoint diuji.

✓ HTTPS

✓ JWT

✓ Authorization

✓ Input Validation

✓ Error Message

✓ Rate Limiting

✓ CORS

---

# 18. Offline Security

SQLite diuji.

✓ Data tetap terenkripsi (Future)

✓ Session tidak bocor

✓ Queue tidak dapat dimanipulasi

✓ Token tidak disimpan dalam plain text

---

# 19. Audit Verification

Semua aktivitas berikut menghasilkan Audit Log.

- Login
- Logout
- Delete Transaction
- Change Role
- OCR Approval
- Email Approval

---

# 20. Dependency Security

Pengujian.

- Dependabot
- CodeQL
- Secret Scan
- Vulnerability Scan

Pipeline gagal apabila ditemukan High Severity Vulnerability.

---

# 21. Security Checklist

Authentication

✓ JWT

✓ Refresh Token

✓ Logout

---

Authorization

✓ Role

✓ Permission

✓ RLS

---

API

✓ HTTPS

✓ Validation

✓ Rate Limit

---

Database

✓ Constraint

✓ RLS

✓ Backup

---

Storage

✓ Private Bucket

✓ File Validation

---

Logging

✓ Audit Log

✓ No Secret Exposure

---

# 22. Security Testing Tools

| Category | Tool |
|----------|------|
| Unit Security | pytest |
| API Security | httpx |
| Dependency Scan | Dependabot |
| Static Analysis | CodeQL |
| Secret Detection | GitHub Secret Scanning |
| Manual Testing | Postman |

Future.

- OWASP ZAP
- Trivy
- Semgrep

---

# 23. Acceptance Criteria

Release dapat dilakukan apabila.

✓ Tidak ada Critical Vulnerability.

✓ Tidak ada High Severity Issue.

✓ Authentication lulus.

✓ Authorization lulus.

✓ API Security lulus.

✓ Audit Log berjalan.

---

# 24. Future Improvements

Roadmap.

- OWASP ZAP Automation
- Penetration Testing
- SAST
- DAST
- Secret Rotation
- Multi-factor Authentication
- Device Trust
- Security Dashboard

---

# 25. Summary

WorthFlow menerapkan Security Testing pada seluruh lapisan sistem mulai dari autentikasi, otorisasi, validasi input, keamanan API, penyimpanan data, hingga infrastruktur.

Pengujian mengikuti prinsip Secure by Design dan mengacu pada praktik terbaik seperti OWASP Top 10 serta Application Security Verification Standard (ASVS), sehingga setiap release memiliki tingkat keamanan yang konsisten dan dapat dipertanggungjawabkan.