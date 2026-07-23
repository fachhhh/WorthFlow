# Audit Log

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan mekanisme Audit Logging pada WorthFlow.

Audit Log digunakan untuk:

- Melacak seluruh aktivitas penting pengguna
- Mendukung proses investigasi insiden
- Menjaga integritas data finansial
- Memenuhi prinsip accountability
- Membantu debugging dan monitoring sistem

Dokumen ini melengkapi:

- 15-auth-flow.md
- 16-security-design.md
- 17-threat-model.md

---

# 2. Audit Logging Principles

WorthFlow menerapkan prinsip berikut.

## Immutable

Audit Log tidak boleh diubah maupun dihapus oleh pengguna.

---

## Traceability

Setiap perubahan harus dapat ditelusuri.

---

## Accountability

Setiap aktivitas memiliki identitas pelaku.

---

## Non-Repudiation

Pengguna tidak dapat menyangkal aktivitas yang telah dilakukan.

---

## Least Information

Audit hanya menyimpan informasi yang diperlukan.

Data sensitif seperti password dan token tidak pernah dicatat.

---

# 3. Audit Architecture

                User
                  │
                  ▼
            API Request
                  │
                  ▼
        Authentication
                  │
                  ▼
        Authorization
                  │
                  ▼
         Business Logic
                  │
          ┌───────┴────────┐
          ▼                ▼
    Database Change    Audit Event
          │                │
          └───────┬────────┘
                  ▼
            audit_logs
                  │
                  ▼
         Monitoring & Admin

---

# 4. Audit Scope

Aktivitas berikut wajib dicatat.

Authentication

- Login
- Logout
- Login Failed

---

Family

- Create Member
- Update Member
- Archive Member

---

Asset

- Create Asset
- Update Asset
- Archive Asset
- Asset Valuation

---

Transaction

- Create
- Update
- Delete (Soft Delete)
- Approve Draft
- Reject Draft

---

Automation

- OCR Upload
- OCR Completed
- Email Sync
- Draft Generated

---

System

- Sync Started
- Sync Completed
- Sync Failed

---

Security

- Access Denied
- Invalid Token
- Rate Limit Triggered

---

# 5. Audit Log Schema

Tabel

audit_logs

Field utama.

| Column | Description |
|----------|-------------|
| id | Primary Key |
| family_id | Family terkait |
| member_id | Pelaku aktivitas |
| entity_type | Jenis data |
| entity_id | ID data |
| action | Aktivitas |
| old_value | Data sebelum perubahan (JSONB) |
| new_value | Data setelah perubahan (JSONB) |
| ip_address | Alamat IP (future) |
| device_info | Informasi perangkat (future) |
| created_at | Waktu aktivitas |

---

# 6. Event Categories

WorthFlow mengelompokkan Audit Event menjadi beberapa kategori.

## Authentication

LOGIN

LOGOUT

LOGIN_FAILED

TOKEN_REFRESH

---

## Transaction

TRANSACTION_CREATED

TRANSACTION_UPDATED

TRANSACTION_ARCHIVED

---

## Asset

ASSET_CREATED

ASSET_UPDATED

ASSET_ARCHIVED

ASSET_VALUATION_UPDATED

---

## Draft

DRAFT_CREATED

DRAFT_APPROVED

DRAFT_REJECTED

---

## OCR

OCR_STARTED

OCR_COMPLETED

OCR_FAILED

---

## Email

EMAIL_SYNC_STARTED

EMAIL_SYNC_COMPLETED

EMAIL_SYNC_FAILED

EMAIL_PARSED

---

## Sync

SYNC_STARTED

SYNC_COMPLETED

SYNC_FAILED

CONFLICT_RESOLVED

---

## Security

ACCESS_DENIED

INVALID_TOKEN

PERMISSION_DENIED

RATE_LIMIT_TRIGGERED

---

# 7. Audit Flow

User Action

↓

Authentication

↓

Authorization

↓

Business Validation

↓

Database Transaction

↓

Audit Event

