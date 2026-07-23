# Test Cases

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan seluruh skenario pengujian fungsional dan non-fungsional pada WorthFlow.

Tujuan dokumen ini adalah:

- Memastikan seluruh kebutuhan pada PRD telah diuji.
- Menjadi acuan regression testing.
- Menjadi referensi User Acceptance Test (UAT).
- Mendukung proses Continuous Integration (CI).

Dokumen ini merupakan implementasi dari:

- 02-prd.md
- 03-user-stories.md
- 25-test-strategy.md

---

# 2. Test Case Structure

Setiap test case memiliki format berikut.

| Field | Description |
|---------|------------|
| Test ID | Identitas unik |
| Module | Modul yang diuji |
| Requirement | Requirement terkait |
| Priority | High / Medium / Low |
| Preconditions | Kondisi sebelum pengujian |
| Steps | Langkah pengujian |
| Expected Result | Hasil yang diharapkan |
| Automation | Manual / Automated |

---

# 3. Authentication

## TC-AUTH-001

Module

Authentication

Requirement

User Login

Priority

High

Precondition

Member telah terdaftar.

Steps

1. Buka aplikasi.
2. Masukkan email.
3. Masukkan password.
4. Tekan Login.

Expected Result

- Login berhasil.
- JWT diterima.
- Dashboard terbuka.

Automation

✅ Automated

---

## TC-AUTH-002

Login gagal.

Expected.

- Password salah.
- Pesan error muncul.
- Tidak membuat session.

---

## TC-AUTH-003

Expired Token.

Expected.

- Refresh Token digunakan.
- User tetap login.

---

## TC-AUTH-004

Logout.

Expected.

- Session dihapus.
- SQLite tetap tersimpan.
- Kembali ke Login Screen.

---

# 4. Family Management

## TC-FAM-001

Membuat Family baru.

Expected.

Family berhasil dibuat.

---

## TC-FAM-002

Mengundang anggota keluarga.

Expected.

Invitation berhasil dibuat.

---

## TC-FAM-003

Menerima undangan.

Expected.

Member bergabung ke Family.

---

## TC-FAM-004

Mengubah Role.

Expected.

Permission berubah sesuai role.

---

# 5. Transaction

## TC-TXN-001

Tambah transaksi manual.

Expected.

Transaction berhasil tersimpan.

---

## TC-TXN-002

Edit transaksi.

Expected.

Perubahan muncul pada Dashboard.

---

## TC-TXN-003

Delete transaksi.

Expected.

Soft Delete berhasil.

Audit Log dibuat.

---

## TC-TXN-004

Input nominal negatif.

Expected.

Validation Error.

---

## TC-TXN-005

Tanggal transaksi di masa depan.

Expected.

Warning muncul.

---

# 6. Asset

## TC-AST-001

Tambah Asset.

Expected.

Asset muncul.

---

## TC-AST-002

Edit Asset.

Expected.

Nilai Asset berubah.

---

## TC-AST-003

Hapus Asset.

Expected.

Soft Delete.

---

# 7. Budget

## TC-BUD-001

Tambah Budget.

Expected.

Budget berhasil dibuat.

---

## TC-BUD-002

Budget terlampaui.

Expected.

Warning muncul.

---

## TC-BUD-003

Progress Budget.

Expected.

Persentase sesuai transaksi.

---

# 8. Receipt OCR

## TC-OCR-001

Upload receipt.

Expected.

Receipt tersimpan.

---

## TC-OCR-002

OCR berhasil.

Expected.

Draft Transaction dibuat.

---

## TC-OCR-003

OCR gagal.

Expected.

Retry tersedia.

---

## TC-OCR-004

Approve Draft.

Expected.

Transaction dibuat.

---

## TC-OCR-005

Edit Draft.

Expected.

Perubahan tersimpan.

---

# 9. Email Parser

## TC-MAIL-001

Sinkronisasi Email.

Expected.

Email berhasil diambil.

---

## TC-MAIL-002

Parser berhasil.

Expected.

Draft dibuat.

---

## TC-MAIL-003

Duplicate Email.

Expected.

Tidak membuat transaksi baru.

---

## TC-MAIL-004

Approve Draft.

Expected.

Transaction dibuat.

---

# 10. Offline First

