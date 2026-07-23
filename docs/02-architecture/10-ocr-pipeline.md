# 10-ocr-pipeline.md
*Version: 0.1 Draft*

# OCR Pipeline Design

## Overview

OCR Pipeline memungkinkan pengguna mengubah foto struk, nota, invoice, atau bukti pembayaran menjadi kandidat transaksi secara otomatis.

Tujuan utama:

* Mengurangi input manual
* Mempercepat pencatatan transaksi
* Mengurangi human error
* Mendukung pencatatan saat bepergian

# Goals

Sistem harus mampu:

1. Menerima foto receipt.
2. Mengekstrak teks dari gambar.
3. Mengidentifikasi informasi transaksi.
4. Membuat transaction draft.
5. Memungkinkan koreksi sebelum data final dibuat.
6. Menyimpan histori OCR untuk audit dan debugging.

# Design Principles

## Principle 1 — Human Verified

OCR tidak pernah langsung membuat transaksi final.

Flow:

```text
Receipt
↓
Draft
↓
Review
↓
Transaction
```

## Principle 2 — Source Preservation

Gambar asli harus tetap tersedia setelah proses OCR.

Tujuan:

* Audit
* Reprocessing
* Verifikasi pengguna

## Principle 3 — OCR ≠ Data Extraction

OCR hanya menghasilkan teks.

AI Extraction bertugas menghasilkan data terstruktur.

# High Level Architecture

```text
Receipt Image
↓
Upload
↓
OCR Engine
↓
Raw Text
↓
AI Extraction
↓
Transaction Draft
↓
User Review
↓
Transaction
```

# OCR Engine Strategy

## MVP Choice

Hybrid Approach

```text
OCR
+
AI Extraction
```

### OCR Layer

Menghasilkan:

```text
Raw Text
```

Contoh:

```text
INDOMARET

TOTAL BELANJA
125000

TERIMA KASIH
```

### AI Extraction Layer

Menghasilkan:

```json
{
  "merchant": "Indomaret",
  "amount": 125000,
  "category": "Groceries"
}
```

# Why Hybrid?

OCR:

* Murah
* Cepat
* Deterministik

AI:

* Lebih pintar memahami konteks
* Dapat menangani berbagai format receipt

# OCR Pipeline Flow

## Step 1

User mengambil foto.

```text
Camera
↓
Receipt Image
```

## Step 2

Receipt disimpan.

```text
Receipt
status = uploaded
```

## Step 3

OCR dijalankan.

```text
Receipt
↓
OCR Job
```

## Step 4

Raw text dihasilkan.

```text
OCR Result
```

## Step 5

AI Extraction dijalankan.

```text
Raw Text
↓
Structured Data
```

## Step 6

Transaction Draft dibuat.

```text
Draft
status = pending_review
```

## Step 7

User melakukan review.

```text
Approve
Reject
Edit
```

# Domain Model

## Receipt

Representasi gambar struk.

Fields:

```text
receipt_id

member_id

file_url

capture_time

upload_status
```

# OCR Job

Representasi proses OCR.

Fields:

```text
ocr_job_id

receipt_id

status

started_at

completed_at
```

Possible Status:

```text
PENDING

PROCESSING

SUCCESS

FAILED
```

# OCR Result

Menyimpan hasil OCR.

Fields:

```text
ocr_result_id

ocr_job_id

raw_text

confidence_score
```

Confidence Example:

```text
0.94
```

# AI Extraction

Mengubah raw text menjadi data terstruktur.

Output Example

```json
{
  "merchant": "KFC",
  "amount": 150000,
  "transaction_date": "2026-01-10",
  "category": "Food"
}
```

# Transaction Draft Integration

OCR tidak membuat transaksi langsung.

Flow:

```text
OCR Result
↓
AI Extraction
↓
Transaction Draft
```

Transaction Draft menjadi pusat seluruh automation.

Sources:

```text
EMAIL
OCR
```

# User Review Flow

## Approve

```text
Draft
↓
Approve
↓
Transaction
```

## Edit

```text
Draft
↓
Edit
↓
Approve
↓
Transaction
```

## Reject

```text
Draft
↓
Reject
```

# Duplicate Detection

Sistem mencoba mendeteksi transaksi yang sudah ada.

Matching Fields

```text
Amount

Date

Merchant
```

Possible Result

```text
NO_MATCH

POSSIBLE_DUPLICATE

CONFIRMED_DUPLICATE
```

# Offline Behaviour

## Offline Supported

```text
Capture Receipt
Store Image
```

## Offline Not Supported

```text
OCR Processing
AI Extraction
```

Flow:

```text
Capture
↓
Store Local
↓
Sync Later
↓
OCR
```

# Error Handling

## Image Blur

Status:

```text
LOW_QUALITY_IMAGE
```

## OCR Failure

Status:

```text
OCR_FAILED
```

## AI Extraction Failure

Status:

```text
EXTRACTION_FAILED
```

## Unsupported Receipt

Status:

```text
UNSUPPORTED_FORMAT
```

# Quality Validation

Sebelum OCR dijalankan:

```text
Check Resolution

Check Brightness

Check Blur
```

Jika gagal:

```text
Manual Review Required
```

# Security Design

Receipt dapat mengandung:

```text
Merchant
Card Information
Address
Phone Number
```

Sensitive information harus:

```text
Encrypted At Rest
```

untuk penyimpanan cloud.

# Audit Events

Catat:

```text
Receipt Uploaded

OCR Started

OCR Completed

Draft Created

Draft Approved

Draft Rejected
```

# Metrics

Sistem mencatat:

```text
receipts_uploaded

ocr_success_rate

ocr_failure_rate

average_processing_time

draft_approval_rate
```

# Future Enhancements

Tidak termasuk MVP.

## Offline OCR

Menggunakan OCR engine lokal.

## Multi Receipt Processing

Batch OCR.

## Merchant Recognition

Database merchant otomatis.

## Smart Categorization

Kategori otomatis berdasarkan histori transaksi.

## Receipt Line Item Extraction

Contoh:

```text
Nasi Goreng
Es Teh
Ayam Goreng
```

bukan hanya total transaksi.

# Architecture Summary

WorthFlow menggunakan pendekatan:

```text
Receipt
↓
OCR Engine
↓
Raw Text
↓
AI Extraction
↓
Transaction Draft
↓
Human Review
↓
Transaction
```

untuk memastikan hasil OCR tetap akurat, dapat diaudit, dan tidak langsung mempengaruhi data keuangan keluarga tanpa verifikasi pengguna.