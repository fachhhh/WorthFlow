# Coding Standards

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan standar penulisan kode (Coding Standards) untuk seluruh proyek WorthFlow.

Tujuan utama:

- Menjaga konsistensi kode.
- Mempermudah proses code review.
- Mengurangi technical debt.
- Mempermudah onboarding developer baru.
- Meningkatkan maintainability aplikasi.

Seluruh source code harus mengikuti standar pada dokumen ini.

---

# 2. General Principles

WorthFlow menerapkan prinsip berikut.

- Readability over Cleverness
- Simplicity over Complexity
- Explicit is Better than Implicit
- Small & Focused Functions
- Single Responsibility Principle
- Consistent Naming
- Self-documenting Code

Kode yang mudah dipahami lebih bernilai daripada kode yang terlalu kompleks.

---

# 3. Project Structure

Repository menggunakan struktur berikut.

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

Setiap folder memiliki satu tanggung jawab utama.

---

# 4. Naming Convention

## Folder

Gunakan:

```
snake_case
```

Contoh.

```
email_parser

ocr_worker

sync_engine
```

---

## File

Gunakan.

```
snake_case
```

Contoh.

```
transaction_service.py

budget_repository.py

receipt_controller.py
```

Flutter.

```
transaction_card.dart

dashboard_page.dart
```

---

## Class

Gunakan.

```
PascalCase
```

Contoh.

```python
TransactionService
```

```dart
BudgetCard
```

---

## Variable

Gunakan.

```
camelCase (Dart)

snake_case (Python)
```

Contoh.

```dart
monthlyExpense
```

```python
monthly_expense
```

---

## Constant

Python.

```
MAX_UPLOAD_SIZE
```

Flutter.

```
const maxUploadSize
```

---

## Enum

Gunakan.

```
PascalCase
```

Contoh.

```dart
TransactionType
```

---

# 5. Python Standards

Mengikuti:

PEP 8

Target Python.

```
Python 3.13+
```

Gunakan.

- Black
- Ruff
- isort
- mypy

Urutan import.

```
Standard Library

↓

Third Party

↓

Local Module
```

Contoh.

```python
import datetime

from fastapi import APIRouter

from app.services.transaction import TransactionService
```

---

# 6. FastAPI Standards

Gunakan struktur.

```
routers/

services/

repositories/

models/

schemas/

core/
```

Controller hanya bertugas.

- menerima request
- validasi
- memanggil service

Business Logic diletakkan pada Service.

Repository hanya mengakses Database.

---

# 7. Flutter Standards

Mengikuti rekomendasi Effective Dart.

Gunakan.

```
feature-first architecture
```

Contoh.

```
features/

authentication/

dashboard/

transaction/

budget/

asset/
```

Setiap feature memiliki.

```
data/

domain/

presentation/
```

---

# 8. State Management

WorthFlow menggunakan.

Riverpod

Aturan.

Provider tidak boleh langsung mengakses Database.

Seluruh akses data melalui Repository.

---

# 9. Database Standards

Nama tabel.

```
plural_snake_case
```

Contoh.

```
transactions

assets

budgets
```

Kolom.

```
snake_case
```

Primary Key.

```
id
```

Foreign Key.

```
family_id

member_id

transaction_id
```

Timestamp.

```
created_at

updated_at

deleted_at
```

---

# 10. API Standards

RESTful API.

Gunakan.

```
GET

POST

PATCH

DELETE
```

Endpoint.

```
/transactions

/assets

/budgets

/receipts
```

Response.

```json
{
  "success": true,
  "data": {},
  "message": "Success"
}
```

---

# 11. Error Handling

Jangan menggunakan.

```
except:
```

Gunakan.

```python
except ValidationError:
```

atau.

```python
except HTTPException:
```

Semua error memiliki log.

---

# 12. Logging Standards

Gunakan.

```
logging
```

Jangan gunakan.

```
print()
```

Level.

DEBUG

INFO

WARNING

ERROR

CRITICAL

Log tidak boleh berisi.

- Password
- JWT
- Secret
- API Key

---

# 13. Commenting

Komentar digunakan apabila.

- Algoritma kompleks.
- Rumus bisnis.
- Workaround.

Jangan menjelaskan sesuatu yang sudah jelas.

Contoh buruk.

```python
# increment i

i += 1
```

---

# 14. Documentation

Seluruh Public Function memiliki docstring.

Contoh.

```python
def create_transaction():
    """
    Create a new transaction.

    Returns
    -------
    Transaction
    """
```

---

# 15. Formatting

Python.

- Black

Flutter.

- dart format

Seluruh commit wajib dalam kondisi format bersih.

---

# 16. Git Convention

Branch.

```
feature/

bugfix/

hotfix/

release/
```

Contoh.

```
feature/offline-sync

feature/email-parser

bugfix/login

hotfix/token-expired
```

---

# 17. Commit Convention

Menggunakan Conventional Commits.

Contoh.

```
feat:

fix:

refactor:

test:

docs:

style:

perf:

chore:
```

Contoh.

```
feat(transaction): add recurring expense

fix(auth): refresh token bug

docs(api): update auth flow

test(ocr): add receipt parser tests
```

---

# 18. Pull Request Standards

Setiap Pull Request harus.

✓ Lulus CI

✓ Tidak ada konflik

✓ Lulus seluruh test

✓ Memiliki deskripsi

✓ Menghubungkan Issue (jika ada)

---

# 19. Code Review Checklist

Reviewer memeriksa.

- Readability
- Naming
- Architecture
- Test
- Security
- Performance
- Documentation

---

# 20. Dependency Standards

Gunakan library yang.

- Aktif dikembangkan.
- Memiliki dokumentasi baik.
- Banyak digunakan komunitas.
- Mendukung LTS.
- Memiliki lisensi yang kompatibel (Apache 2.0, MIT, BSD).

Hindari dependency yang tidak lagi dipelihara.

---

# 21. Static Analysis

Sebelum commit.

Python.

- Ruff
- Black
- mypy

Flutter.

- dart analyze
- dart format

Pipeline CI akan gagal jika terdapat lint error.

---

# 22. Security Guidelines

Jangan pernah.

- Hardcode Secret
- Hardcode Password
- Commit `.env`
- Commit API Key
- Menyimpan JWT dalam log

Gunakan Environment Variable untuk seluruh konfigurasi sensitif.

---

# 23. Code Quality Metrics

Target minimum.

| Metric | Target |
|---------|--------|
| Test Coverage | ≥80% |
| Cyclomatic Complexity | ≤10 |
| Function Length | ≤50 baris |
| File Length | ≤500 baris (disarankan) |
| Public Function Documentation | 100% |

Kode yang melebihi batas perlu dipertimbangkan untuk dipecah menjadi modul yang lebih kecil.

---

# 24. Future Improvements

Roadmap.

- SonarQube Integration
- Pre-commit Hooks
- AI-assisted Code Review
- Architecture Linting
- Dependency Health Dashboard
- Automatic Refactoring Suggestions

---

# 25. Summary

Dokumen ini menetapkan standar penulisan kode pada WorthFlow mulai dari struktur proyek, konvensi penamaan, gaya penulisan Python dan Flutter, standar API, database, Git, hingga proses code review.

Dengan mengikuti aturan ini, seluruh kode di dalam repository diharapkan tetap konsisten, mudah dipahami, mudah dipelihara, dan siap dikembangkan oleh lebih dari satu developer tanpa mengorbankan kualitas maupun keamanan.