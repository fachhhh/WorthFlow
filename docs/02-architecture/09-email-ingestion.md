# Email Ingestion
*Version: 0.1 Draft*

# Email Ingestion Design

## Overview

Email Ingestion adalah fitur yang memungkinkan WorthFlow mengubah email notifikasi transaksi bank menjadi kandidat transaksi yang dapat ditinjau pengguna.

Tujuan utama:

* Mengurangi input manual
* Mengurangi transaksi yang terlupakan
* Meningkatkan kelengkapan data keuangan keluarga

# Goals

Sistem harus mampu:

1. Membaca email dari akun Gmail yang terhubung.
2. Mengidentifikasi email transaksi bank.
3. Mengekstrak data transaksi.
4. Menghasilkan transaction draft.
5. Mencegah email diproses lebih dari sekali.
6. Memungkinkan review sebelum menjadi transaksi final.

# Design Principles

## Principle 1 — Human Verified

Tidak ada email yang langsung menjadi transaksi final.

Flow:

```text
Email
↓
Draft
↓
Review
↓
Transaction
```

## Principle 2 — Source Traceability

Setiap transaksi harus dapat ditelusuri kembali ke email asalnya.

## Principle 3 — Idempotent Processing

Email yang sama tidak boleh menghasilkan transaksi ganda.

# High Level Flow

```text
Gmail
↓
Email Sync
↓
Email Message
↓
Parser
↓
Transaction Draft
↓
User Review
↓
Transaction
```

# Supported Providers

## MVP

```text
Gmail
```

## Future

```text
Outlook
Yahoo
Open Banking API
```

# Domain Model

## Email Account

Representasi akun email yang terhubung.

Fields:

```text
email_account_id

member_id

email_address

provider

status

last_sync_at
```

# Email Message

Representasi email yang berhasil diambil.

Fields:

```text
email_message_id

email_account_id

provider_message_id

subject

sender

received_at

processing_status
```

# Why Store Email Message?

Untuk:

* audit
* deduplication
* debugging parser
* reprocessing

# Processing Lifecycle

## Stage 1

Email ditemukan.

Status:

```text
RECEIVED
```

## Stage 2

Parser dijalankan.

Status:

```text
PROCESSING
```

## Stage 3

Parser berhasil.

Status:

```text
PARSED
```

## Stage 4

Draft dibuat.

Status:

```text
DRAFT_CREATED
```

## Stage 5

Gagal diproses.

Status:

```text
FAILED
```

# Email Detection

Parser hanya memproses email yang cocok dengan rule tertentu.

Example:

```text
Debit BCA

Transaksi Kartu Kredit

Transfer Masuk
```

# Parser Strategy

MVP menggunakan:

```text
Rule Based Parsing
```

Bukan:

```text
AI Parsing
```

Reason:

* gratis
* cepat
* mudah dipelihara
* mudah di-debug

# Parser Output

Parser menghasilkan:

```json
{
  "merchant": "Tokopedia",
  "amount": 250000,
  "transaction_date": "2026-01-10",
  "bank": "BCA"
}
```

# Transaction Draft

Draft adalah hasil parser yang belum disetujui.

Fields:

```text
draft_id

source_type

source_reference

status
```

Possible Status:

```text
PENDING_REVIEW

APPROVED

REJECTED
```

# User Review Flow

```text
Draft
↓
Review
↓
Approve
↓
Transaction
```

atau

```text
Draft
↓
Reject
```

# Duplicate Detection

## Problem

Email bank dapat:

* diterima dua kali
* disinkronisasi ulang
* diproses ulang

## Solution

Gunakan:

```text
provider_message_id
```

sebagai unique identifier.

Jika sudah ada:

```text
Skip Processing
```

# Transaction Matching

Sistem mencoba mendeteksi apakah transaksi sudah dicatat secara manual.

Matching Fields:

```text
Amount

Date

Merchant
```

Example

Manual:

```text
Tokopedia
250000
```

Email:

```text
Tokopedia
250000
```

Result:

```text
Possible Duplicate
```

# Duplicate States

```text
NO_MATCH

POSSIBLE_DUPLICATE

CONFIRMED_DUPLICATE
```

# Sync Schedule

Email tidak diproses real-time.

MVP:

```text
Every 15 Minutes
```

atau

```text
Manual Refresh
```

# Security Design

## Access Scope

Aplikasi hanya meminta izin yang diperlukan.

Read Only Access

```text
Read Gmail Messages
```

Tidak memiliki izin:

```text
Delete Email

Send Email
```

# Privacy Design

Email lengkap tidak perlu disimpan permanen.

Store:

```text
Metadata

Parsed Result

Reference ID
```

Optional:

```text
Email Body
```

untuk debugging.

# Error Handling

## Gmail API Failure

Status:

```text
SYNC_FAILED
```

## Parser Failure

Status:

```text
PARSE_FAILED
```

## Invalid Format

Status:

```text
UNSUPPORTED_FORMAT
```

# Audit Events

Catat:

```text
Email Synced

Email Parsed

Draft Created

Draft Approved

Draft Rejected
```

# Metrics

Sistem mencatat:

```text
emails_received

emails_parsed

drafts_created

drafts_approved

parser_failures
```

# Future Enhancements

Tidak termasuk MVP.

## AI Parsing

Menggunakan LLM untuk format email yang kompleks.

## Multi Bank Support

Parser per bank.

## Auto Categorization

Kategori otomatis berdasarkan merchant.

## Auto Approval Rules

Contoh:

```text
Jika merchant = PLN

Approve otomatis
```

# Architecture Summary

WorthFlow menggunakan pendekatan:

```text
Email Account
↓
Email Message
↓
Rule Based Parser
↓
Transaction Draft
↓
Human Review
↓
Transaction
```

untuk memastikan transaksi hasil email tetap akurat dan dapat diaudit.