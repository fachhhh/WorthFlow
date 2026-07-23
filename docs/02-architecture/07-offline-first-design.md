# Offline First Design
*Version: 0.1 Draft*

## Overview
WorthFlow mengadopsi pendekatan **Offline First Architecture**.

Seluruh aktivitas penting pengguna harus tetap dapat dilakukan meskipun perangkat tidak memiliki koneksi internet.

Tujuan utama pendekatan ini adalah:

* Mengurangi risiko kehilangan transaksi
* Mempercepat input data
* Menghilangkan ketergantungan terhadap jaringan
* Meningkatkan pengalaman pengguna non-teknis

# Design Principles

## Principle 1 — Local First

Setiap data yang dibuat pengguna harus disimpan terlebih dahulu pada perangkat lokal.

Tidak ada proses yang langsung bergantung pada server.

Flow:

```text
User Action
↓
Local Database
↓
Sync Queue
↓
Cloud Database
```

## Principle 2 — Never Block User Input

Pengguna tidak boleh melihat pesan:

```text
"Gagal menyimpan karena tidak ada internet"
```

Selama data valid, transaksi harus tetap diterima.

## Principle 3 — Eventual Consistency

Data lokal dan cloud tidak harus identik secara real-time.

Konsistensi dicapai melalui proses sinkronisasi bertahap.

## Principle 4 — Sync Transparency

Pengguna harus mengetahui status sinkronisasi tanpa harus memahami detail teknis.

Status yang digunakan:

```text
Pending
Syncing
Synced
Failed
```

# Offline Capabilities Matrix

| Feature               | Offline |
| --------------------- | ------- |
| Login Session         | ✅       |
| Dashboard Cached Data | ✅       |
| Create Transaction    | ✅       |
| Edit Transaction      | ✅       |
| Delete Transaction    | ✅       |
| Asset Management      | ✅       |
| Receipt Upload        | ✅       |
| OCR Processing        | ❌       |
| Email Import          | ❌       |
| Google Sheets Sync    | ❌       |
| Real-Time Refresh     | ❌       |

# Local Data Architecture

## Local Database

Mobile application menyimpan subset data menggunakan database lokal.

Entity yang disimpan:

```text
User
Family
FamilyMember

Transaction
Category

Asset
AssetValuation

Receipt

SyncQueue
```

## Local Database Responsibilities

* Menyimpan data saat offline
* Menjadi cache saat online
* Menyimpan antrean sinkronisasi
* Menyediakan pengalaman aplikasi yang cepat

# Transaction Lifecycle

## Create Transaction

Saat pengguna membuat transaksi:

```text
Input Form
↓
Validation
↓
Save Local Database
↓
Create Sync Queue Item
↓
Show Success
```

Tidak ada komunikasi server pada tahap ini.

## Edit Transaction

```text
Edit Transaction
↓
Update Local Record
↓
Create Sync Queue Item
↓
Mark Pending Sync
```

## Delete Transaction

```text
Delete Transaction
↓
Soft Delete Local
↓
Create Sync Queue Item
↓
Sync Later
```

# Sync Queue Design

Seluruh perubahan data akan dicatat ke antrean sinkronisasi.

## Queue Operation Types

```text
CREATE
UPDATE
DELETE
```

## Queue Example

```text
Queue Item #1
CREATE Transaction

Queue Item #2
UPDATE Asset

Queue Item #3
DELETE Transaction
```

# Sync Trigger Strategy

Sinkronisasi akan dipicu oleh:

## Trigger A

Internet kembali tersedia.

```text
Offline
↓
Online
↓
Start Sync
```

## Trigger B

User membuka aplikasi.

```text
App Launch
↓
Check Connection
↓
Sync
```

## Trigger C

Periodic Sync

```text
Every X Minutes
```

hanya jika aplikasi aktif.

# Receipt Handling

Receipt tetap dapat diunggah saat offline.

Flow:

```text
Take Photo
↓
Store Local File
↓
Create Queue Item
↓
Wait Until Online
```

Saat online:

```text
Upload Receipt
↓
OCR Pipeline
↓
Transaction Draft
```

# Dashboard Behaviour

## Online

Dashboard menggunakan data terbaru dari server.

## Offline

Dashboard menggunakan cache lokal.

Indikator:

```text
Last Updated:
12 July 2026
09:30
```

# Asset Behaviour

Seluruh aset dapat:

```text
Create
Update
Delete
```

saat offline.

Net worth tetap dapat dihitung menggunakan data lokal.

# Conflict Management

MVP menggunakan strategi sederhana:

```text
Last Write Wins
```

Contoh:

Device A

```text
Transaction Amount
100000
```

Device B

```text
Transaction Amount
120000
```

Data dengan timestamp terbaru akan menjadi versi final.

# Soft Delete Strategy

Data tidak langsung dihapus.

Status:

```text
ACTIVE
DELETED
```

Keuntungan:

* Mudah recovery
* Mudah audit
* Aman saat sinkronisasi

# Network Detection

Aplikasi akan memonitor:

```text
Internet Available
Server Reachable
```

State:

```text
ONLINE
OFFLINE
DEGRADED
```

# Sync Status Indicator

Setiap transaksi memiliki status sinkronisasi.

Possible Values
```text
PENDING
SYNCING
SYNCED
FAILED
```

Visual Example
```text
🟢 Synced

🟡 Pending

🔴 Failed
```

# Error Recovery
## Failed Sync
Jika sinkronisasi gagal:
```text
Retry Automatically
```

Retry Strategy
```text
1 minute
5 minutes
15 minutes
30 minutes
```
Maximum retries:

```text
5 attempts
```

# Security Considerations
Data lokal tetap harus dilindungi.

Stored Securely
```text
Access Token
Refresh Token
Session Data
```
Sensitive fields dapat dienkripsi sebelum disimpan.

# Data Ownership
Setiap record harus memiliki:
```text
family_id
created_by
updated_by
```
untuk memastikan sinkronisasi dan audit berjalan dengan baik.

# Future Enhancements
Tidak termasuk MVP.

## Multi Device Sync
```text
Phone
Tablet
Web
```
sinkronisasi dua arah penuh.

## Conflict Resolution UI
User dapat memilih versi data saat terjadi konflik.

## Offline OCR
Menggunakan OCR engine lokal di perangkat.

# Architecture Summary
WorthFlow menggunakan pendekatan:
```text
Local First
Offline First
Queue Based Sync
Eventual Consistency
Last Write Wins
```
di mana seluruh data pengguna disimpan terlebih dahulu pada perangkat sebelum disinkronkan ke cloud.