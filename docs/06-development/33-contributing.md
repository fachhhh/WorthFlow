# Contributing Guide

Version: 1.0

---

# 1. Purpose

Dokumen ini menjelaskan proses kontribusi pada proyek WorthFlow.

Tujuan utama:

- Menjaga kualitas kode.
- Menstandarkan workflow pengembangan.
- Mempermudah onboarding developer baru.
- Mengurangi konflik saat pengembangan.
- Memastikan setiap perubahan terdokumentasi.

Seluruh kontributor diharapkan mengikuti panduan ini.

---

# 2. Development Workflow

Alur kontribusi.

```
Issue
    │
    ▼
Discussion
    │
    ▼
Create Branch
    │
    ▼
Development
    │
    ▼
Local Testing
    │
    ▼
Commit
    │
    ▼
Push
    │
    ▼
Pull Request
    │
    ▼
Code Review
    │
    ▼
Merge
```

---

# 3. Prerequisites

Pastikan telah menginstal:

- Git
- Flutter SDK
- Python 3.13+
- Docker Desktop
- PostgreSQL Client (opsional)
- VS Code / Android Studio

---

# 4. Clone Repository

```bash
git clone https://github.com/<username>/worthflow.git

cd worthflow
```

---

# 5. Setup Development Environment

## Backend

```bash
cd services/backend

python -m venv .venv

source .venv/bin/activate
```

Install dependency.

```bash
pip install -r requirements.txt
```

---

## Mobile

```bash
cd apps/mobile

flutter pub get
```

---

## Web

```bash
cd apps/web

flutter pub get
```

---

# 6. Environment Variables

Salin file.

```
.env.example
```

menjadi.

```
.env
```

Isi seluruh variabel sesuai kebutuhan.

Contoh.

```
SUPABASE_URL=

SUPABASE_KEY=

JWT_SECRET=

GEMINI_API_KEY=
```

Jangan pernah melakukan commit file `.env`.

---

# 7. Branch Strategy

Gunakan branch berdasarkan jenis pekerjaan.

```
feature/

bugfix/

hotfix/

release/

docs/

refactor/
```

Contoh.

```
feature/offline-sync

feature/dashboard

bugfix/login

docs/api-spec
```

---

# 8. Commit Convention

WorthFlow menggunakan Conventional Commits.

Format.

```
type(scope): message
```

Contoh.

```
feat(transaction): add recurring transaction

fix(auth): refresh token validation

docs(api): update endpoint specification

refactor(sync): simplify queue processing

test(ocr): add parser unit tests
```

---

# 9. Pull Request Checklist

Sebelum membuat Pull Request.

Pastikan.

- [ ] Branch sudah diperbarui dari `main`
- [ ] Tidak ada konflik merge
- [ ] Seluruh test lulus
- [ ] Lint tidak memiliki error
- [ ] Dokumentasi diperbarui bila diperlukan
- [ ] Screenshot ditambahkan jika ada perubahan UI

---

# 10. Code Review Guidelines

Reviewer akan memeriksa.

- Arsitektur
- Readability
- Naming Convention
- Error Handling
- Security
- Performance
- Test Coverage
- Dokumentasi

Reviewer berhak meminta perubahan sebelum proses merge.

---

# 11. Coding Standards

Seluruh kode wajib mengikuti dokumen.

```
30-coding-standards.md
```

Hal ini mencakup.

- Struktur folder
- Penamaan
- Formatting
- Logging
- Error handling
- Dokumentasi

---

# 12. Testing Requirements

Minimal pengujian sebelum Pull Request.

Backend.

```bash
pytest
```

Flutter.

```bash
flutter test
```

Static Analysis.

Python.

```bash
ruff check

black --check
```

Flutter.

```bash
dart analyze
```

---

# 13. CI/CD Requirements

Pull Request hanya dapat di-merge apabila.

- Build berhasil
- Unit Test berhasil
- API Test berhasil
- Static Analysis berhasil
- Security Scan berhasil

---

# 14. Documentation

Perubahan berikut wajib memperbarui dokumentasi.

- API baru
- Database
- Feature baru
- Security
- Deployment
- Design System

Dokumentasi merupakan bagian dari Definition of Done.

---

# 15. Issue Management

Gunakan label berikut.

```
feature

bug

documentation

enhancement

security

performance

refactor

question
```

Prioritas.

```
Critical

High

Medium

Low
```

---

# 16. Feature Development Process

Setiap fitur mengikuti tahapan berikut.

```
Idea

↓

Discussion

↓

Design

↓

Implementation

↓

Testing

↓

Review

↓

Merge

↓

Release
```

---

# 17. Merge Strategy

Gunakan.

```
Squash and Merge
```

Alasan.

- Riwayat commit lebih bersih.
- Mudah melakukan rollback.
- Commit history lebih mudah dibaca.

Branch fitur dapat dihapus setelah merge.

---

# 18. Release Workflow

```
Development

↓

Testing

↓

Staging

↓

Production

↓

Monitoring
```

Release mengikuti proses pada:

```
24-release-process.md
```

---

# 19. Communication

Diskusi perubahan besar dilakukan melalui.

- GitHub Issues
- GitHub Discussions (jika diaktifkan)

Keputusan arsitektur dicatat pada folder.

```
docs/adr/
```

---

# 20. Definition of Done

Sebuah task dianggap selesai apabila.

✓ Implementasi selesai.

✓ Lulus seluruh test.

✓ Tidak ada lint error.

✓ Dokumentasi diperbarui.

✓ Code review disetujui.

✓ Berhasil di-merge ke `main`.

---

# 21. Code of Conduct

Seluruh kontributor diharapkan.

- Menghormati pendapat orang lain.
- Memberikan review yang konstruktif.
- Berdiskusi berdasarkan data dan kebutuhan produk.
- Menjaga komunikasi yang profesional.

---

# 22. Future Improvements

Roadmap.

- Contributor License Agreement (CLA)
- Automated PR Template
- Issue Template
- Release Template
- GitHub Project Automation
- Pair Programming Guide

---

# 23. Summary

Dokumen ini mendefinisikan proses kontribusi pada WorthFlow mulai dari setup lingkungan pengembangan, strategi branching, standar commit, proses code review, pengujian, hingga release.

Dengan mengikuti panduan ini, setiap perubahan dapat dilakukan secara konsisten, terdokumentasi, dan tetap menjaga kualitas perangkat lunak seiring bertambahnya fitur maupun anggota tim.