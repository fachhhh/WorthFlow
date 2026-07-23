# 25. Test Strategy

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi pengujian (Testing Strategy) pada WorthFlow.

Tujuan utama testing adalah:

- Memastikan setiap fitur berjalan sesuai kebutuhan.
- Mengurangi bug sebelum aplikasi dirilis.
- Menjaga stabilitas sistem ketika ada perubahan kode.
- Mendukung Continuous Integration (CI).
- Menjamin kualitas aplikasi dalam jangka panjang.

Dokumen ini menjadi acuan seluruh proses Quality Assurance (QA).

---

# 2. Testing Philosophy

WorthFlow menerapkan prinsip:

> **Test Early, Test Often, Automate Whenever Possible**

Setiap perubahan kode harus:

- Dapat diuji.
- Dapat direproduksi.
- Tidak merusak fitur yang sudah ada.
- Memiliki tingkat kepercayaan (confidence) yang tinggi sebelum dirilis.

---

# 3. Testing Pyramid

WorthFlow menggunakan pendekatan Testing Pyramid.

```
                End-to-End Test
                     ▲
             Integration Test
                     ▲
               API / Service Test
                     ▲
                Widget Test
                     ▲
                 Unit Test
```

Proporsi pengujian:

| Layer | Approximation |
|---------|--------------|
| Unit Test | 60% |
| Widget Test | 20% |
| API / Service Test | 10% |
| Integration Test | 7% |
| End-to-End Test | 3% |

Semakin ke atas jumlah test lebih sedikit tetapi cakupan lebih luas.

---

# 4. Scope of Testing

Seluruh komponen akan diuji.

Frontend

- Flutter Mobile
- Flutter Web

Backend

- FastAPI

Infrastructure

- Database
- Storage
- Authentication

Business Feature

- Transaction
- Asset
- Budget
- OCR
- Email Parser
- Offline Sync

---

# 5. Testing Levels

WorthFlow menggunakan lima level pengujian.

## Unit Testing

Menguji fungsi atau class secara individual.

Contoh.

- Currency Formatter
- Budget Calculator
- Category Validator
- Transaction Mapper

Target:

Cepat dan deterministik.

---

## Widget Testing

Menguji komponen UI Flutter.

Contoh.

- Login Form
- Transaction Card
- Budget Progress
- Receipt Card

Target.

UI tetap konsisten ketika terjadi perubahan.

---

## API Testing

Menguji endpoint FastAPI.

Contoh.

```
POST /auth/login

GET /transactions

POST /receipts

GET /assets
```

Target.

- HTTP Status
- Response Schema
- Validation
- Authorization

---

## Integration Testing

Menguji interaksi antar service.

Contoh.

Flutter

↓

API

↓

Supabase

↓

Storage

↓

Response

Target.

Semua komponen bekerja bersama dengan benar.

---

## End-to-End Testing

Mensimulasikan alur pengguna sebenarnya.

Contoh.

Login

↓

Tambah transaksi

↓

Upload receipt

↓

OCR

↓

Approve

↓

Dashboard Update

↓

Logout

---

# 6. Functional Testing

Memastikan seluruh fitur sesuai PRD.

Meliputi.

- Authentication
- Family Management
- Transaction
- Asset
- Budget
- Analytics
- OCR
- Email Sync
- Offline Sync

---

# 7. Non-Functional Testing

Selain fitur.

WorthFlow juga menguji.

Performance

Security

Reliability

Availability

Usability

Accessibility

Compatibility

---

# 8. Regression Testing

Regression Test dijalankan setiap.

- Merge ke develop
- Merge ke main
- Sebelum release

Tujuan.

Memastikan fitur lama tetap berjalan.

---

# 9. Smoke Testing

Setelah deployment.

Minimal diuji.

✓ Login

✓ Dashboard

✓ Transaction

✓ OCR

✓ Email Sync

✓ Offline Sync

Jika Smoke Test gagal.

↓

Deployment dianggap gagal.

---

# 10. Performance Testing

Target performa.

