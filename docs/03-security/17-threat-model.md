# Threat Model

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan analisis ancaman (Threat Model) terhadap sistem WorthFlow.

Threat Model digunakan untuk:

- Mengidentifikasi potensi ancaman keamanan
- Menentukan prioritas mitigasi
- Membantu proses desain keamanan
- Mendukung pengembangan aplikasi yang aman sejak awal (Secure by Design)

Dokumen ini melengkapi:

- 15-auth-flow.md
- 16-security-design.md
- 18-audit-log.md

---

# 2. Threat Modeling Methodology

WorthFlow menggunakan pendekatan STRIDE.

STRIDE terdiri dari:

- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

---

# 3. System Scope

Komponen yang dianalisis.

- Mobile Application
- Web Dashboard
- FastAPI Backend
- Supabase Auth
- PostgreSQL Database
- Supabase Storage
- OCR Worker
- Email Parser
- Sync Engine
- Analytics Service

---

# 4. Assets to Protect

Prioritas tertinggi.

- Transaction
- Asset Balance
- Family Information
- Receipt Image
- OCR Result
- Email Transaction
- JWT
- Refresh Token
- API Secret

---

# 5. Trust Boundary

                 Internet
                     │
──────────────────────────────────
                     │
             FastAPI Backend
                     │
──────────────────────────────────
                     │
          PostgreSQL + Supabase
                     │
──────────────────────────────────
                     │
            Local Mobile Device

Seluruh perpindahan data antar boundary harus divalidasi.

---

# 6. STRIDE Analysis

## S — Spoofing Identity

Threat

Penyerang berpura-pura menjadi pengguna lain.

Contoh

- JWT dicuri
- Token bocor
- Session hijacking

Mitigation

- HTTPS
- JWT Expiration
- Refresh Token
- Secure Storage
- Supabase Auth

Risk

Medium

---

## T — Tampering

Threat

Mengubah data transaksi secara ilegal.

Contoh

- Mengubah nominal transaksi
- Mengubah asset balance
- Memodifikasi request API

Mitigation

- JWT Validation
- Family Validation
- Input Validation
- PostgreSQL Constraint
- Audit Log

Risk

High

---

## R — Repudiation

Threat

Pengguna menyangkal pernah melakukan perubahan.

Contoh

"Saya tidak pernah menghapus transaksi."

Mitigation

- Audit Log
- Timestamp
- Member ID
- Action History

Risk

Medium

---

## I — Information Disclosure

Threat

Kebocoran informasi sensitif.

Contoh

- Receipt
- Email Bank
- Saldo
- Asset
- JWT

Mitigation

- HTTPS
- Row Level Security
- Secure Storage
- Hidden Error Message

Risk

High

---

## D — Denial of Service

Threat

Server dibanjiri request.

Contoh

- Spam OCR
- Spam Login
- Spam Email Sync

Mitigation

- Rate Limit
- Queue
- Retry Policy

Risk

Medium

---

## E — Elevation of Privilege

Threat

User memperoleh hak akses lebih tinggi.

Contoh

Child menjadi Owner.

Mitigation

- Role Validation
- Backend Authorization
- RLS
- Family Isolation

Risk

High

---

# 7. Authentication Threat

Threat

Brute Force Login

Mitigation

- Rate Limit
- Password Policy
- Temporary Lock (Future)

---

Threat

Token Theft

Mitigation

- HTTPS
- Secure Storage
- Token Expiration

---

Threat

Refresh Token Abuse

Mitigation

- Rotation (Future)
- Session Expiration

---

# 8. API Threat

Threat

Broken Authentication

Mitigation

JWT Validation

---

Threat

Broken Authorization

Mitigation

Family Validation

---

Threat

Mass Assignment

Mitigation

DTO Validation

---

Threat

Injection

Mitigation

ORM

Parameterized Query

Validation

---

Threat

Replay Attack

Mitigation

Short JWT Lifetime

HTTPS

---

