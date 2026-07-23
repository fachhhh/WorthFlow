# ADR-003: Adopt Offline-First Architecture

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow dirancang sebagai aplikasi manajemen keuangan keluarga yang harus tetap dapat digunakan kapan saja, termasuk ketika koneksi internet tidak tersedia atau tidak stabil.

Target pengguna meliputi:

- Keluarga dengan koneksi internet terbatas.
- Pengguna yang sering berpindah jaringan.
- Pengguna yang ingin mencatat transaksi secara instan tanpa menunggu sinkronisasi.

Aktivitas utama seperti:

- Mencatat transaksi
- Mengambil foto struk
- Mengedit budget
- Melihat histori transaksi
- Mengelola aset

harus tetap dapat dilakukan tanpa bergantung pada koneksi internet.

Apabila aplikasi hanya menggunakan pendekatan Online-Only, pengalaman pengguna akan terganggu setiap kali koneksi internet tidak tersedia.

---

# Decision

WorthFlow mengadopsi **Offline-First Architecture**.

Seluruh operasi utama akan dilakukan terlebih dahulu pada database lokal.

Sinkronisasi dengan server dilakukan secara asynchronous ketika koneksi tersedia.

Prinsip utama:

```
User Action

↓

Local Database

↓

Immediate UI Update

↓

Sync Queue

↓

Background Synchronization

↓

Server
```

Database lokal menjadi sumber data utama untuk aplikasi.

Server bertindak sebagai sumber kebenaran global (Global Source of Truth).

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan.

## Better User Experience

Pengguna tidak perlu menunggu jaringan.

Setiap aksi terasa instan.

Contoh.

```
Tambah Transaksi

↓

Tersimpan Lokal (<50 ms)

↓

UI langsung berubah

↓

Sinkronisasi di belakang layar
```

---

## Reliability

Aplikasi tetap dapat digunakan ketika:

- Tidak ada internet.
- Jaringan lambat.
- Server sedang maintenance.
- Pengguna berada di mode pesawat.

---

## Family Usage

WorthFlow digunakan oleh beberapa anggota keluarga.

Masing-masing anggota dapat tetap mencatat transaksi walaupun sedang offline.

Sinkronisasi dilakukan ketika perangkat kembali online.

---

## Data Safety

Transaksi tidak hilang hanya karena koneksi internet gagal.

Data tetap berada pada database lokal.

---

## Performance

Sebagian besar operasi dilakukan pada SQLite lokal.

Membaca ribuan transaksi menjadi jauh lebih cepat dibanding selalu melakukan request ke server.

---

# Alternatives Considered

## Online-Only

### Pros

- Arsitektur lebih sederhana.
- Tidak memerlukan Sync Engine.
- Tidak ada konflik data.

### Cons

- Tidak dapat digunakan tanpa internet.
- UX buruk pada jaringan lambat.
- Setiap aksi bergantung pada server.
- Tidak sesuai dengan visi WorthFlow.

Decision:

Not Selected.

---

## Cache-First

### Pros

- Implementasi relatif sederhana.
- Data dapat disimpan sementara.

### Cons

- Cache bukan database.
- Tidak cocok untuk operasi CRUD kompleks.
- Sulit menangani perubahan data lokal.

Decision:

Not Selected.

---

## Offline-First

### Pros

- UX sangat baik.
- Cepat.
- Tetap bekerja tanpa internet.
- Sinkronisasi fleksibel.
- Lebih tahan terhadap gangguan jaringan.

### Cons

- Sinkronisasi lebih kompleks.
- Membutuhkan Conflict Resolution.
- Membutuhkan Local Database.

Decision:

Selected.

---

# Consequences

## Positive

- Aplikasi tetap dapat digunakan tanpa internet.
- Respons antarmuka lebih cepat.
- Mengurangi ketergantungan terhadap jaringan.
- Pengalaman pengguna lebih konsisten.
- Sangat cocok untuk penggunaan sehari-hari.

---

## Negative

- Membutuhkan Sync Engine.
- Membutuhkan Queue Management.
- Membutuhkan Conflict Resolution.
- Arsitektur menjadi lebih kompleks.
- Pengujian sinkronisasi lebih sulit.

---

# Impact

Keputusan ini memengaruhi hampir seluruh arsitektur WorthFlow.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Offline Architecture |
| 07-offline-first-design.md | Core Design |
| 08-sync-engine.md | Synchronization |
| 10-ocr-pipeline.md | Local Draft Storage |
| 11-erd.md | Sync Queue Entity |
| 12-schema-design.md | Local Database |
| 13-data-flow.md | Offline Data Flow |
| 27-api-testing.md | Sync Testing |
| 28-performance-testing.md | Local Performance |

---

# Risks

Risiko utama.

- Konflik data.
- Sinkronisasi gagal.
- Queue menumpuk.
- Perubahan urutan sinkronisasi.
- Data lokal korup.

Mitigasi.

- Sync Queue.
- Retry Mechanism.
- Version Number.
- Timestamp.
- Conflict Resolution.
- Local Backup.

---

# Implementation Notes

Arsitektur sinkronisasi.

```
Flutter

↓

Repository

↓

Drift SQLite

↓

Sync Queue

↓

Sync Engine

↓

REST API

↓

FastAPI

↓

PostgreSQL
```

Semua operasi CRUD akan mengikuti urutan berikut.

```
Create

↓

Save Local

↓

Insert Queue

↓

Update UI

↓

Background Sync

↓

Success

↓

Remove Queue
```

Jika sinkronisasi gagal.

```
Retry

↓

Exponential Backoff

↓

User Notification (jika diperlukan)
```

---

# Conflict Resolution Strategy

Strategi MVP menggunakan:

**Last Write Wins (LWW)**

Urutan.

```
Local Change

↓

Timestamp

↓

Server Compare

↓

Latest Version Wins
```

Pada versi berikutnya strategi dapat dikembangkan menjadi:

- Manual Merge
- Operational Transformation
- CRDT
- Field-level Merge

---

# Review Criteria

ADR ini harus ditinjau ulang apabila:

- Arsitektur sinkronisasi berubah secara signifikan.
- Dibutuhkan real-time collaboration.
- Konflik data menjadi terlalu kompleks.
- Offline database diganti.

Review dilakukan setiap major release.

---

# References

Internal Documentation

- 06-system-architecture.md
- 07-offline-first-design.md
- 08-sync-engine.md
- 11-erd.md
- 12-schema-design.md
- 13-data-flow.md
- 28-performance-testing.md
- 36-architecture-decision-records.md

External References

- Martin Kleppmann — *Designing Data-Intensive Applications*
- SQLite Documentation
- Flutter Offline-First Architecture Guidelines
- PostgreSQL Documentation

---

# Decision Summary

WorthFlow mengadopsi **Offline-First Architecture** sebagai prinsip utama pengembangan aplikasi. Seluruh operasi dilakukan terlebih dahulu pada database lokal menggunakan Drift (SQLite), kemudian disinkronkan ke server secara asynchronous melalui Sync Engine.

Pendekatan ini memberikan pengalaman pengguna yang lebih cepat, andal, dan tetap berfungsi tanpa koneksi internet. Meskipun meningkatkan kompleksitas arsitektur melalui kebutuhan akan sinkronisasi, antrean perubahan, dan penyelesaian konflik data, manfaatnya jauh lebih besar bagi aplikasi keuangan keluarga yang harus selalu tersedia kapan pun dan di mana pun.