| Component | Target |
|------------|---------|
| Login | <300 ms |
| Dashboard | <500 ms |
| Transaction API | <500 ms |
| OCR | <5 detik |
| Email Sync | <10 detik |
| Offline Sync | <30 detik |

---

# 11. Security Testing

Pengujian keamanan meliputi.

- Authentication
- Authorization
- JWT Validation
- SQL Injection
- XSS
- CSRF
- Rate Limiting
- Secret Exposure

---

# 12. Offline Testing

Karena WorthFlow bersifat Offline First.

Pengujian meliputi.

Internet Mati

↓

Tambah transaksi

↓

Masuk SQLite

↓

Internet Aktif

↓

Sync

↓

Dashboard Update

---

# 13. OCR Testing

Skenario.

Receipt

↓

OCR

↓

AI Parsing

↓

Draft

↓

Approve

↓

Transaction

Yang diuji.

- OCR Accuracy
- Parsing Accuracy
- Response Time
- Retry Mechanism

---

# 14. Email Testing

Skenario.

Email Masuk

↓

Parser

↓

Draft

↓

Approve

↓

Transaction

Yang diuji.

- Email Download
- Parsing
- Duplicate Detection
- Error Handling

---

# 15. Database Testing

Pengujian.

- Constraint
- Foreign Key
- Index
- Cascade
- Migration
- RLS Policy

---

# 16. Automation Testing

Semua test otomatis dijalankan melalui GitHub Actions.

Workflow.

Push

↓

Lint

↓

Unit Test

↓

Widget Test

↓

API Test

↓

Build

↓

Deploy

---

# 17. Test Data Strategy

Menggunakan data terpisah.

Development

↓

Dummy Data

Staging

↓

Synthetic Data

Production

↓

Real Family Data

Tidak diperbolehkan menggunakan data Production untuk proses testing.

---

# 18. Exit Criteria

Release hanya dapat dilakukan apabila.

✓ Seluruh Unit Test lulus.

✓ Widget Test lulus.

✓ API Test lulus.

✓ Integration Test lulus.

✓ Tidak ada Critical Bug.

✓ Smoke Test berhasil.

---

# 19. Test Coverage Target

| Component | Minimum Coverage |
|-----------|------------------|
| Backend | ≥ 80% |
| Flutter Business Logic | ≥ 80% |
| Flutter UI | ≥ 60% |
| API | ≥ 90% |
| Core Utility | ≥ 90% |

Coverage digunakan sebagai indikator, bukan satu-satunya ukuran kualitas.

---

# 20. Testing Responsibilities

| Role | Responsibility |
|------|----------------|
| Developer | Unit Test, Widget Test |
| CI/CD | Automation Testing |
| QA (Future) | Manual & Regression Test |
| Product Owner | User Acceptance Test |

Pada tahap MVP, seluruh aktivitas QA dilakukan oleh Developer.

---

# 21. Testing Tools

| Layer | Tool |
|---------|------|
| Flutter Unit Test | flutter_test |
| Widget Test | flutter_test |
| Integration Test | integration_test |
| Backend Unit Test | pytest |
| API Test | httpx + pytest |
| Mocking | unittest.mock / mocktail |
| Coverage | coverage.py, lcov |
| CI | GitHub Actions |

---

# 22. Future Improvements

Roadmap.

- Visual Regression Testing
- Snapshot Testing
- Load Testing
- Chaos Engineering
- Automated Performance Benchmark
- AI-assisted Test Generation

---

# 23. Summary

WorthFlow menerapkan strategi pengujian berlapis (Layered Testing Strategy) yang mencakup Unit Test, Widget Test, API Test, Integration Test, dan End-to-End Test.

Seluruh pengujian diintegrasikan dengan pipeline CI/CD sehingga setiap perubahan kode divalidasi secara otomatis sebelum dirilis ke Production. Pendekatan ini membantu menjaga kualitas aplikasi, mengurangi regresi, dan memastikan seluruh fitur tetap berjalan sesuai kebutuhan sepanjang siklus pengembangan.