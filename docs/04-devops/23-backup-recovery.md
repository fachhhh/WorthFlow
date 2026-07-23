# Backup & Recovery

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi Backup & Disaster Recovery pada WorthFlow.

Tujuan utama:

- Melindungi data finansial keluarga.
- Meminimalkan kehilangan data.
- Mempercepat proses pemulihan sistem.
- Menjamin keberlangsungan layanan.
- Mendukung operasional jangka panjang.

Dokumen ini melengkapi:

- 19-environments.md
- 21-deployment-guide.md
- 22-monitoring.md

---

# 2. Backup Strategy

WorthFlow menerapkan beberapa lapisan backup.

```
Mobile SQLite
        │
        ▼
Offline Queue
        │
        ▼
Supabase PostgreSQL
        │
        ▼
Automatic Backup
        │
        ▼
Recovery
```

Backup dilakukan pada beberapa komponen secara terpisah.

---

# 3. Backup Scope

Komponen yang wajib memiliki backup.

| Component | Backup |
|-----------|--------|
| PostgreSQL Database | ✅ |
| Supabase Storage | ✅ |
| Receipt Images | ✅ |
| Audit Logs | ✅ |
| Migration Files | ✅ |
| Git Repository | ✅ |

Komponen berikut tidak perlu dibackup.

- Cache
- Temporary OCR Result
- Session
- Access Token

---

# 4. Database Backup

Database utama menggunakan PostgreSQL (Supabase).

Backup meliputi:

- Families
- Members
- Assets
- Transactions
- Categories
- Budgets
- Receipts Metadata
- Audit Logs
- Sync Queue

---

# 5. Storage Backup

Receipt disimpan pada Supabase Storage.

Backup dilakukan terhadap:

- Receipt Image
- Attachment
- OCR Source Image

Storage menggunakan bucket private.

---

# 6. Backup Frequency

| Data | Frequency |
|------|-----------|
| Database | Daily |
| Storage | Daily |
| Audit Log | Daily |
| Source Code | Real-time (Git) |
| Migration | Real-time (Git) |

---

# 7. Backup Retention

Development

- Manual

Staging

- 7 hari

Production

- 30 hari

Future

- 90 hari
- 1 tahun arsip tahunan

---

# 8. Recovery Objective

Target Recovery.

Recovery Time Objective (RTO)

≤ 1 jam

Recovery Point Objective (RPO)

≤ 24 jam

Untuk MVP, target ini sudah memadai karena aplikasi digunakan dalam lingkup keluarga.

---

# 9. Recovery Workflow

```
Failure

↓

Identify

↓

Stop Service

↓

Restore Database

↓

Restore Storage

↓

Run Migration Check

↓

Health Check

↓

Resume Service
```

---

# 10. Database Recovery

Langkah pemulihan.

1. Restore database backup.
2. Jalankan migration verification.
3. Verifikasi Foreign Key.
4. Verifikasi Row Level Security.
5. Jalankan Health Check.

---

# 11. Storage Recovery

Langkah.

Restore Bucket

↓

Restore Receipt

↓

Restore Metadata

↓

OCR Ready

---

# 12. Mobile Recovery

Jika aplikasi dihapus.

User Login

↓

Sync

↓

Download Data

↓

Restore Local SQLite

↓

Offline Ready

Karena SQLite hanya cache lokal, data utama tetap berasal dari server.

---

# 13. Offline Queue Recovery

Jika proses sinkronisasi gagal.

SQLite Queue

↓

Retry

↓

Conflict Resolution

↓

Upload

↓

Completed

Tidak ada transaksi yang langsung dihapus sebelum sinkronisasi berhasil.

---

# 14. Disaster Scenario

## Database Failure

Recovery

- Restore Backup
- Health Check
- Reconnect API

---

## Storage Failure

Recovery

- Restore Bucket
- Re-upload Missing File

---

## Backend Failure

Recovery

- Redeploy Docker
- Load Environment
- Health Check

---

## Mobile Device Lost

Recovery

- Install App
- Login
- Synchronize Data

---

## OCR Worker Failure

Recovery

- Restart Worker
- Retry Queue

---

# 15. Backup Verification

Backup dianggap valid apabila.

✓ File dapat dibaca.

✓ Database dapat di-restore.

✓ Migration berhasil dijalankan.

✓ Health Check berhasil.

---

# 16. Backup Security

Backup harus:

- Encrypted
- Private
- Tidak dapat diakses publik

Secret tidak pernah masuk backup.

---

# 17. Recovery Checklist

Database

✓ Restore

✓ Constraint

✓ RLS

---

Storage

✓ Receipt

✓ Bucket

---

Backend

✓ API

✓ Docker

---

Mobile

✓ Sync

✓ SQLite

---

Monitoring

✓ Health Check

✓ Log

---

# 18. Testing Recovery

Recovery diuji secara berkala.

Development

- Manual

Staging

- Sebelum Release

Production

- Simulasi setiap 6 bulan (Future)

---

# 19. Future Improvements

Roadmap.

- Point-in-Time Recovery
- Multi Region Backup
- Automated Restore Testing
- Incremental Backup
- Cross Region Storage
- Disaster Recovery Dashboard

---

# 20. Summary

WorthFlow menerapkan strategi Backup & Recovery untuk melindungi data finansial keluarga dari kehilangan akibat kegagalan perangkat, server, maupun kesalahan operasional.

Database, storage, audit log, dan source code memiliki mekanisme backup masing-masing, sedangkan proses recovery dirancang agar sistem dapat kembali beroperasi dengan cepat dan aman.

Dengan strategi ini, risiko kehilangan data dapat diminimalkan dan aplikasi tetap dapat diandalkan sebagai pusat pencatatan keuangan keluarga.