# Schema Design

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan rancangan skema database fisik (Logical Database Design) untuk WorthFlow.

Schema ini diturunkan langsung dari dokumen:

- 11-erd.md

Dokumen ini akan menjadi acuan utama dalam:

- PostgreSQL Schema
- Supabase Migration
- SQL Constraint
- Backend Repository
- API Validation
- Query Optimization

---

# 2. Database Overview

Database Engine

- PostgreSQL 17
- Supabase

Design Goals

- Third Normal Form (3NF)
- UUID Primary Key
- Offline-first compatible
- Family-scoped support
- Audit friendly
- Easily extensible

---

# 3. Naming Convention

## Table

Semua tabel menggunakan:

- snake_case
- plural noun

Contoh

families

family_members

transactions

email_messages

---

## Column

Semua kolom menggunakan:

snake_case

Contoh

created_at

updated_at

transaction_date

source_asset_id

---

## Primary Key

Seluruh tabel menggunakan

id UUID PRIMARY KEY

---

## Foreign Key

Menggunakan format

<entity>_id

Contoh

family_id

member_id

category_id

source_asset_id

destination_asset_id

---

## Timestamp

Semua tabel memiliki

created_at

updated_at

kecuali tabel histori tertentu.

---

# 4. Common Columns

Sebagian besar tabel memiliki struktur berikut.

| Column | Type | Required |
|----------|------|----------|
| id | UUID | Yes |
| created_at | TIMESTAMP WITH TIME ZONE | Yes |
| updated_at | TIMESTAMP WITH TIME ZONE | Yes |

---

# 5. Enum Definitions

## TransactionType

income

expense

transfer

adjustment

---

## TransactionSource

manual

email

ocr

---

## DraftStatus

pending_review

approved

rejected

---

## SyncStatus

pending

syncing

completed

failed

---

## AssetType

cash

bank

ewallet

gold

crypto

stock

property

loan

---

## OCRJobStatus

queued

processing

completed

failed

---

## UserStatus

active

inactive

invited

---

# 6. Core Tables

## families

Purpose

Root aggregate seluruh sistem.

Columns

- id
- name
- currency_code
- created_at
- updated_at

---

## users

Purpose

Representasi akun autentikasi.

Columns

- id
- auth_user_id
- email
- status
- created_at
- updated_at

Catatan

auth_user_id mengacu pada Supabase Auth.

---

## family_members

Purpose

Representasi anggota keluarga.

Columns

- id
- family_id
- user_id (nullable)
- display_name
- role
- joined_at
- created_at
- updated_at

Catatan

user_id boleh NULL untuk anggota keluarga yang belum memiliki akun.

---

## categories

Purpose

Kategori transaksi.

Columns

- id
- family_id
- name
- type
- icon
- color
- created_at
- updated_at

---

## assets

Purpose

Representasi seluruh aset maupun kewajiban.

Columns

- id
- family_id
- owner_member_id (nullable)
- name
- asset_type
- institution
- account_number_last4
- initial_balance
- current_balance
- currency_code
- is_archived
- created_at
- updated_at

Catatan

owner_member_id boleh NULL apabila aset dimiliki bersama oleh keluarga.

---

## asset_valuations

Purpose

Riwayat perubahan nilai aset.

Columns

- id
- asset_id
- valuation_amount
- valuation_date
- notes
- created_at

---

## transactions

Purpose

Single Source of Truth seluruh pergerakan uang.

Columns

- id
- family_id
- member_id
- category_id
- source_asset_id (nullable)
- destination_asset_id (nullable)
- transaction_type
- source
- amount
- transaction_date
- merchant
- description
- attachment_url
- created_at
- updated_at

---

# 7. Automation Tables

## email_accounts

Columns

- id
- member_id
- email_address
- provider
- last_sync_at
- created_at
- updated_at

---

## email_messages

Columns

- id
- email_account_id
- provider_message_id
- sender
- subject
- snippet
- received_at
- processing_status
- created_at

provider_message_id wajib UNIQUE.

---

