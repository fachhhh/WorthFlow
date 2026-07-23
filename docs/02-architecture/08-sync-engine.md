# Sync Engine
*Version: 0.1 Draft*

# Sync Engine Design
## Overview

Sync Engine adalah komponen yang bertanggung jawab menjaga konsistensi data antara:

```text
Mobile Local Database
```

dan

```text
Cloud Database
```

dalam kondisi:

* Online
* Offline
* Intermittent Connection
* Failed Network Request

# Goals

Sync Engine harus mampu:

1. Menjamin data tidak hilang.
2. Menjamin perubahan lokal tetap tersimpan saat offline.
3. Menyinkronkan data secara otomatis saat online.
4. Mencegah duplikasi data.
5. Menangani kegagalan jaringan secara aman.

# Architecture Overview

```text
User Action
      │
      ▼
Local Database
      │
      ▼
Sync Queue
      │
      ▼
Sync Worker
      │
      ▼
Backend API
      │
      ▼
Cloud Database
```

# Design Principles

## Principle 1 — Local Source First

Semua perubahan disimpan terlebih dahulu secara lokal.

Tidak ada operasi yang langsung menulis ke cloud.

## Principle 2 — Queue Based Synchronization

Semua perubahan data harus masuk ke antrean sinkronisasi.

Tidak ada perubahan yang langsung dikirim ke server.

## Principle 3 — Idempotent Operations

Operasi yang sama tidak boleh menghasilkan data ganda.

Contoh:

```text
Create Transaction
Retry
Retry
Retry
```

Tetap menghasilkan:

```text
1 Transaction
```

bukan:

```text
3 Transactions
```

## Principle 4 — Background Processing

Sinkronisasi harus berjalan di background.

User tidak perlu menekan tombol:

```text
Sync Now
```

untuk penggunaan normal.

# Sync Queue Architecture

## Queue Entity

Setiap perubahan menghasilkan Queue Item.

Structure:

```text
queue_id

entity_type

entity_id

operation

payload

status

retry_count

created_at
```

# Entity Types

```text
TRANSACTION

ASSET

RECEIPT

CATEGORY
```

# Operation Types

```text
CREATE

UPDATE

DELETE
```

# Queue Status

```text
PENDING

PROCESSING

SUCCESS

FAILED
```

# Example Queue

```text
Q001

TRANSACTION

CREATE

PENDING
```

```text
Q002

ASSET

UPDATE

PENDING
```

# Sync Worker

## Responsibilities

* membaca queue
* mengirim data ke backend
* menangani retry
* memperbarui status queue

Flow:

```text
Read Queue
↓
Take Oldest Item
↓
Send API Request
↓
Receive Response
↓
Update Queue Status
```

# Processing Strategy

MVP menggunakan:

```text
FIFO
```

First In First Out

Reason:

* sederhana
* mudah di-debug
* cukup untuk skala keluarga

# Create Flow

## Local Transaction Creation

```text
User Create Transaction
↓
Save Local Database
↓
Generate UUID
↓
Insert Queue Item
↓
Show Success
```

## Sync Flow

```text
Queue Item
↓
API Request
↓
Backend Success
↓
Mark Queue Success
↓
Mark Transaction Synced
```

# Update Flow

```text
User Update Transaction
↓
Update Local Record
↓
Create Queue Item
↓
Sync Later
```

# Delete Flow

MVP menggunakan Soft Delete.

Flow:

```text
Delete Transaction
↓
Set Status Deleted
↓
Queue Delete Event
↓
Sync
```

# Idempotency Strategy

## Problem

Network timeout dapat menyebabkan:

```text
Client Tidak Tahu
Apakah Data Sudah Masuk
Atau Belum
```

## Solution

Setiap record memiliki:

```text
client_generated_uuid
```

Example:

```text
txn_84f71d12
```

Server akan memeriksa:

```text
Apakah UUID Sudah Ada?
```

Jika ada:

```text
Return Existing Record
```

Tidak membuat data baru.

# Sync Status Lifecycle

```text
PENDING
↓
PROCESSING
↓
SUCCESS
```

Jika gagal:

```text
PENDING
↓
PROCESSING
↓
FAILED
```

# Retry Mechanism

Jika request gagal:

```text
Retry #1
1 Minute

Retry #2
5 Minutes

Retry #3
15 Minutes

Retry #4
30 Minutes

Retry #5
60 Minutes
```

Maximum:

```text
5 Retries
```

Setelah itu:

```text
FAILED
```

# Conflict Resolution

## MVP Strategy

```text
Last Write Wins
```

Contoh:

Transaction:

```text
Amount = 100000
```

Device A:

```text
Update
110000
09:00
```

Device B:

```text
Update
120000
09:05
```

Result:

```text
120000
```

Karena timestamp lebih baru.

# Device Model

MVP menggunakan:

```text
Single Active Device Assumption
```

Artinya:

Mayoritas pengguna diasumsikan menggunakan satu perangkat utama.

Future:

```text
Phone
Tablet
Web
```

dapat didukung melalui Device Entity.

# Sync Triggers

## Trigger A

Application Launch

```text
App Open
↓
Sync
```

## Trigger B

Connection Restored

```text
Offline
↓
Online
↓
Sync
```

## Trigger C

Periodic Check

```text
Every 5 Minutes
```

saat aplikasi aktif.

# Receipt Synchronization

Receipt image disimpan lokal terlebih dahulu.

Flow:

```text
Capture Image
↓
Store Local File
↓
Queue Upload
↓
Cloud Storage
```

Setelah upload berhasil:

```text
Create OCR Job
```

# Asset Synchronization

Asset diperlakukan sama seperti transaksi.

Flow:

```text
Create Asset
↓
Local Save
↓
Queue
↓
Sync
```

# Queue Recovery

Jika aplikasi ditutup:

```text
Pending Queue
```

tetap tersimpan.

Saat aplikasi dibuka kembali:

```text
Resume Sync
```

# Failure Scenarios

## No Internet

```text
Keep Pending
```

## API Error

```text
Retry
```

## Server Error

```text
Retry
```

## Validation Error

```text
Failed
Manual Review Required
```

# Metrics

Sync Engine harus mencatat:

```text
sync_attempts

sync_success

sync_failures

average_sync_time
```

# Audit Events

Event berikut harus dicatat:

```text
Sync Started

Sync Success

Sync Failed

Conflict Detected
```

# Security Considerations

Payload harus dikirim melalui:

```text
HTTPS
```

Token harus diverifikasi sebelum sinkronisasi.

# Future Enhancements

Tidak termasuk MVP.

## Delta Sync

Hanya data yang berubah yang dikirim.

## Multi Device Synchronization

```text
Device A
↔
Cloud
↔
Device B
```

## Conflict Resolution UI

User dapat memilih versi data.

## Sync Priority Queue

Prioritas berbeda untuk:

```text
Transactions

Assets

Receipts
```

# Architecture Summary

WorthFlow menggunakan:

```text
Queue Based Synchronization

Background Processing

Idempotent Operations

Last Write Wins

Automatic Retry

Eventual Consistency
```

untuk memastikan data tetap aman meskipun koneksi internet tidak stabil.