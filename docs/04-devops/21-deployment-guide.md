# Deployment Guide

Version: 1.0

---

# 1. Purpose

Dokumen ini menjelaskan langkah-langkah deployment WorthFlow mulai dari proses setup hingga aplikasi siap digunakan pada lingkungan Production.

Deployment Guide mencakup:

- Local Development
- Backend Deployment
- Web Deployment
- Mobile Distribution
- Database Migration
- Environment Configuration
- Verification
- Rollback

Dokumen ini melengkapi:

- 19-environments.md
- 20-cicd.md

---

# 2. Deployment Architecture

WorthFlow menggunakan arsitektur deployment berikut.

```

                GitHub Repository
                        │
                        ▼
                GitHub Actions
          ┌─────────────┴─────────────┐
          ▼                           ▼
     Flutter Web                 FastAPI Backend
          │                           │
          ▼                           ▼
       Vercel                     Docker Image
                                      │
                                      ▼
                                    Koyeb
                                      │
                                      ▼
                                 Supabase API
                                      │
                                      ▼
                           PostgreSQL + Storage

```

---

# 3. Prerequisites

Sebelum melakukan deployment, pastikan tersedia:

## Software

- Git
- Flutter SDK
- Python 3.12+
- Docker
- Docker Compose
- Make (Optional)

---

## Accounts

- GitHub
- Supabase
- Koyeb
- Vercel
- Google AI Studio (Gemini API)

---

## Secrets

- SUPABASE_URL
- SUPABASE_ANON_KEY
- SUPABASE_SERVICE_ROLE_KEY
- DATABASE_URL
- GEMINI_API_KEY

---

# 4. Initial Setup

Clone repository.

```bash
git clone https://github.com/<username>/worthflow.git

cd worthflow
```

Install dependency Flutter.

```bash
flutter pub get
```

Install backend dependency.

```bash
pip install -r requirements.txt
```

---

# 5. Environment Configuration

Copy file.

```bash
cp .env.example .env
```

Isi seluruh Environment Variable.

Contoh.

```env
APP_ENV=development

SUPABASE_URL=...

SUPABASE_ANON_KEY=...

DATABASE_URL=...

GEMINI_API_KEY=...
```

Jangan pernah melakukan commit terhadap file `.env`.

---

# 6. Database Migration

Jalankan migration.

```bash
alembic upgrade head
```

Verifikasi seluruh tabel berhasil dibuat.

- families
- members
- assets
- transactions
- receipts
- audit_logs
- sync_queue

---

# 7. Local Development

Backend.

```bash
uvicorn app.main:app --reload
```

Frontend.

```bash
flutter run
```

Web.

```bash
flutter run -d chrome
```

Pastikan aplikasi dapat:

- Login
- Sinkronisasi
- Membuat transaksi
- Upload receipt

---

# 8. Backend Deployment

Backend dikemas menggunakan Docker.

Build image.

```bash
docker build -t worthflow-backend .
```

Push ke registry (future).

Deployment dilakukan melalui Koyeb.

Pastikan:

- Docker Build berhasil.
- Environment Variable telah dimuat.
- Health Check aktif.

---

# 9. Web Deployment

Flutter Web dibangun menggunakan:

```bash
flutter build web
```

Deployment otomatis melalui GitHub Actions ke Vercel.

Setelah deployment:

- Verifikasi halaman login.
- Verifikasi dashboard.
- Verifikasi koneksi API.

---

# 10. Mobile Deployment

Android.

```bash
flutter build appbundle --release
```

Output:

```
build/app/outputs/bundle/release/
```

APK dapat digunakan untuk:

- Internal Testing
- Distribusi ke anggota keluarga

Future.

Google Play Internal Testing.

---

# 11. Backend Verification

Lakukan pengecekan endpoint.

```http
GET /admin/health
```

Response.

```json
{
  "status": "healthy"
}
```

Pastikan:

- Database Connected
- Storage Connected
- API berjalan

---

# 12. Database Verification

Pastikan:

✓ Migration berhasil

✓ Constraint aktif

✓ RLS aktif

✓ Seed Data tersedia

---

# 13. Storage Verification

Upload receipt.

↓

Pastikan file masuk ke bucket.

↓

OCR Worker membaca file.

↓

Draft berhasil dibuat.

---

# 14. Email Verification

Hubungkan akun email.

↓

Sync Email.

↓

Parser berjalan.

↓

Draft muncul.

↓

Approve Draft.

↓

Transaction berhasil dibuat.

---

# 15. Offline Verification

Matikan koneksi internet.

↓

Tambah transaksi.

↓

Pastikan tersimpan pada SQLite.

↓

Aktifkan internet.

↓

Sinkronisasi berhasil.

↓

Dashboard diperbarui.

---

# 16. Deployment Checklist

Backend

✓ Build

✓ Deploy

✓ Health Check

---

Frontend

✓ Build

✓ API Connected

✓ Responsive

---

Database

✓ Migration

✓ Seed

✓ Constraint

✓ RLS

---

Storage

✓ Upload

✓ Read

✓ OCR

---

Automation

✓ Email Sync

✓ OCR

✓ Draft

---

Security

✓ HTTPS

✓ Secret Loaded

✓ JWT

---

# 17. Rollback Procedure

Jika deployment gagal.

1. Hentikan deployment.
2. Kembalikan versi sebelumnya.
3. Jalankan Health Check.
4. Verifikasi API.
5. Verifikasi Database.
6. Verifikasi Mobile.

Tidak diperbolehkan melakukan rollback database tanpa backup.

---

# 18. Troubleshooting

## Backend tidak dapat dijalankan

Periksa:

- Environment Variable
- Database URL
- Docker Log

---

## Flutter gagal build

Periksa:

```bash
flutter doctor
```

---

## OCR gagal

Periksa:

- Storage Bucket
- OCR Worker
- API Key

---

## Email Sync gagal

Periksa:

- OAuth
- IMAP
- Parser Log

---

## Database gagal

Periksa:

- Migration
- Connection String
- Supabase Status

---

# 19. Production Release Flow

```
Feature Branch

↓

Develop

↓

CI Pipeline

↓

Deploy Staging

↓

UAT

↓

Merge Main

↓

Deploy Production

↓

Health Check

↓

Release
```

---

# 20. Maintenance

Lakukan pemeriksaan rutin.

Harian

- Health Check
- Error Log

Mingguan

- Dependency Update
- Database Backup

Bulanan

- Security Review
- Performance Review
- Cleanup Audit Log

---

# 21. Disaster Recovery (Future)

Jika terjadi kegagalan total.

1. Restore Database Backup.
2. Deploy Backend.
3. Deploy Web.
4. Restore Storage.
5. Jalankan Migration.
6. Verifikasi API.
7. Verifikasi Sinkronisasi.

---

# 22. Summary

Deployment WorthFlow dilakukan menggunakan kombinasi GitHub Actions, Docker, Koyeb, Vercel, dan Supabase sehingga proses build, pengujian, dan rilis dapat berjalan secara otomatis serta konsisten.

Dokumen ini menjadi panduan operasional untuk menyiapkan lingkungan baru, melakukan deployment, memverifikasi hasil deployment, hingga melakukan rollback apabila terjadi kegagalan. Dengan mengikuti langkah-langkah pada dokumen ini, aplikasi dapat dirilis dengan risiko yang minimal dan siap digunakan oleh seluruh anggota keluarga.