## TC-OFF-001

Internet mati.

Tambah transaksi.

Expected.

SQLite bertambah.

---

## TC-OFF-002

Internet aktif.

Expected.

Sync otomatis.

---

## TC-OFF-003

Conflict.

Expected.

Conflict Resolver berjalan.

---

# 11. Analytics

## TC-ANA-001

Dashboard Bulanan.

Expected.

Data sesuai transaksi.

---

## TC-ANA-002

Filter Tahun.

Expected.

Grafik berubah.

---

## TC-ANA-003

Cash Flow.

Expected.

Income & Expense sesuai.

---

# 12. Notification

## TC-NOTIF-001

Budget Warning.

Expected.

Notifikasi muncul.

---

## TC-NOTIF-002

Sync Success.

Expected.

Snackbar muncul.

---

# 13. API

## TC-API-001

GET Transaction.

Expected.

200 OK.

---

## TC-API-002

POST Transaction.

Expected.

201 Created.

---

## TC-API-003

Unauthorized.

Expected.

401.

---

## TC-API-004

Forbidden.

Expected.

403.

---

## TC-API-005

Validation Error.

Expected.

422.

---

# 14. Database

## TC-DB-001

Foreign Key.

Expected.

Constraint aktif.

---

## TC-DB-002

Cascade Delete.

Expected.

Soft Delete.

---

## TC-DB-003

Migration.

Expected.

Berhasil dijalankan.

---

# 15. Security

## TC-SEC-001

SQL Injection.

Expected.

Ditolak.

---

## TC-SEC-002

XSS.

Expected.

Input disanitasi.

---

## TC-SEC-003

JWT Invalid.

Expected.

401.

---

## TC-SEC-004

Rate Limit.

Expected.

429 Too Many Requests.

---

# 16. Performance

## TC-PERF-001

Login.

Expected.

<300 ms.

---

## TC-PERF-002

Dashboard.

Expected.

<500 ms.

---

## TC-PERF-003

OCR.

Expected.

<5 detik.

---

# 17. Accessibility

## TC-A11Y-001

Text Scaling.

Expected.

UI tetap rapi.

---

## TC-A11Y-002

Dark Mode.

Expected.

Kontras memenuhi standar.

---

## TC-A11Y-003

Screen Reader.

Expected.

Komponen terbaca.

---

# 18. Regression Suite

Regression wajib mencakup.

✓ Login

✓ Dashboard

✓ Transaction

✓ Asset

✓ Budget

✓ OCR

✓ Email Parser

✓ Offline Sync

✓ Analytics

---

# 19. Smoke Suite

Sebelum release.

✓ Login

✓ Dashboard

✓ API

✓ OCR

✓ Email Parser

---

# 20. UAT Checklist

Product Owner melakukan validasi.

✓ Semua User Story selesai.

✓ Tidak ada Critical Bug.

✓ Data sesuai.

✓ UX sesuai.

---

# 21. Traceability Matrix

| Requirement | User Story | Test Case |
|------------|------------|-----------|
| Login | US-001 | TC-AUTH-001 |
| Add Transaction | US-010 | TC-TXN-001 |
| OCR Receipt | US-023 | TC-OCR-001 |
| Email Parsing | US-030 | TC-MAIL-001 |
| Offline Sync | US-041 | TC-OFF-001 |

---

# 22. Exit Criteria

Release dinyatakan layak apabila.

- 100% High Priority Test Pass.
- Tidak ada Critical Bug.
- Regression Test Pass.
- Smoke Test Pass.
- UAT Disetujui.

---

# 23. Future Improvements

Roadmap.

- Automated UI Testing
- Visual Regression Test
- AI-generated Test Cases
- Cross-platform Device Testing
- Load Testing
- Chaos Testing

---

# 24. Summary

Dokumen ini mendefinisikan seluruh skenario pengujian WorthFlow mulai dari autentikasi, transaksi, aset, OCR, email parser, offline synchronization, hingga keamanan dan performa.

Seluruh test case dirancang agar dapat ditelusuri kembali ke Product Requirement Document (PRD) dan User Stories melalui Traceability Matrix, sehingga setiap requirement memiliki cakupan pengujian yang jelas dan dapat divalidasi sebelum aplikasi dirilis ke lingkungan Production.