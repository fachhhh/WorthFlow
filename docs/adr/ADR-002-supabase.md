# ADR-002: Use Supabase PostgreSQL as the Primary Database

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow membutuhkan database utama yang mampu mendukung fitur-fitur berikut:

- Family Management
- Multi-member Collaboration
- Transaction Management
- Budget Management
- Receipt Storage
- OCR Draft
- Email Transaction
- Offline Synchronization
- Analytics
- Audit Log

Database juga harus memenuhi kebutuhan berikut:

- Relational Database
- SQL Support
- ACID Transaction
- Strong Data Integrity
- Authentication Integration
- Storage untuk Receipt
- Mudah dikelola pada tahap MVP
- Dapat berkembang ketika jumlah pengguna meningkat

Karena WorthFlow merupakan aplikasi keuangan keluarga, konsistensi dan integritas data menjadi prioritas utama.

---

# Decision

WorthFlow menggunakan **Supabase PostgreSQL** sebagai database utama.

Supabase digunakan untuk menyediakan:

- PostgreSQL Database
- Object Storage
- Row Level Security (RLS)
- Authentication (opsional)
- Dashboard Management
- Backup & Monitoring

Backend FastAPI tetap menjadi satu-satunya komponen yang berinteraksi langsung dengan database.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Relational Database

WorthFlow memiliki banyak relasi data.

Contohnya.

```
Family

↓

Members

↓

Transactions

↓

Receipt

↓

Budget

↓

Analytics
```

Model seperti ini lebih cocok menggunakan database relasional dibanding NoSQL.

---

## PostgreSQL

PostgreSQL merupakan salah satu database open-source paling stabil.

Keunggulan:

- ACID Compliance
- Foreign Key
- Transaction
- Indexing
- JSON Support
- Window Function
- Full SQL

---

## Row Level Security

Data keuangan harus terisolasi antar Family.

Supabase menyediakan Row Level Security (RLS) yang memungkinkan setiap Family hanya dapat mengakses datanya sendiri.

Hal ini memberikan lapisan keamanan tambahan di tingkat database.

---

## Managed Infrastructure

Supabase mengelola:

- Database
- Backup
- Monitoring
- SSL
- Storage

Sehingga developer dapat fokus pada pengembangan fitur.

---

## Object Storage

Receipt, invoice, dan dokumen transaksi dapat disimpan menggunakan Supabase Storage.

Tidak diperlukan layanan storage tambahan pada MVP.

---

## Excellent Developer Experience

Supabase menyediakan:

- Dashboard
- SQL Editor
- Migration Support
- API Keys Management
- Authentication Service

Sehingga proses development menjadi lebih cepat.

---

# Alternatives Considered

## Firebase Firestore

### Pros

- Sangat populer.
- Integrasi mudah dengan Flutter.
- Realtime bawaan.
- Dokumentasi lengkap.

### Cons

- NoSQL.
- Query kompleks lebih sulit.
- Relasi antar data tidak natural.
- Vendor lock-in lebih tinggi.
- Kurang cocok untuk model data finansial yang kompleks.

Decision:

Not Selected.

---

## Railway PostgreSQL

### Pros

- PostgreSQL.
- Deployment sederhana.
- Mudah digunakan.

### Cons

- Fokus utama hanya database hosting.
- Tidak menyediakan Authentication.
- Tidak menyediakan Storage.
- Tidak memiliki Row Level Security bawaan.

Decision:

Not Selected.

---

## Neon PostgreSQL

### Pros

- PostgreSQL modern.
- Branching database.
- Autoscaling.

### Cons

- Tidak menyediakan Storage.
- Tidak menyediakan Authentication.
- Tidak menyediakan Dashboard selengkap Supabase.
- Membutuhkan layanan tambahan untuk file storage.

Decision:

Not Selected.

---

## Self-hosted PostgreSQL

### Pros

- Kontrol penuh.
- Fleksibel.
- Tidak bergantung vendor.

### Cons

- Maintenance lebih tinggi.
- Backup manual.
- Monitoring manual.
- Deployment lebih kompleks.
- Tidak sesuai untuk MVP.

Decision:

Not Selected.

---

# Consequences

## Positive

- Database relasional yang kuat.
- SQL penuh.
- Foreign Key dan Constraint.
- Object Storage bawaan.
- Dashboard administrasi.
- Row Level Security.
- Skalabel untuk pertumbuhan aplikasi.
- Integrasi baik dengan FastAPI melalui SQLAlchemy.

---

## Negative

- Tetap memiliki ketergantungan terhadap layanan Supabase.
- Beberapa fitur enterprise memerlukan paket berbayar.
- Realtime tidak menjadi fokus utama pada MVP.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Database Architecture |
| 11-erd.md | Entity Relationship |
| 12-schema-design.md | Database Schema |
| 13-data-flow.md | Data Flow |
| 14-api-spec.md | REST API |
| 16-security-design.md | Row Level Security |
| 19-environments.md | Environment Configuration |
| 21-deployment-guide.md | Database Deployment |
| 23-backup-recovery.md | Backup Strategy |

---

# Risks

Risiko utama.

- Ketergantungan pada managed service.
- Perubahan harga layanan.
- Downtime dari penyedia layanan.

Mitigasi.

- Menggunakan PostgreSQL standar sehingga mudah dipindahkan ke penyedia lain.
- Backup database secara berkala.
- Seluruh migration disimpan dalam repository menggunakan Alembic.

---

# Implementation Notes

Arsitektur database.

```
Flutter Mobile / Web

↓

FastAPI

↓

SQLAlchemy ORM

↓

Supabase PostgreSQL

↓

Supabase Storage
```

Semua akses database dilakukan melalui Repository Layer.

Frontend tidak pernah mengakses database secara langsung.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Kebutuhan skalabilitas berubah secara signifikan.
- Dibutuhkan fitur database yang tidak didukung Supabase.
- Terjadi perubahan biaya yang tidak sesuai dengan kebutuhan proyek.
- Arsitektur berpindah ke self-hosted PostgreSQL.

Review dilakukan minimal setiap major release.

---

# References

Internal Documentation

- 06-system-architecture.md
- 11-erd.md
- 12-schema-design.md
- 13-data-flow.md
- 16-security-design.md
- 23-backup-recovery.md
- 32-dependency-management.md
- 36-architecture-decision-records.md

External References

- https://supabase.com/docs
- https://www.postgresql.org/docs/
- https://www.sqlalchemy.org/

---

# Decision Summary

WorthFlow menggunakan **Supabase PostgreSQL** sebagai database utama karena menyediakan kombinasi database relasional yang kuat, Object Storage, Row Level Security, serta layanan terkelola yang mengurangi beban operasional pada tahap MVP.

Dibandingkan Firebase Firestore, Railway PostgreSQL, Neon PostgreSQL, maupun PostgreSQL self-hosted, Supabase memberikan keseimbangan terbaik antara kemudahan pengembangan, keamanan, skalabilitas, dan biaya operasional. Selain itu, karena Supabase menggunakan PostgreSQL standar, migrasi ke penyedia lain tetap memungkinkan apabila kebutuhan proyek berubah di masa depan.