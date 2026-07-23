# System Architecture
*Version: 0.1 Draft*

Dokumen ini mendefinisikan arsitektur tingkat tinggi (High Level Architecture) untuk WorthFlow.

Fokus utama arsitektur:

* Offline First
* Mobile First
* Low Cost (Rp 0 selama MVP)
* Mudah di-maintain oleh satu developer
* Mudah di-scale jika pengguna bertambah

# Architecture Principles

## 1. Mobile First

Platform utama adalah aplikasi mobile.

Seluruh fitur inti harus dapat digunakan melalui aplikasi mobile.

Web hanya berfungsi sebagai:

* Admin dashboard
* Monitoring
* Audit
* Reporting

## 2. Offline First

Input transaksi tidak boleh bergantung pada internet.

Setiap transaksi harus terlebih dahulu disimpan secara lokal sebelum dikirim ke cloud.

## 3. Single Source of Truth

Data utama disimpan pada database cloud.

Spreadsheet hanya berfungsi sebagai:

* Reporting
* Backup ringan
* Analisis tambahan

## 4. Human Verification

Seluruh hasil otomatisasi:

* OCR
* Email Parsing

harus dapat diverifikasi oleh pengguna sebelum menjadi data final.

# High Level Architecture

```text
                ┌─────────────────────┐
                │     Mobile App      │
                └──────────┬──────────┘
                           │
                     Local Database
                           │
                           ▼
                      Sync Engine
                           │
                           ▼
                ┌─────────────────────┐
                │     Backend API     │
                └──────────┬──────────┘
                           │
         ┌─────────────────┼──────────────────┐
         ▼                 ▼                  ▼
   PostgreSQL        Object Storage      Audit Log
                           │
                           ▼
                    Google Sheets
```

# System Components
## Mobile Application
Platform utama pengguna.

### Responsibilities

* Authentication
* Transaction Management
* Offline Storage
* Dashboard
* Asset Tracking
* OCR Upload
* Sync Management

### Local Storage

Digunakan untuk:

```text
Users
Transactions
Assets
Pending Sync Queue
Settings
```

### Benefits

* Tetap berjalan tanpa internet
* Input cepat
* UX lebih baik

# Sync Engine

Komponen paling penting dalam WorthFlow.

### Responsibilities

* Menyimpan transaksi offline
* Mengirim transaksi ke cloud
* Retry jika gagal
* Mencegah duplikasi

### Sync Strategy

```text
Create Transaction
↓
Save Local
↓
Pending Queue
↓
Background Sync
↓
Cloud Database
↓
Mark Synced
```

### Conflict Strategy (MVP)

Menggunakan:

```text
Last Write Wins
```

Versi awal mengutamakan kesederhanaan.

# Backend API

Backend berfungsi sebagai pusat logika bisnis.

### Responsibilities

* Authentication
* Authorization
* Transaction Processing
* Asset Processing
* Audit Logging
* Email Integration
* OCR Processing Coordination

### Non Responsibilities

Backend tidak melakukan:

* Spreadsheet sebagai database utama
* Analisis berat
* Machine Learning Training

# Database Layer

Database utama.

### Responsibilities

* Menyimpan data permanen
* Menjadi source of truth

### Data Domains

```text
Users
Families
Transactions
Assets
Receipts
Email Records
Audit Logs
```

# Object Storage

Digunakan untuk menyimpan file.

### Stored Objects

* Receipt Images
* OCR Source Files
* Attachment Files

### Not Stored

* Structured Financial Data

Data finansial tetap berada di database.

# OCR Pipeline

Tujuan:

Mengubah foto struk menjadi transaksi.

## Flow

```text
Receipt Image
↓
OCR Engine
↓
Raw Text
↓
AI Extraction
↓
Draft Transaction
↓
User Review
↓
Final Transaction
```

## OCR Responsibilities

Menghasilkan:

```text
Raw Text
```

Contoh:

```text
INDOMARET

TOTAL : 125000
```

## AI Extraction Responsibilities

Menghasilkan:

```json
{
  "merchant": "Indomaret",
  "amount": 125000,
  "category": "Groceries"
}
```

## Verification Layer

User wajib melakukan review sebelum data final dibuat.

# Email Ingestion Pipeline

Tujuan:

Menghasilkan transaksi dari email bank.

## Flow

```text
Email
↓
Parser
↓
Candidate Transaction
↓
User Review
↓
Final Transaction
```

## Responsibilities

Mengidentifikasi:

* Merchant
* Amount
* Transaction Date
* Bank

## Supported Sources

MVP:

```text
Gmail
```

## Future Sources

* Outlook
* Yahoo

# Analytics Layer

Menghasilkan data dashboard.

## Responsibilities

### Cash Flow

```text
Income - Expense
```

### Net Worth

```text
Assets - Liabilities
```

### Expense Analysis

* Category Distribution
* Monthly Trends
* Spending Pattern

# Spreadsheet Integration

Spreadsheet bukan database utama.

## Purpose

* Reporting
* Family Sharing
* Backup

## Flow

```text
Database
↓
Export Service
↓
Google Sheets
```

# Admin Web Architecture

Digunakan untuk monitoring.

### Features

* Audit Logs
* User Management
* Sync Monitoring
* Export Management

### Not Intended For

* Daily transaction input
* Receipt upload

# Security Architecture

## Authentication

```text
User
↓
Login
↓
Access Token
↓
API Access
```

## Authorization

Role Based Access Control.

### Roles

```text
Admin
Member
```

## Data Isolation

Setiap keluarga hanya dapat mengakses data miliknya sendiri.

# Error Handling

## Offline Mode

Jika internet tidak tersedia:

```text
Transaction
↓
Local Storage
↓
Pending Sync
```

## OCR Failure

Jika OCR gagal:

```text
Receipt
↓
Manual Input
```

## Email Parsing Failure

Jika parser gagal:

```text
Email
↓
Review Required
```

# Scalability Strategy

MVP menggunakan:

```text
Monolith Backend
```

## Why?

Karena:

* User sedikit
* Gratis
* Lebih mudah di-maintain
* Lebih cepat dikembangkan

## Not Using

* Kubernetes
* Service Mesh
* Event Streaming
* Distributed Systems

# Deployment Architecture (MVP)

```text
Mobile App
     │
     ▼
Backend API
     │
     ▼
Supabase
     │
     ├── PostgreSQL
     ├── Storage
     └── Auth (optional)
```

# Observability

MVP minimal memiliki:

### Application Logs

* Login
* Transaction
* OCR
* Email Parsing

### Audit Logs

* Create
* Update
* Delete

### Error Tracking

* Sync Errors
* OCR Errors
* Parser Errors

# Architecture Decisions

## AD-001

```text
Offline First
```

Dipilih karena pengguna dapat mencatat transaksi kapan saja.

## AD-002

```text
Cloud Database
```

Dipilih agar data tidak hilang ketika perangkat rusak.

## AD-003

```text
Human Verified Automation
```

Dipilih untuk mengurangi kesalahan OCR dan email parser.

## AD-004

```text
Monolith First
```

Dipilih untuk mempercepat pengembangan dan mengurangi kompleksitas.

# Architecture Summary

WorthFlow dibangun menggunakan pendekatan:

```text
Mobile First
Offline First
Cloud Synced
Human Verified Automation
Monolithic Backend
```

dengan tujuan menyediakan satu sumber kebenaran untuk seluruh aktivitas keuangan keluarga.