↓

audit_logs

↓

Monitoring

---

# 8. Before & After Snapshot

Update Transaction

Old Value

```json
{
  "amount": 50000,
  "category": "Food"
}
```

↓

New Value

```json
{
  "amount": 75000,
  "category": "Food"
}
```

Audit Log menyimpan kedua versi agar histori perubahan dapat ditelusuri.

---

# 9. Soft Delete Strategy

WorthFlow tidak menghapus data finansial secara permanen.

Ketika pengguna menghapus transaksi.

Transaction

↓

status = archived

↓

Audit Log

↓

Dashboard Update

---

# 10. Audit Retention

Audit Log disimpan selama:

MVP

- Tidak ada penghapusan otomatis.

Future

- Arsip tahunan.
- Retention Policy yang dapat dikonfigurasi.

---

# 11. Sensitive Data Policy

Audit Log **tidak boleh** menyimpan.

- Password
- JWT
- Refresh Token
- OTP
- API Secret
- Service Key

Untuk data sensitif seperti nomor rekening hanya disimpan sebagian.

Contoh

****1234

---

# 12. Monitoring Integration

Audit Log menjadi sumber data untuk:

- Admin Dashboard
- Security Monitoring
- Incident Investigation
- Analytics
- Error Tracking

---

# 13. Failed Activity Logging

Aktivitas yang gagal juga dicatat.

Contoh.

Login Failed

↓

Audit Event

↓

Security Monitoring

---

Access Denied

↓

Audit Event

↓

Alert

---

Sync Failed

↓

Audit Event

↓

Retry Queue

---

# 14. OCR Audit

Receipt Upload

↓

OCR Started

↓

OCR Completed

↓

Draft Created

↓

Draft Approved

↓

Transaction Created

Setiap tahapan menghasilkan Audit Event tersendiri.

---

# 15. Email Audit

Email Sync Started

↓

Email Downloaded

↓

Email Parsed

↓

Draft Generated

↓

Draft Approved

↓

Transaction Created

---

# 16. Offline Sync Audit

Offline Transaction

↓

SQLite

↓

Sync Queue

↓

Upload

↓

Supabase

↓

Audit Log

↓

Completed

---

# 17. Admin Audit View

Owner Family dapat melihat.

- Aktivitas transaksi
- Aktivitas aset
- OCR
- Email Sync
- Login
- Sync

Filter.

- Member
- Tanggal
- Jenis Aktivitas
- Entity

---

# 18. Example Audit Record

```json
{
  "entity_type": "transaction",
  "entity_id": "tx_001",
  "action": "TRANSACTION_UPDATED",
  "member_id": "member_01",
  "old_value": {
    "amount": 50000
  },
  "new_value": {
    "amount": 75000
  },
  "created_at": "2026-08-14T10:30:00Z"
}
```

---

# 19. Audit Checklist

Setiap Audit Event minimal memiliki.

✓ Timestamp

✓ Family ID

✓ Member ID

✓ Entity

✓ Entity ID

✓ Action

✓ Before Value (jika ada)

✓ After Value (jika ada)

---

# 20. Future Enhancement

Versi berikutnya dapat menambahkan.

- Device Fingerprint
- IP Address
- Geolocation
- Browser Information
- Risk Score
- Anomaly Detection
- SIEM Integration
- Export Audit Report (CSV / PDF)

---

# 21. Summary

WorthFlow menerapkan Audit Logging sebagai mekanisme pencatatan aktivitas yang bersifat **immutable**, **traceable**, dan **audit-ready**.

Setiap perubahan penting—baik yang dilakukan pengguna maupun proses otomatis seperti OCR, Email Sync, dan Offline Synchronization—menghasilkan Audit Event yang tersimpan pada tabel `audit_logs`.

Dengan pendekatan ini, sistem mampu menyediakan histori perubahan yang lengkap, mendukung investigasi insiden, meningkatkan keamanan, serta memastikan seluruh aktivitas finansial dapat dipertanggungjawabkan.