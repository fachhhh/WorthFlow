# Enhanced Entity Relationship Diagram (EERD)
Version: 2.0

# 1. Purpose

Dokumen ini mendefinisikan model data konseptual (Enhanced Entity Relationship Diagram / EERD) untuk WorthFlow.

Dokumen ini menjadi acuan utama dalam:

- Database Schema
- API Design
- Backend Development
- Migration Planning
- Data Validation
- Future Feature Expansion

Dokumen ini masih berada pada level konseptual (Conceptual Data Model) dan belum membahas implementasi PostgreSQL secara detail.

# 2. Design Principles

Model data WorthFlow dibangun berdasarkan prinsip berikut.

## 2.1 Family First

Seluruh data dimiliki oleh sebuah Family.

Bukan oleh User.

Artinya semua transaksi, aset, kategori, laporan, dan histori berada dalam konteks keluarga.

## 2.2 Transaction is the Source of Truth

Seluruh perpindahan nilai uang direpresentasikan oleh Transaction.

Tidak ada entity lain yang menyimpan histori perpindahan uang.

## 2.3 Asset Represents Value

Asset merepresentasikan seluruh bentuk kekayaan maupun kewajiban keluarga.

Contoh:

- Cash
- Bank Account
- E-Wallet
- Gold
- Stock
- Crypto
- Property
- Loan

## 2.4 Automation Never Writes Directly

Email maupun OCR tidak pernah membuat Transaction secara langsung.

Seluruh hasil otomatisasi harus melewati TransactionDraft.

## 2.5 Auditability

Seluruh perubahan penting harus dapat ditelusuri kembali.

# 3. Domain Overview

Model dibagi menjadi lima domain.

## Family Domain

- Family
- User
- FamilyMember

## Finance Domain

- Category
- Transaction

## Asset Domain

- Asset
- AssetValuation

## Automation Domain

- EmailAccount
- EmailMessage
- Receipt
- OCRJob
- OCRResult
- TransactionDraft

## Platform Domain

- SyncQueue
- AuditLog

# 4. Entity Catalog

Total Entity = 14

## Family

Root aggregate seluruh sistem.

Mewakili satu keluarga.

## User

Representasi akun login.

Menggunakan Supabase Auth.

## FamilyMember

Representasi anggota keluarga.

Member boleh memiliki akun maupun tidak.

Contoh:

- Ayah
- Ibu
- Anak SD

## Category

Kategori transaksi.

Dimiliki oleh Family.

## Transaction

Entity utama sistem.

Seluruh pemasukan, pengeluaran, transfer, maupun adjustment disimpan pada entity ini.

## Asset

Representasi kekayaan maupun kewajiban.

Asset dapat dimiliki oleh:

- Family
- FamilyMember

## AssetValuation

Riwayat perubahan nilai Asset.

Digunakan untuk:

- Gold
- Property
- Crypto
- Stock

## EmailAccount

Email yang terhubung ke sistem.

## EmailMessage

Email transaksi yang berhasil diambil.

## Receipt

File struk yang diupload.

## OCRJob

Proses OCR terhadap Receipt.

## OCRResult

Hasil ekstraksi OCR.

## TransactionDraft

Draft hasil otomatisasi.

Masih membutuhkan review pengguna.

## SyncQueue

Queue sinkronisasi Offline First.

## AuditLog

Riwayat perubahan data.

# 5. Relationship Matrix

Family
1 ---- N FamilyMember

Family
1 ---- N Category

Family
1 ---- N Asset

FamilyMember
1 ---- N Transaction

Category
1 ---- N Transaction

Asset
1 ---- N Transaction
(role = Source Asset)

Asset
1 ---- N Transaction
(role = Destination Asset)

Asset
1 ---- N AssetValuation

FamilyMember
1 ---- N EmailAccount

EmailAccount
1 ---- N EmailMessage

FamilyMember
1 ---- N Receipt

Receipt
1 ---- N OCRJob

OCRJob
1 ---- 1 OCRResult

EmailMessage
1 ---- 0..1 TransactionDraft

OCRResult
1 ---- 0..1 TransactionDraft

TransactionDraft
1 ---- 0..1 Transaction

FamilyMember
1 ---- N AuditLog

# 6. Cardinality

One Family

↓

Many Members

---

One Family

↓

Many Categories

---

One Family

↓

Many Assets

---

One Member

↓

Many Transactions

---

One Asset

↓

Many Transactions

(sebagai sumber)

---

One Asset

↓

Many Transactions

(sebagai tujuan)

---

One Receipt

↓

Many OCR Jobs

---

One OCR Job

↓

Exactly One OCR Result

---

One Draft

↓

Zero or One Transaction

# 7. Participation

Mandatory

FamilyMember → Family

Category → Family

Transaction → FamilyMember

Transaction → Category

Asset → Family

AssetValuation → Asset

EmailAccount → FamilyMember

EmailMessage → EmailAccount

Receipt → FamilyMember

OCRJob → Receipt

OCRResult → OCRJob

AuditLog → FamilyMember

Optional

User → FamilyMember

TransactionDraft → Transaction

EmailMessage → TransactionDraft

OCRResult → TransactionDraft

Asset → Owner Member

# 8. EER Specialization

Asset

ISA

- Cash
- Bank
- EWallet
- Gold
- Crypto
- Stock
- Property
- Loan

Constraint

Disjoint

Total

Artinya satu Asset hanya boleh menjadi satu subtype.

# 9. Business Rules

BR-01

Family minimal memiliki satu FamilyMember.

BR-02

FamilyMember boleh tidak memiliki User.

BR-03

Category hanya dimiliki satu Family.

BR-04

Transaction wajib memiliki Category.

BR-05

Transaction wajib memiliki FamilyMember sebagai creator.

BR-06

Income

Source Asset = NULL

Destination Asset ≠ NULL

BR-07

Expense

Source Asset ≠ NULL

Destination Asset = NULL

BR-08

Transfer

Source Asset ≠ NULL

Destination Asset ≠ NULL

BR-09

Adjustment

Source Asset = NULL

Destination Asset = NULL

BR-10

Receipt dapat diproses berkali-kali.

BR-11

Satu OCRJob hanya menghasilkan satu OCRResult.

BR-12

TransactionDraft hanya berasal dari SATU sumber.

Email

atau

OCR

BR-13

Transaction boleh berasal dari Draft maupun dibuat manual.

BR-14

Asset boleh dimiliki Family secara bersama.

BR-15

Owner Member pada Asset bersifat opsional.

# 10. Normalization

Model telah dirancang memenuhi:

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

Tidak terdapat:

- repeating group
- partial dependency
- transitive dependency

# 11. Mapping to Physical Database

Dokumen ini menjadi dasar implementasi pada:

12-schema-design.md

yang kemudian diterjemahkan menjadi:

- PostgreSQL
- Supabase Migration
- SQL Constraint
- Index
- Row Level Security

# 12. Future Extension

Model dirancang agar mudah dikembangkan.

Entity yang direncanakan:

- Budget
- Goal
- Investment
- Notification
- Device
- Session
- AI Insight
- Financial Report