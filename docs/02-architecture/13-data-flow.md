# Data Flow

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan bagaimana data bergerak di dalam sistem WorthFlow.

Data Flow menjadi acuan untuk:

- Backend Development
- Mobile Development
- Web Dashboard
- API Integration
- Offline Synchronization
- OCR Pipeline
- Email Pipeline
- Analytics Engine

Dokumen ini melengkapi:

- 11-erd.md
- 12-schema-design.md

---

# 2. Data Flow Principles

WorthFlow dibangun menggunakan beberapa prinsip utama.

## Single Source of Truth

Seluruh perubahan finansial hanya disimpan pada tabel:

Transaction

---

## Draft Before Commit

Seluruh proses otomatis (OCR maupun Email Parser) tidak langsung membuat Transaction.

Seluruh hasil otomatisasi harus melewati:

TransactionDraft

↓

Review User

↓

Transaction

---

## Offline First

Seluruh input pengguna pertama kali disimpan secara lokal.

Sinkronisasi dilakukan ketika perangkat kembali online.

---

## Event Driven Synchronization

Perubahan data tidak langsung dikirim ke server.

Seluruh perubahan dimasukkan ke:

Sync Queue

kemudian diproses oleh Sync Engine.

---

# 3. High Level Data Flow

                    User
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Manual Form      Email Sync       OCR Upload
      │               │                │
      │               ▼                ▼
      │         Email Parser      OCR Pipeline
      │               │                │
      │               ▼                ▼
      │         Transaction Draft      │
      └───────────────┼────────────────┘
                      ▼
                User Review
                      │
          ┌───────────┴───────────┐
          │                       │
      Reject                 Approve
          │                       │
          ▼                       ▼
      Draft Closed         Transaction
                                  │
                     ┌────────────┼────────────┐
                     ▼            ▼            ▼
                  Asset      Audit Log    Sync Queue
                     │
                     ▼
                Analytics

---

# 4. Manual Transaction Flow

## Description

Flow ketika pengguna memasukkan transaksi secara manual.

## Flow

User

↓

Open Transaction Form

↓

Input Data

↓

Validation

↓

Create Transaction

↓

Update Asset Balance

↓

Write Audit Log

↓

Insert Sync Queue

↓

Refresh Dashboard

---

Affected Tables

- transactions
- audit_logs
- sync_queue

---

# 5. Manual Asset Flow

User

↓

Create Asset

↓

Save Asset

↓

Insert Sync Queue

↓

Dashboard Refresh

Affected Tables

- assets
- sync_queue

---

# 6. Email Ingestion Flow

## Description

Mengambil transaksi dari email bank.

## Flow

Scheduler

↓

Email Provider

↓

Fetch Email

↓

Save EmailMessage

↓

AI Parser

↓

Generate TransactionDraft

↓

Wait User Review

↓

Approve

↓

Transaction

↓

Sync Queue

Affected Tables

- email_accounts
- email_messages
- transaction_drafts
- transactions

---

# 7. OCR Pipeline Flow

## Description

Mengubah foto struk menjadi transaksi.

## Flow

User Upload Receipt

↓

Receipt

↓

OCR Job

↓

OCR Result

↓

AI Extraction

↓

Transaction Draft

↓

User Review

↓

Transaction

↓

Dashboard Update

Affected Tables

- receipts
- ocr_jobs
- ocr_results
- transaction_drafts
- transactions

---

# 8. Offline Synchronization Flow

## Description

Flow ketika perangkat sedang offline.

## Flow

User Action

↓

SQLite Local Database

↓

Sync Queue

↓

Internet Available

↓

Sync Engine

↓

Supabase

↓

Receive Response

↓

Mark Completed

↓

Refresh Local Cache

---

# 9. Asset Movement Flow

WorthFlow menggunakan dua kolom:

- source_asset_id
- destination_asset_id

---

## Income

Salary

↓

Transaction

↓

destination_asset = BCA

↓

Asset Balance + Amount

---

## Expense

Shopee

↓

Transaction

↓

source_asset = Jago

↓

Asset Balance - Amount

---

## Transfer

BCA

↓

Transaction

↓

Jago

↓

Source Balance -

↓

Destination Balance +

---

## Adjustment

Admin Correction

↓

Transaction

↓

Manual Recalculation

---

# 10. Transaction Draft Lifecycle

Draft dibuat dari:

- Email
- OCR

Status

Pending Review

↓

Approved

↓

Transaction

atau

Rejected

↓

Archive

---

# 11. Sync Queue Lifecycle

Pending

↓

Syncing

↓

Completed

↓

Archived

atau

Failed

↓

Retry

↓

Completed

---

# 12. Audit Log Flow

Setiap perubahan penting menghasilkan Audit Log.

Transaction Created

↓

Audit Log

Transaction Updated

↓

Audit Log

Transaction Deleted (Soft Delete)

↓

Audit Log

Asset Updated

↓

Audit Log

---

# 13. Dashboard Aggregation Flow

Transaction

↓

Aggregation Service

↓

Income Summary

Expense Summary

Cash Flow

Asset Allocation

Monthly Report

↓

Dashboard API

↓

Mobile UI

---

# 14. Net Worth Calculation Flow

Assets

↓

Current Balance

+

Asset Valuation

↓

Net Asset

↓

Loan

↓

Net Worth

---

# 15. Analytics Flow

Transactions

↓

Grouping

↓

Category Analysis

↓

Merchant Analysis

↓

Monthly Trend

↓

Yearly Trend

↓

Visualization

---

# 16. Notification Flow (Future)

Transaction

↓

Rule Engine

↓

Notification

↓

Mobile Push

---

# 17. Error Handling Flow

OCR Failed

↓

Retry OCR

↓

Still Failed

↓

Manual Input

---

Email Parsing Failed

↓

Keep Email

↓

Manual Review

---

Sync Failed

↓

Retry Queue

↓

Success

---

# 18. Data Ownership Flow

Family

↓

Family Member

↓

Assets

↓

Transactions

↓

Reports

↓

Dashboard

Seluruh data selalu berada dalam konteks Family.

---

# 19. Security Checkpoints

Setiap flow wajib melewati validasi berikut.

- Authentication
- Authorization
- Family Access Validation
- Input Validation
- Audit Logging
- Offline Queue Validation
- Row Level Security

---

# 20. Summary

Seluruh lifecycle data WorthFlow mengikuti pola berikut.

Input

↓

Validation

↓

Draft (Automation Only)

↓

Transaction

↓

Asset Update

↓

Audit Log

↓

Sync Queue

↓

Supabase

↓

Analytics

↓

Dashboard

Dengan pendekatan ini, WorthFlow memiliki alur data yang konsisten, mudah diaudit, serta mendukung operasi offline-first tanpa mengorbankan integritas data.