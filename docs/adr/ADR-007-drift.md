# ADR-007: Use Drift (SQLite) as the Local Database

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow mengadopsi arsitektur **Offline-First**, sehingga seluruh data utama harus tetap dapat diakses dan dimodifikasi meskipun perangkat tidak memiliki koneksi internet.

Seluruh operasi seperti:

- Login Session
- Family Management
- Transactions
- Budgets
- Assets
- Categories
- OCR Draft
- Receipt Metadata
- Sync Queue
- User Preferences

harus dapat disimpan secara lokal sebelum disinkronkan ke server.

Selain itu, model data WorthFlow memiliki banyak relasi antar entitas sehingga membutuhkan database yang mendukung struktur relasional secara penuh.

---

# Decision

WorthFlow menggunakan **Drift** (SQLite ORM untuk Flutter) sebagai database lokal utama.

Drift menjadi penyimpanan utama pada perangkat untuk seluruh data aplikasi selama proses Offline-First berlangsung.

SQLite dipilih sebagai storage engine, sedangkan Drift menyediakan:

- ORM
- Type-safe Query
- Migration
- Reactive Query
- Code Generation

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Relational Data Model

WorthFlow memiliki relasi data yang kompleks.

Contoh.

```
Family

↓

Members

↓

Transactions

↓

Receipts

↓

Budgets

↓

Assets
```

Model seperti ini lebih cocok menggunakan database relasional dibanding key-value database.

---

## Offline-First Foundation

Seluruh CRUD dilakukan terlebih dahulu pada database lokal.

```
User Action

↓

Drift SQLite

↓

UI Updated

↓

Sync Queue

↓

FastAPI

↓

Supabase
```

Drift menjadi fondasi utama dari arsitektur Offline-First.

---

## SQLite Stability

SQLite merupakan database embedded yang telah digunakan secara luas pada perangkat mobile.

Keunggulannya meliputi:

- Stabil
- Cepat
- ACID Compliance
- Ringan
- Tidak memerlukan server
- Mendukung transaksi

---

## Type Safety

Drift menghasilkan kode Dart yang type-safe.

Keuntungan:

- Autocomplete
- Compile-time validation
- Mengurangi kesalahan query
- Integrasi baik dengan Flutter

---

## Migration Support

Skema database akan berkembang seiring bertambahnya fitur.

Drift menyediakan mekanisme migration sehingga perubahan skema dapat dilakukan tanpa kehilangan data pengguna.

---

## Reactive Queries

Perubahan data pada database dapat langsung memperbarui UI tanpa melakukan query manual berulang.

Hal ini sangat cocok dipadukan dengan Riverpod.

---

# Alternatives Considered

## Hive

### Pros

- Sangat cepat.
- Ringan.
- Mudah digunakan.
- Tidak memerlukan code generation.

### Cons

- Key-value database.
- Tidak mendukung foreign key.
- Tidak cocok untuk relasi kompleks.
- Sulit menangani query analitik.

Decision:

Not Selected.

---

## Isar

### Pros

- Sangat cepat.
- Modern.
- Reactive.
- Query cukup fleksibel.

### Cons

- Bukan database relasional.
- Tidak memiliki SQL.
- Tidak mendukung foreign key secara penuh.
- Kurang sesuai untuk model data WorthFlow.

Decision:

Not Selected.

---

## Sembast

### Pros

- Mudah digunakan.
- JSON-based.
- Ringan.

### Cons

- Tidak menggunakan SQL.
- Tidak mendukung relasi kompleks.
- Query lebih terbatas dibanding SQLite.

Decision:

Not Selected.

---

## sqflite

### Pros

- SQLite resmi untuk Flutter.
- Stabil.
- Fleksibel.

### Cons

- Menulis SQL secara manual.
- Tidak memiliki ORM bawaan.
- Boilerplate lebih banyak.
- Tidak reactive secara native.

Decision:

Not Selected.

---

# Consequences

## Positive

- Mendukung Offline-First secara penuh.
- Database relasional.
- SQL lengkap.
- Foreign Key.
- Migration.
- Reactive Query.
- Type-safe.
- Integrasi sangat baik dengan Flutter.
- Mudah dipadukan dengan Riverpod.

---

## Negative

- Code generation menambah waktu build.
- Perlu memahami konsep migration.
- Sedikit lebih kompleks dibanding Hive.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 07-offline-first-design.md | Local Storage |
| 08-sync-engine.md | Sync Queue |
| 10-ocr-pipeline.md | Draft Storage |
| 11-erd.md | Local Entity |
| 12-schema-design.md | SQLite Schema |
| 13-data-flow.md | Offline Flow |
| 25-test-strategy.md | Database Testing |
| 28-performance-testing.md | Local Performance |
| 32-dependency-management.md | Flutter Dependencies |

---

# Risks

Risiko utama.

- Korupsi database lokal.
- Migration gagal.
- Sinkronisasi tidak konsisten.
- Database bertambah besar.

Mitigasi.

- Backup lokal berkala.
- Migration testing.
- Retry Sync.
- VACUUM database secara berkala.
- Indexing pada kolom yang sering digunakan.

---

# Implementation Notes

Struktur penyimpanan data.

```
Flutter UI

↓

Riverpod

↓

Repository

↓

Drift SQLite

├── Users
├── Families
├── Members
├── Transactions
├── Receipts
├── Budgets
├── Assets
├── Sync Queue
└── Audit Log

↓

Sync Engine

↓

FastAPI

↓

Supabase PostgreSQL
```

Semua operasi CRUD dilakukan terhadap Drift terlebih dahulu.

Sinkronisasi dilakukan di background melalui Sync Engine.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Drift tidak lagi aktif dikembangkan.
- SQLite tidak lagi memenuhi kebutuhan aplikasi.
- Dibutuhkan database lokal dengan kemampuan yang jauh lebih tinggi.
- Arsitektur Offline-First berubah secara signifikan.

Review dilakukan setiap major release.

---

# References

Internal Documentation

- 07-offline-first-design.md
- 08-sync-engine.md
- 11-erd.md
- 12-schema-design.md
- 13-data-flow.md
- 25-test-strategy.md
- 28-performance-testing.md
- 32-dependency-management.md
- 36-architecture-decision-records.md

External References

- https://drift.simonbinder.eu/
- https://sqlite.org/
- https://pub.dev/packages/drift

---

# Decision Summary

WorthFlow menggunakan **Drift (SQLite)** sebagai database lokal karena menyediakan kombinasi database relasional yang stabil, type-safe ORM, reactive queries, migration support, dan integrasi yang sangat baik dengan Flutter.

Dibandingkan Hive, Isar, Sembast, maupun penggunaan SQLite mentah melalui sqflite, Drift memberikan keseimbangan terbaik antara kemudahan pengembangan, integritas data, dan dukungan terhadap arsitektur Offline-First yang menjadi fondasi utama WorthFlow. Keputusan ini memastikan seluruh data aplikasi tetap tersedia secara lokal, konsisten, dan siap disinkronkan ke backend ketika koneksi internet tersedia.