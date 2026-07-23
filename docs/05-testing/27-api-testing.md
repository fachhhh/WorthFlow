# API Testing

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi dan skenario pengujian seluruh REST API pada WorthFlow.

Tujuan utama:

- Memastikan seluruh endpoint bekerja sesuai spesifikasi.
- Memvalidasi request dan response.
- Menguji keamanan endpoint.
- Menguji performa API.
- Menjamin kompatibilitas antara Mobile, Web, dan Backend.

Dokumen ini merupakan implementasi dari:

- 14-api-spec.md
- 15-auth-flow.md
- 25-test-strategy.md
- 26-test-cases.md

---

# 2. API Testing Scope

Seluruh endpoint berikut wajib diuji.

Authentication

- Login
- Refresh Token
- Logout

Family

- Create Family
- Invite Member
- List Members

Transaction

- CRUD Transaction
- Filter
- Pagination

Asset

- CRUD Asset

Budget

- CRUD Budget

Receipt

- Upload
- OCR
- Draft

Email

- Sync
- Draft
- Approve

Analytics

- Dashboard
- Monthly Summary

Admin

- Health Check
- Audit Log

---

# 3. Testing Levels

API diuji pada beberapa level.

```
Request Validation
        │
        ▼
Authentication
        │
        ▼
Authorization
        │
        ▼
Business Logic
        │
        ▼
Database
        │
        ▼
Response Validation
```

---

# 4. Request Validation

Semua endpoint wajib menguji.

✓ Required Field

✓ Optional Field

✓ Empty Value

✓ Invalid Data Type

✓ Maximum Length

✓ Minimum Length

✓ Invalid Enum

✓ Invalid Date

---

Contoh.

POST /transactions

Valid

```json
{
  "amount":50000,
  "category_id":"uuid",
  "transaction_date":"2026-07-20"
}
```

Invalid.

```json
{
  "amount":"abc"
}
```

Expected.

422 Validation Error

---

# 5. Authentication Testing

Endpoint.

POST /auth/login

Test.

✓ Email valid

✓ Password valid

✓ Wrong Password

✓ Unknown Email

✓ Expired Token

✓ Refresh Token

✓ Logout

Expected.

Status Code sesuai.

---

# 6. Authorization Testing

Semua endpoint wajib diuji menggunakan role.

Owner

Admin

Member

Viewer

Contoh.

Member mencoba.

DELETE /members/{id}

Expected.

403 Forbidden

---

# 7. CRUD Testing

Semua resource mengikuti pola berikut.

Create

↓

Read

↓

Update

↓

Delete

Yang diuji.

- Success
- Validation
- Unauthorized
- Forbidden
- Duplicate
- Conflict

---

# 8. Transaction API

Endpoint.

GET /transactions

Test.

✓ Pagination

✓ Filter

✓ Sort

✓ Search

✓ Date Range

✓ Category

✓ Member

✓ Amount

---

POST /transactions

Test.

✓ Valid Transaction

✓ Invalid Amount

✓ Missing Category

✓ Future Date

✓ Duplicate Request

---

PATCH /transactions/{id}

Test.

✓ Update Success

✓ Transaction Not Found

✓ Unauthorized

---

DELETE /transactions/{id}

Test.

✓ Soft Delete

✓ Audit Log Created

---

# 9. Receipt API

Endpoint.

POST /receipts

Test.

✓ Upload Image

✓ Invalid File

✓ Unsupported Format

✓ Large File

✓ Duplicate Upload

Expected.

Receipt berhasil dibuat.

---

POST /receipts/{id}/ocr

Test.

✓ OCR Success

✓ OCR Failed

✓ AI Parsing Failed

✓ Retry OCR

---

POST /receipts/{id}/approve

Test.

✓ Draft menjadi Transaction

✓ Duplicate Approval

---

# 10. Email Parser API

POST /emails/sync

Test.

✓ Sync Success

✓ Duplicate Email

✓ Invalid Connection

✓ Parser Error

---

POST /emails/{id}/approve

Test.

✓ Draft menjadi Transaction

✓ Duplicate Approval

---

# 11. Budget API

Test.

✓ Create Budget

✓ Update Budget

✓ Delete Budget

✓ Over Budget

✓ Remaining Budget

---

# 12. Asset API

Test.

✓ Create Asset

✓ Edit Asset

✓ Delete Asset

✓ Asset Value

✓ Asset History

---

# 13. Dashboard API

Endpoint.

GET /dashboard

Test.

✓ Monthly Expense

✓ Monthly Income

✓ Asset Summary

✓ Budget Summary

✓ Category Summary

---

# 14. Health Check API

GET /admin/health

Expected.

```json
{
  "status":"healthy"
}
```

Status Code.

200

---

# 15. Response Validation

Semua endpoint harus memvalidasi.

Status Code

Header

JSON Schema

Timestamp

Pagination

Contoh.

```json
{
  "success":true,
  "data":{},
  "meta":{},
  "message":"Success"
}
```

---

# 16. Error Handling

Response.

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

422 Validation Error

429 Too Many Requests

500 Internal Server Error

Semua response mengikuti format yang konsisten.

---

# 17. Performance Testing

Target.

| Endpoint | Target |
|------------|---------|
| Login | <300 ms |
| Dashboard | <500 ms |
| Transaction | <500 ms |
| Upload Receipt | <2 s |
| OCR | <5 s |
| Email Sync | <10 s |

---

# 18. Security Testing

Pengujian.

✓ SQL Injection

✓ JWT Manipulation

✓ Expired Token

✓ Missing Token

✓ Invalid Role

✓ Brute Force

✓ Rate Limiting

✓ IDOR

---

# 19. Database Verification

Setelah API berhasil.

Verifikasi.

Database berubah.

↓

Audit Log dibuat.

↓

Sync Queue diperbarui.

↓

Analytics berubah.

---

# 20. Mocking Strategy

Unit Test menggunakan.

Mock Database

Mock OCR

Mock Gemini

Mock Email Service

Tujuan.

Test tidak bergantung pada internet.

---

# 21. Automation

API Test dijalankan melalui.

pytest

↓

httpx

↓

GitHub Actions

↓

Coverage Report

---

# 22. Coverage Target

| Endpoint | Coverage |
|-----------|----------|
| Authentication | ≥95% |
| Transaction | ≥90% |
| Asset | ≥90% |
| Budget | ≥90% |
| Receipt | ≥90% |
| Email | ≥90% |
| Dashboard | ≥85% |

---

# 23. Future Improvements

Roadmap.

- Contract Testing
- OpenAPI Validation
- Postman Collection
- Newman Automation
- Chaos API Testing
- Load API Testing

---

# 24. Summary

Seluruh REST API pada WorthFlow diuji mulai dari validasi request, autentikasi, otorisasi, business logic, hingga perubahan data pada database.

Setiap endpoint memiliki target performa, pengujian keamanan, serta validasi response yang terintegrasi dengan pipeline CI/CD sehingga kualitas layanan backend dapat dipertahankan secara konsisten sebelum setiap proses deployment.