# 9. Database Threat

Threat

SQL Injection

Mitigation

SQLAlchemy ORM

Parameterized Query

---

Threat

Unauthorized Read

Mitigation

Row Level Security

---

Threat

Unauthorized Update

Mitigation

Family Validation

---

Threat

Data Corruption

Mitigation

Foreign Key

Transaction

Constraint

---

# 10. OCR Threat

Threat

Malicious Image

Mitigation

File Validation

MIME Validation

Size Validation

---

Threat

Incorrect OCR

Mitigation

User Review

Draft Approval

---

Threat

Prompt Injection (Future AI)

Mitigation

Prompt Isolation

Validation Layer

Confidence Threshold

---

# 11. Email Threat

Threat

Fake Email

Mitigation

Trusted Sender Validation

---

Threat

Duplicate Email

Mitigation

provider_message_id UNIQUE

---

Threat

Incorrect Parsing

Mitigation

Transaction Draft

User Review

---

# 12. Offline Sync Threat

Threat

Conflict Update

Mitigation

Sync Queue

Conflict Resolution

---

Threat

Offline Data Manipulation

Mitigation

Audit Log

Sync Validation

---

Threat

Replay Sync

Mitigation

Sync ID

Timestamp

---

# 13. Mobile Threat

Threat

Rooted Device

Mitigation

Warning (Future)

---

Threat

Device Lost

Mitigation

Logout

Token Expiration

Biometric Login (Future)

---

Threat

Screenshot Leakage

Mitigation

Sensitive Screen Protection (Future)

---

# 14. Infrastructure Threat

Threat

Secret Exposure

Mitigation

Environment Variable

Git Ignore

---

Threat

Dependency Vulnerability

Mitigation

Dependabot

GitHub Security

---

Threat

Storage Exposure

Mitigation

Private Bucket

Signed URL

---

# 15. Privacy Threat

Threat

Receipt berisi informasi pribadi.

Mitigation

Private Storage

---

Threat

Bank Account Number

Mitigation

Masking

Last 4 Digit

---

Threat

Email Content

Mitigation

Minimal Storage

---

# 16. Risk Matrix

| Threat | Impact | Likelihood | Priority |
|----------|--------|------------|----------|
| SQL Injection | High | Low | High |
| Token Theft | High | Medium | High |
| Unauthorized Access | High | Low | High |
| OCR Error | Medium | High | Medium |
| Email Parsing Error | Medium | Medium | Medium |
| DoS | Medium | Medium | Medium |
| Replay Attack | Medium | Low | Low |
| Device Loss | Medium | Medium | Medium |

---

# 17. Security Roadmap

MVP

- JWT
- HTTPS
- RLS
- Validation
- Audit Log

Version 2

- Biometric Login
- Device Management
- Session Dashboard
- Token Rotation

Version 3

- Passkey
- Hardware Security Key
- Fraud Detection
- AI Threat Detection

---

# 18. Residual Risk

Risiko yang masih dapat diterima pada MVP.

- OCR salah membaca struk
- Email parser gagal mengenali format baru
- Device hilang saat masih login
- Rooted device tidak terdeteksi

Risiko ini akan dikurangi pada versi berikutnya.

---

# 19. Summary

WorthFlow menggunakan pendekatan STRIDE untuk mengidentifikasi ancaman pada seluruh komponen sistem, mulai dari Mobile App, Backend, Database, OCR Pipeline, Email Parser, hingga Offline Sync.

Ancaman dengan prioritas tertinggi adalah:

- Unauthorized Access
- Data Tampering
- Information Disclosure
- Elevation of Privilege

Mitigasi dilakukan melalui kombinasi Authentication, Authorization, Row Level Security, Input Validation, Audit Logging, HTTPS, Secure Storage, dan prinsip Defense in Depth.

Threat Model ini menjadi acuan utama dalam proses pengembangan fitur baru agar setiap perubahan tetap memenuhi standar keamanan aplikasi finansial.