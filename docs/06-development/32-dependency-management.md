# Dependency Management

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi pengelolaan dependency pada WorthFlow.

Tujuan utama:

- Menjaga keamanan dependency.
- Mengurangi technical debt.
- Menjamin kompatibilitas antar package.
- Memudahkan proses upgrade.
- Menghindari penggunaan library yang tidak terawat.

Dependency Management merupakan bagian dari Software Supply Chain Security.

---

# 2. Principles

WorthFlow memilih dependency berdasarkan prinsip berikut.

- Stable First
- Community Driven
- Long-term Maintenance
- Security First
- Minimal Dependency
- Explicit Versioning

Tidak menggunakan package hanya karena sedang populer.

---

# 3. Dependency Categories

Dependency dibagi menjadi beberapa kategori.

Core Framework

UI Framework

Networking

Database

State Management

Authentication

Utilities

Testing

Dev Tools

Infrastructure

---

# 4. Frontend Dependencies

## Flutter SDK

Role

Framework utama aplikasi Mobile dan Web.

Reason

- Single codebase
- Cross-platform
- Performa tinggi
- Dukungan komunitas besar

---

## Riverpod

Role

State Management.

Reason

- Compile-time safety
- Testable
- Scalable
- Tidak bergantung pada BuildContext

---

## GoRouter

Role

Routing.

Reason

- Declarative routing
- Deep linking
- Web support

---

## Dio

Role

HTTP Client.

Reason

- Interceptor
- Retry
- Timeout
- Logging
- Multipart Upload

---

## Drift

Role

SQLite ORM.

Reason

- Offline First
- Type-safe
- Migration support

---

## Flutter Secure Storage

Role

Penyimpanan token sensitif.

Reason

- Encrypted storage
- Cross-platform

---

# 5. Backend Dependencies

## FastAPI

Role

REST API Framework.

Reason

- High performance
- Automatic OpenAPI
- Type hints
- Async support

---

## SQLAlchemy

Role

ORM.

Reason

- Mature
- PostgreSQL support
- Migration friendly

---

## Alembic

Role

Migration.

Reason

- Versioned migration
- Reproducible database changes

---

## Pydantic

Role

Validation.

Reason

- Type-safe
- Fast
- Native FastAPI integration

---

## JWT Library

Role

Authentication.

Reason

- Stateless
- Widely adopted

---

# 6. Database Dependencies

Supabase PostgreSQL

Reason.

- Free tier
- Managed database
- Row Level Security
- Storage
- Authentication support

---

# 7. OCR Dependencies

## Tesseract OCR

Role

Local OCR.

Reason

- Offline
- Open Source
- No API cost

---

## Gemini (Optional)

Role

AI Parsing.

Reason

- Mengubah hasil OCR menjadi data transaksi.
- Digunakan hanya ketika diperlukan.

Fallback tetap tersedia tanpa AI.

---

# 8. Infrastructure Dependencies

Docker

Role

Containerization.

GitHub Actions

Role

CI/CD.

Vercel

Role

Frontend Deployment.

Koyeb

Role

Backend Deployment.

---

# 9. Development Dependencies

Python

- Ruff
- Black
- isort
- mypy
- pytest

Flutter

- flutter_test
- integration_test
- build_runner

Semua dependency development tidak ikut dibawa ke Production.

---

# 10. Versioning Strategy

Menggunakan Semantic Versioning.

Format.

```
MAJOR.MINOR.PATCH
```

Contoh.

```
2.1.0
```

Patch update lebih diprioritaskan dibanding major update.

---

# 11. Version Pinning

Semua dependency menggunakan versi yang eksplisit.

Contoh.

```
fastapi==0.116.x
```

atau.

```
flutter_riverpod: ^3.x.x
```

Hindari penggunaan wildcard yang terlalu longgar.

---

# 12. Dependency Evaluation Checklist

Sebelum menambahkan library baru.

Pastikan.

✓ Masih aktif dikembangkan.

✓ Dokumentasi lengkap.

✓ Komunitas besar.

✓ Lisensi kompatibel.

✓ Tidak memiliki kerentanan keamanan.

✓ Memiliki release berkala.

---

# 13. Security Policy

Seluruh dependency dipindai menggunakan.

- Dependabot
- GitHub Security Advisory
- CodeQL

Update keamanan dilakukan sesegera mungkin untuk kerentanan High atau Critical.

---

# 14. Upgrade Policy

Upgrade dilakukan.

Monthly

↓

Check Changelog

↓

Update Staging

↓

Regression Test

↓

Production

Major version tidak langsung digunakan tanpa evaluasi.

---

# 15. Deprecated Dependency

Dependency akan diganti apabila.

- Tidak lagi dipelihara.
- Memiliki banyak CVE.
- Tidak kompatibel dengan versi terbaru.
- Dokumentasi tidak tersedia.
- Performa buruk.

---

# 16. License Policy

Dependency harus menggunakan lisensi yang kompatibel.

Diutamakan.

- Apache 2.0
- MIT
- BSD

Hindari dependency dengan lisensi yang membatasi distribusi atau penggunaan komersial apabila tidak diperlukan.

---

# 17. Dependency Tree

```
Flutter
│
├── Riverpod
├── Dio
├── Drift
├── GoRouter
└── Secure Storage

FastAPI
│
├── SQLAlchemy
├── Alembic
├── Pydantic
└── JWT

Infrastructure
│
├── Docker
├── GitHub Actions
├── Vercel
└── Koyeb
```

---

# 18. Dependency Audit

Audit dilakukan sebelum setiap release.

Checklist.

✓ Dependency terbaru.

✓ Tidak ada High Severity.

✓ Tidak ada dependency usang.

✓ Tidak ada package tidak terpakai.

---

# 19. Future Improvements

Roadmap.

- SBOM (Software Bill of Materials)
- SLSA Compliance
- Sigstore
- Dependency Provenance
- Automatic License Report
- Renovate Bot
- Container Image Scanning

---

# 20. Approved Technology Stack

| Layer | Technology |
|---------|------------|
| Mobile | Flutter |
| Web | Flutter Web |
| Backend | FastAPI |
| Database | PostgreSQL (Supabase) |
| Offline DB | Drift (SQLite) |
| State Management | Riverpod |
| HTTP Client | Dio |
| ORM | SQLAlchemy |
| OCR | Tesseract |
| AI Parsing | Gemini (Optional) |
| CI/CD | GitHub Actions |
| Container | Docker |
| Frontend Hosting | Vercel |
| Backend Hosting | Koyeb |

---

# 21. Summary

WorthFlow menerapkan strategi Dependency Management yang menekankan stabilitas, keamanan, dan keberlanjutan jangka panjang.

Setiap library dipilih berdasarkan kualitas komunitas, dokumentasi, lisensi, dan tingkat pemeliharaan, serta dievaluasi secara berkala melalui proses audit, pembaruan terkontrol, dan pengujian regresi sebelum digunakan di lingkungan Production.