## receipts

Columns

- id
- member_id
- image_url
- uploaded_at
- upload_status
- created_at

---

## ocr_jobs

Columns

- id
- receipt_id
- status
- started_at
- completed_at
- created_at

---

## ocr_results

Columns

- id
- ocr_job_id
- raw_text
- confidence_score
- created_at

---

## transaction_drafts

Purpose

Area review sebelum menjadi Transaction.

Columns

- id
- family_id
- member_id
- source_type
- source_reference_id
- merchant
- amount
- transaction_date
- suggested_category_id
- suggested_source_asset_id
- suggested_destination_asset_id
- status
- reviewed_by
- reviewed_at
- created_at
- updated_at

---

# 8. Platform Tables

## sync_queue

Columns

- id
- entity_type
- entity_id
- operation
- status
- retry_count
- last_attempt_at
- created_at
- updated_at

Menggunakan pola polymorphic reference.

---

## audit_logs

Columns

- id
- family_id
- member_id
- entity_type
- entity_id
- action
- old_value (JSONB)
- new_value (JSONB)
- created_at

---

# 9. Relationship Rules

Family

1

↓

N

FamilyMember

---

Family

1

↓

N

Category

---

Family

1

↓

N

Asset

---

FamilyMember

1

↓

N

Transaction

---

Category

1

↓

N

Transaction

---

Asset

1

↓

N

Transaction

(role = source)

---

Asset

1

↓

N

Transaction

(role = destination)

---

Asset

1

↓

N

AssetValuation

---

EmailAccount

1

↓

N

EmailMessage

---

Receipt

1

↓

N

OCRJob

---

OCRJob

1

↓

1

OCRResult

---

EmailMessage

1

↓

0..1

TransactionDraft

---

OCRResult

1

↓

0..1

TransactionDraft

---

TransactionDraft

1

↓

0..1

Transaction

---

# 10. Constraints

UNIQUE

- users.email
- email_messages.provider_message_id

---

NOT NULL

- family_id
- member_id
- category_id
- amount
- transaction_date

---

CHECK

TransactionType

- income
- expense
- transfer
- adjustment

---

CHECK

Amount > 0

---

# 11. Index Strategy

Primary Index

Seluruh Primary Key.

---

Secondary Index

transactions

- family_id
- member_id
- transaction_date
- category_id

---

assets

- family_id
- owner_member_id

---

transaction_drafts

- status
- source_type

---

email_messages

- provider_message_id

---

audit_logs

- entity_type
- entity_id

---

# 12. JSONB Usage

JSONB hanya digunakan untuk data semi-structured.

audit_logs

old_value

new_value

Future

OCR metadata

AI reasoning

Parser confidence

---

# 13. Soft Delete Strategy

WorthFlow tidak menggunakan DELETE fisik untuk data finansial.

Sebagai gantinya digunakan:

is_archived

atau

status

Audit Log tetap menyimpan histori perubahan.

---

# 14. Timestamp Strategy

Semua waktu menggunakan

TIMESTAMP WITH TIME ZONE

Timezone default

UTC

Konversi timezone dilakukan pada level aplikasi.

---

# 15. Row Level Security (Supabase)

Seluruh tabel domain menggunakan Row Level Security.

Aturan utama

User hanya dapat mengakses data dari Family tempat dirinya menjadi anggota.

Policy secara umum

family_id IN (
    daftar family milik current user
)

---

# 16. Migration Strategy

Urutan pembuatan tabel

1. families

2. users

3. family_members

4. categories

5. assets

6. asset_valuations

7. transactions

8. email_accounts

9. email_messages

10. receipts

11. ocr_jobs

12. ocr_results

13. transaction_drafts

14. sync_queue

15. audit_logs

Urutan ini menjaga integritas seluruh Foreign Key.

---

# 17. Future Extension

Schema dirancang agar mudah dikembangkan.

Entity yang direncanakan

- budgets
- financial_goals
- investment_portfolios
- recurring_transactions
- notifications
- ai_insights
- exchange_rates
- attachments