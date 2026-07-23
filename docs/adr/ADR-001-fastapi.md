# ADR-001: Use FastAPI as the Backend Framework

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow membutuhkan backend yang mampu melayani aplikasi Mobile (Flutter), Web (Flutter Web), serta beberapa service pendukung seperti OCR Worker dan Email Parser.

Backend akan bertanggung jawab untuk:

- Authentication & Authorization
- Family Management
- Transaction Management
- Receipt Management
- OCR Draft Approval
- Budget Management
- Analytics
- Offline Synchronization
- REST API
- Background Jobs

Backend juga harus mudah dikembangkan oleh satu developer pada fase MVP namun tetap dapat diskalakan ketika aplikasi berkembang.

Selain itu, seluruh API harus terdokumentasi dengan baik agar integrasi antara frontend dan backend menjadi lebih mudah.

---

# Decision

WorthFlow menggunakan **FastAPI** sebagai backend framework utama.

FastAPI akan menjadi fondasi seluruh REST API yang digunakan oleh:

- Flutter Mobile
- Flutter Web
- OCR Worker
- Email Parser
- Future External Integrations

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## High Performance

FastAPI dibangun di atas Starlette dan Uvicorn yang memiliki performa sangat baik untuk aplikasi asynchronous.

Hal ini penting karena WorthFlow memiliki beberapa proses I/O seperti:

- Database Query
- OCR Processing
- Email Parsing
- File Upload
- Synchronization

---

## Excellent Developer Experience

FastAPI menggunakan:

- Python Type Hint
- Pydantic
- Automatic Validation

Sehingga error dapat ditemukan lebih awal saat proses development.

---

## Automatic API Documentation

FastAPI secara otomatis menghasilkan dokumentasi:

- OpenAPI
- Swagger UI
- ReDoc

Hal ini mengurangi pekerjaan dokumentasi manual.

---

## Async Support

WorthFlow membutuhkan operasi asynchronous untuk:

- Upload Receipt
- OCR Worker
- Sync Engine
- Email Processing

FastAPI mendukung asynchronous programming secara native menggunakan `async` dan `await`.

---

## Strong Python Ecosystem

WorthFlow menggunakan beberapa library Python seperti:

- SQLAlchemy
- Alembic
- Pydantic
- Tesseract OCR
- Pillow
- Pandas (future)

Seluruh library tersebut memiliki integrasi yang baik dengan FastAPI.

---

## Easy Deployment

FastAPI dapat dijalankan menggunakan:

- Docker
- Koyeb
- Railway
- Render
- VPS
- Kubernetes (Future)

Hal ini memberikan fleksibilitas deployment.

---

# Alternatives Considered

## Django

### Pros

- Sangat mature
- Ekosistem besar
- Banyak plugin
- Admin Panel bawaan

### Cons

- Lebih berat untuk kebutuhan REST API.
- Banyak fitur yang tidak digunakan pada MVP.
- Async support tidak sebaik FastAPI.

Decision:

Not Selected.

---

## Flask

### Pros

- Sangat ringan
- Mudah dipelajari

### Cons

- Terlalu minimal.
- Banyak komponen harus dipilih sendiri.
- Validasi tidak terintegrasi.
- Dokumentasi OpenAPI memerlukan konfigurasi tambahan.

Decision:

Not Selected.

---

## Node.js (Express)

### Pros

- Banyak developer JavaScript.
- Ekosistem besar.

### Cons

- Tidak sejalan dengan stack OCR yang menggunakan Python.
- Perlu berpindah bahasa pemrograman antara backend dan worker.

Decision:

Not Selected.

---

## NestJS

### Pros

- Struktur project sangat rapi.
- Dependency Injection bawaan.

### Cons

- Memerlukan TypeScript.
- Tidak memanfaatkan ekosistem Python untuk OCR.

Decision:

Not Selected.

---

# Consequences

## Positive

- Performa tinggi.
- Dokumentasi API otomatis.
- Type-safe melalui Pydantic.
- Native async support.
- Mudah di-deploy.
- Sangat cocok dengan OCR pipeline berbasis Python.
- Komunitas berkembang pesat.
- Kode lebih mudah dipelihara.

---

## Negative

- Ekosistem lebih kecil dibanding Django.
- Belum memiliki admin panel bawaan.
- Membutuhkan pemahaman asynchronous programming.
- Sebagian library Python lama belum sepenuhnya async.

---

# Impact

Keputusan ini memengaruhi beberapa dokumen lain.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Backend Architecture |
| 10-ocr-pipeline.md | OCR Worker Integration |
| 14-api-spec.md | REST API |
| 15-auth-flow.md | Authentication |
| 16-security-design.md | API Security |
| 20-cicd.md | Backend Build |
| 21-deployment-guide.md | Backend Deployment |
| 27-api-testing.md | API Testing |

---

# Risks

Risiko utama.

- Ketergantungan pada ekosistem Python.
- Perubahan besar pada FastAPI dapat memerlukan penyesuaian kode.
- Async yang tidak digunakan dengan benar dapat menurunkan performa.

Mitigasi.

- Mengikuti Semantic Versioning.
- Menggunakan pinned dependency.
- Menjalankan regression test sebelum upgrade major version.

---

# Implementation Notes

Backend akan menggunakan arsitektur berlapis.

```
Client

↓

FastAPI Router

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy ORM

↓

PostgreSQL (Supabase)
```

Seluruh endpoint akan:

- Menggunakan JWT Authentication.
- Menggunakan Pydantic Validation.
- Mengembalikan response JSON.
- Mengikuti RESTful API Convention.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- FastAPI tidak lagi memenuhi kebutuhan performa.
- Dibutuhkan arsitektur event-driven yang berbeda.
- Terjadi perubahan besar pada kebutuhan bisnis.
- Framework lain memberikan keuntungan signifikan.

Review dilakukan minimal setiap major release.

---

# References

Internal Documentation:

- 06-system-architecture.md
- 14-api-spec.md
- 15-auth-flow.md
- 20-cicd.md
- 21-deployment-guide.md
- 32-dependency-management.md
- 36-architecture-decision-records.md

External References:

- https://fastapi.tiangolo.com/
- https://docs.pydantic.dev/
- https://www.sqlalchemy.org/

---

# Decision Summary

WorthFlow menggunakan **FastAPI** sebagai backend framework utama karena menawarkan kombinasi performa tinggi, dukungan asynchronous, dokumentasi API otomatis, validasi berbasis tipe, serta integrasi yang sangat baik dengan ekosistem Python yang digunakan untuk OCR dan pemrosesan data. Keputusan ini mendukung tujuan proyek untuk membangun MVP yang ringan, mudah dikembangkan, dan siap berkembang menjadi sistem yang lebih besar di masa depan.