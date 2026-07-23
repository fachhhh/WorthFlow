# API Specification

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan spesifikasi REST API untuk WorthFlow.

API digunakan oleh:

- Mobile App
- Web Dashboard
- OCR Worker
- Email Parser
- Analytics Service

Dokumen ini menjadi acuan utama untuk:

- Backend Development
- Frontend Integration
- API Testing
- API Documentation

---

# 2. API Design Principles

WorthFlow menggunakan pendekatan:

- RESTful API
- Resource-Oriented
- Stateless
- JSON Request & Response
- JWT Authentication
- Versioned Endpoint

Base URL

/api/v1

---

# 3. Response Standard

## Success Response

{
    "success": true,
    "data": { },
    "message": null
}

---

## Error Response

{
    "success": false,
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Amount must be greater than zero."
    }
}

---

# 4. Authentication

Authorization

Bearer JWT

Header

Authorization: Bearer <token>

Authentication dikelola menggunakan Supabase Auth.

---

# 5. API Versioning

Semua endpoint diawali

/api/v1

Contoh

/api/v1/transactions

---

# 6. Resource Groups

WorthFlow membagi API berdasarkan domain.

- Auth
- Family
- Finance
- Assets
- Automation
- Analytics
- Admin

---

# 7. Auth API

POST

/auth/login

Description

Login menggunakan Supabase.

---

POST

/auth/logout

Description

Logout user.

---

GET

/auth/me

Description

Mengambil profil user.

---

# 8. Family API

GET

/family

Description

Informasi keluarga aktif.

---

PATCH

/family

Update informasi keluarga.

---

GET

/family/members

Daftar anggota keluarga.

---

POST

/family/members

Tambah anggota keluarga.

---

PATCH

/family/members/{id}

Update anggota.

---

DELETE

/family/members/{id}

Arsip anggota.

---

# 9. Category API

GET

/categories

List kategori.

---

POST

/categories

Tambah kategori.

---

PATCH

/categories/{id}

Update kategori.

---

DELETE

/categories/{id}

Arsip kategori.

---

# 10. Asset API

GET

/assets

Daftar seluruh aset.

---

GET

/assets/{id}

Detail aset.

---

POST

/assets

Tambah aset.

---

PATCH

/assets/{id}

Update aset.

---

DELETE

/assets/{id}

Arsip aset.

---

GET

/assets/{id}/valuations

Riwayat valuasi.

---

POST

/assets/{id}/valuations

Tambah valuasi.

---

# 11. Transaction API

GET

/transactions

List transaksi.

Parameter

- page
- limit
- category
- member
- asset
- start_date
- end_date

---

GET

/transactions/{id}

Detail transaksi.

---

POST

/transactions

Tambah transaksi manual.

Body

{
    "categoryId": "...",
    "amount": 120000,
    "sourceAssetId": "...",
    "destinationAssetId": null,
    "transactionDate": "...",
    "description": "Lunch"
}

---

PATCH

/transactions/{id}

Edit transaksi.

---

DELETE

/transactions/{id}

Soft delete.

---

# 12. Draft API

GET

/drafts

Daftar draft.

---

GET

/drafts/{id}

Detail draft.

---

POST

/drafts/{id}/approve

Approve draft.

---

POST

/drafts/{id}/reject

Reject draft.

---

PATCH

/drafts/{id}

Edit draft sebelum approve.

---

# 13. Email API

GET

/email/accounts

List akun email.

---

POST

/email/accounts

Tambah akun email.

---

DELETE

/email/accounts/{id}

Hapus akun.

---

POST

/email/sync

Sinkronisasi email.

---

GET

/email/messages

Daftar email.

---

GET

/email/messages/{id}

Detail email.

---

# 14. OCR API

POST

/ocr/upload

Upload receipt.

Multipart Form Data

image

---

GET

/ocr/jobs/{id}

Status OCR.

---

GET

/ocr/results/{id}

Hasil OCR.

---

POST

/ocr/retry/{id}

Retry OCR.

---

# 15. Analytics API

GET

/analytics/dashboard

Dashboard utama.

---

GET

/analytics/cashflow

Cash Flow.

---

GET

/analytics/net-worth

Net Worth.

---

GET

/analytics/category

Analisis kategori.

---

GET

/analytics/monthly

Laporan bulanan.

---

GET

/analytics/yearly

Laporan tahunan.

---

# 16. Sync API

POST

/sync/upload

Upload perubahan lokal.

---

GET

/sync/download

Download perubahan terbaru.

---

POST

/sync/resolve

Resolve konflik sinkronisasi.

---

# 17. Audit API

GET

/audit

Riwayat aktivitas.

---

GET

/audit/{id}

Detail log.

---

# 18. Admin API

GET

/admin/health

Health Check.

---

GET

/admin/version

Versi backend.

---

GET

/admin/config

Konfigurasi publik.

---

# 19. HTTP Status Code

200

OK

---

201

Created

---

204

No Content

---

400

Bad Request

---

401

Unauthorized

---

403

Forbidden

---

404

Not Found

---

409

Conflict

---

422

Validation Error

---

500

Internal Server Error

---

# 20. Pagination Standard

Response

{
    "data": [],
    "pagination": {
        "page": 1,
        "limit": 20,
        "total": 315,
        "totalPages": 16
    }
}

---

# 21. Filtering Standard

Semua endpoint list mendukung:

page

limit

sort

order

search

Contoh

GET /transactions?page=1&limit=20

---

# 22. Sorting

sort

transaction_date

amount

created_at

name

order

asc

desc

---

# 23. Error Codes

AUTH_REQUIRED

ACCESS_DENIED

INVALID_TOKEN

RESOURCE_NOT_FOUND

VALIDATION_ERROR

EMAIL_ALREADY_EXISTS

SYNC_CONFLICT

OCR_FAILED

DRAFT_NOT_FOUND

TRANSACTION_NOT_FOUND

---

# 24. Security Rules

Semua endpoint wajib:

JWT Authentication

↓

Family Validation

↓

Input Validation

↓

Business Validation

↓

Audit Logging

↓

Response

---

# 25. Rate Limiting

Default

120 request / minute

Endpoint OCR

10 upload / minute

Endpoint Email Sync

5 request / minute

---

# 26. API Lifecycle

Client

↓

JWT Authentication

↓

REST Endpoint

↓

FastAPI Router

↓

Service Layer

↓

Repository Layer

↓

PostgreSQL

↓

Response

---

# 27. Future API

GraphQL

Webhook

AI Recommendation API

Budget API

Notification API

Investment API

---

# 28. Summary

WorthFlow menggunakan REST API berbasis domain (Bounded Context), bukan berdasarkan struktur tabel database.

Pendekatan ini menghasilkan API yang:

- mudah dipahami
- mudah dipelihara
- konsisten
- scalable
- siap dikembangkan menjadi platform finansial yang lebih besar.