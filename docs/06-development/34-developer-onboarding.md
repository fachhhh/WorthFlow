# Developer Onboarding

Version: 1.0

---

# 1. Purpose

Dokumen ini menjelaskan langkah-langkah yang diperlukan agar developer baru dapat menjalankan proyek WorthFlow secara lokal.

Tujuan utama:

- Mempercepat proses onboarding.
- Menstandarkan environment pengembangan.
- Mengurangi konfigurasi manual.
- Memastikan seluruh developer menggunakan setup yang konsisten.

Target waktu onboarding:

**≤ 30 menit**

---

# 2. Project Overview

WorthFlow terdiri dari beberapa komponen.

```
Flutter Mobile
        │
Flutter Web
        │
 REST API
        │
    FastAPI
        │
 PostgreSQL (Supabase)
        │
───────────────
OCR Worker
Email Parser
Analytics
```

---

# 3. Prerequisites

Pastikan software berikut telah terpasang.

| Software | Minimum Version |
|-----------|-----------------|
| Git | Latest |
| Flutter | Stable |
| Dart | Stable |
| Python | 3.13+ |
| Docker Desktop | Latest |
| VS Code / Android Studio | Latest |
| PostgreSQL Client (opsional) | Latest |

---

# 4. Recommended IDE Extensions

## VS Code

Install extension berikut.

Flutter

Dart

Python

Docker

GitLens

Error Lens

YAML

REST Client

Markdown All in One

SQLite Viewer

---

# 5. Clone Repository

```bash
git clone https://github.com/<username>/worthflow.git

cd worthflow
```

---

# 6. Repository Structure

```
worthflow/

apps/
    mobile/
    web/

services/
    backend/
    email-parser/
    ocr-worker/
    analytics/

database/

docs/

assets/

infrastructure/
```

---

# 7. Environment Variables

Salin file.

```
.env.example
```

menjadi.

```
.env
```

Isi seluruh variabel.

```
SUPABASE_URL=

SUPABASE_ANON_KEY=

SUPABASE_SERVICE_KEY=

JWT_SECRET=

GEMINI_API_KEY=
```

Jangan pernah melakukan commit file `.env`.

---

# 8. Backend Setup

Masuk ke folder backend.

```bash
cd services/backend
```

Buat virtual environment.

```bash
python -m venv .venv
```

Aktifkan environment.

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependency.

```bash
pip install -r requirements.txt
```

Jalankan server.

```bash
uvicorn app.main:app --reload
```

Backend tersedia di.

```
http://localhost:8000
```

---

# 9. Mobile Setup

Masuk ke folder.

```bash
cd apps/mobile
```

Install dependency.

```bash
flutter pub get
```

Jalankan aplikasi.

```bash
flutter run
```

---

# 10. Web Setup

Masuk ke folder.

```bash
cd apps/web
```

Install dependency.

```bash
flutter pub get
```

Jalankan.

```bash
flutter run -d chrome
```

---

# 11. Database Setup

WorthFlow menggunakan Supabase.

Langkah.

1. Buat project Supabase.
2. Salin URL dan API Key.
3. Isi file `.env`.
4. Jalankan migration.

Migration disimpan pada.

```
database/migrations/
```

---

# 12. OCR Worker

Masuk ke folder.

```bash
cd services/ocr-worker
```

Install dependency.

```bash
pip install -r requirements.txt
```

Jalankan worker.

```bash
python worker.py
```

---

# 13. Email Parser

Masuk ke folder.

```bash
cd services/email-parser
```

Install dependency.

```bash
pip install -r requirements.txt
```

Jalankan parser.

```bash
python worker.py
```

---

# 14. Running Tests

Backend.

```bash
pytest
```

Flutter.

```bash
flutter test
```

Integration Test.

```bash
flutter test integration_test
```

---

# 15. Static Analysis

Python.

```bash
ruff check

black --check

mypy .
```

Flutter.

```bash
dart analyze

dart format .
```

Semua lint harus lolos sebelum commit.

---

# 16. Docker (Optional)

Menjalankan seluruh service.

```bash
docker compose up
```

Menghentikan service.

```bash
docker compose down
```

---

# 17. CI/CD Pipeline

Setiap Push atau Pull Request akan menjalankan.

- Build
- Lint
- Unit Test
- API Test
- Security Scan

Status pipeline dapat dilihat pada GitHub Actions.

---

# 18. Branch Workflow

Gunakan branch.

```
feature/

bugfix/

hotfix/

docs/

refactor/
```

Contoh.

```
feature/offline-sync

feature/dashboard

bugfix/login
```

---

# 19. Commit Workflow

Gunakan Conventional Commits.

Contoh.

```
feat(transaction): add recurring transaction

fix(auth): refresh expired token

docs(api): update endpoint

test(sync): improve queue testing
```

---

# 20. Development Workflow

```
Pull Latest

↓

Create Branch

↓

Development

↓

Testing

↓

Commit

↓

Push

↓

Pull Request

↓

Review

↓

Merge
```

---

# 21. Common Commands

Backend.

```bash
uvicorn app.main:app --reload
```

Run Tests.

```bash
pytest
```

Flutter.

```bash
flutter run
```

Analyze.

```bash
dart analyze
```

Format.

```bash
dart format .
```

---

# 22. Troubleshooting

## Flutter tidak mendeteksi device

Jalankan.

```bash
flutter doctor
```

---

## Dependency gagal

Jalankan.

```bash
flutter clean

flutter pub get
```

---

## Virtual Environment rusak

Hapus.

```
.venv
```

Buat ulang.

```bash
python -m venv .venv
```

---

## Migration gagal

Periksa.

- Database URL
- Migration Version
- PostgreSQL Connection

---

# 23. Onboarding Checklist

Developer dianggap siap apabila.

- [ ] Repository berhasil di-clone
- [ ] Environment berhasil dikonfigurasi
- [ ] Backend berjalan
- [ ] Mobile berjalan
- [ ] Web berjalan
- [ ] Database terhubung
- [ ] OCR Worker berjalan
- [ ] Email Parser berjalan
- [ ] Seluruh test lulus
- [ ] Lint tidak memiliki error

---

# 24. References

Dokumen terkait.

- 20-cicd.md
- 21-deployment-guide.md
- 30-coding-standards.md
- 31-design-system.md
- 33-contributing.md

---

# 25. Future Improvements

Roadmap.

- One-command setup script
- Dev Container (VS Code)
- Docker Development Environment
- Local Supabase Emulator
- Automated Environment Validation
- Interactive Onboarding Guide

---

# 26. Summary

Dokumen ini menyediakan panduan lengkap bagi developer baru untuk menjalankan WorthFlow mulai dari persiapan environment, konfigurasi backend, frontend, database, worker, hingga proses testing dan workflow pengembangan.

Dengan mengikuti langkah-langkah ini, developer diharapkan dapat mulai berkontribusi dalam waktu kurang dari 30 menit dengan lingkungan kerja yang konsisten dan terdokumentasi.