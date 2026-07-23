# Product Roadmap
*Version: 0.1 Draft*

Dokumen ini mendefinisikan urutan pengembangan WorthFlow dari fase perencanaan hingga digunakan oleh anggota keluarga dalam kondisi nyata.

Roadmap difokuskan pada:
* Mengurangi risiko teknis
* Menghasilkan MVP secepat mungkin
* Memvalidasi penggunaan nyata
* Menjaga biaya operasional tetap Rp 0 selama fase awal

# Development Philosophy
WorthFlow dikembangkan menggunakan pendekatan:
```text
Build
→ Use
→ Learn
→ Improve
```

Bukan:
```text
Build Everything
→ Release
```

Setiap fase harus menghasilkan sesuatu yang dapat diuji secara nyata.

# Phase 0 — Planning & Design
Target:
Menyelesaikan seluruh dokumentasi inti.

## Deliverables
### Product
* [x] Vision
* [x] PRD
* [x] User Stories
* [x] MVP Scope
* [ ] Roadmap

### Architecture
* [ ] System Architecture
* [ ] Offline First Design
* [ ] Sync Engine Design
* [ ] Email Ingestion Design
* [ ] OCR Pipeline Design

### Database
* [ ] ERD
* [ ] Schema Design

### API
* [ ] API Specification

## Exit Criteria
Seluruh dokumentasi inti selesai.

# Phase 1 — Foundation
Estimasi:
Week 1–2

## Objective
Membangun fondasi aplikasi.

## Features
### Authentication
* Register
* Login
* Logout
* Session Persistence

### Family Workspace
* Create Family
* Join Family
* Role Management

### Initial Database
* User
* Family
* Membership

### Mobile Setup
* Navigation
* Theme
* State Management
* Local Database

### Backend Setup
* Authentication API
* User API
* Family API

## Exit Criteria
User dapat login dan masuk ke family workspace.

# Phase 2 — Core Transaction System
Estimasi:
Week 3–4

## Objective
Membangun sistem transaksi inti.

## Features
### Transactions
* Create
* Update
* Delete
* List

### Categories
* Food
* Transportation
* Utilities
* Health
* Entertainment
* Education
* Other

### Offline Storage
* Local database
* Local transaction repository

### Dashboard V1
* Total Income
* Total Expense
* Recent Transactions

## Exit Criteria
Transaksi dapat dibuat dan ditampilkan.


# Phase 3 — Offline First
Estimasi:
Week 5–6

## Objective
Membangun kemampuan offline.

## Features
### Sync Queue
* Pending transactions
* Retry mechanism

### Auto Sync
* Background synchronization
* Online detection

### Sync Status
* Synced
* Pending
* Failed

### Conflict Handling
Versi sederhana:
```text
Last Write Wins
```

## Exit Criteria
User dapat mencatat transaksi tanpa internet.

# Phase 4 — Asset Tracking
Estimasi:
Week 7

## Objective
Menghitung net worth keluarga.

## Features
### Assets
* Cash
* Bank Account
* Deposito
* Saham
* Crypto
* Property

### Dashboard V2
* Asset Summary
* Net Worth

## Exit Criteria
Net worth berhasil dihitung.

# Phase 5 — OCR Pipeline
Estimasi:
Week 8–9

## Objective
Mengurangi input manual.

## Features
### Receipt Upload
* Camera
* Gallery

### OCR
Versi MVP:
```text
Receipt
↓
OCR
↓
Raw Text
```

### AI Extraction
```text
Raw Text
↓
AI Extraction
↓
Transaction Draft
```

### Review Screen
User dapat:
* Edit merchant
* Edit amount
* Edit category

## Exit Criteria
Receipt dapat menjadi transaksi.

# Phase 6 — Email Ingestion
Estimasi:
Week 10–11

## Objective
Otomatisasi transaksi bank.

## Features
### Gmail Integration
* Connect Gmail

### Email Parser
MVP:
```text
1 Bank
```
saja terlebih dahulu.

### Candidate Transaction
User dapat:
* Approve
* Reject

### Duplicate Detection
Versi sederhana.

## Exit Criteria
Email transaksi dapat menghasilkan transaksi baru.

# Phase 7 — Export & Spreadsheet
Estimasi:
Week 12

## Objective
Integrasi dengan workflow keluarga.

## Features
### Export
* CSV
* Excel

### Google Sheets Sync
* Push transaction
* Push asset data

## Exit Criteria
Data dapat dibaca melalui spreadsheet.

# Phase 8 — Admin Dashboard
Estimasi:
Week 13

## Objective
Monitoring sistem.

## Features
### Admin Web
* Users
* Families
* Transactions

### Audit Logs
* Create
* Update
* Delete

### Sync Monitoring
* Pending Jobs
* Failed Jobs

## Exit Criteria
Admin dapat memonitor sistem.

# Phase 9 — Family Beta
Estimasi:
30 Hari

## Objective
Validasi penggunaan nyata.

## Participants
* Kamu
* Ayah
* Ibu

## Goals
Mengumpulkan:
* Bug
* Missing Features
* UX Issues

## Metrics
### Adoption
Target:
```text
>3 users
```

### Transactions
Target:
```text
>90% transaksi tercatat
```

### Sync
Target:
```text
>95% success rate
```

### OCR
Target:
```text
>80% accuracy
```

## Exit Criteria
WorthFlow digunakan secara nyata.

# Phase 10 — Public Portfolio Release
Estimasi:
Setelah Beta Stabil

## Deliverables
### Documentation
* Architecture
* ERD
* ADR
* API Design

### Engineering
* CI/CD
* Tests
* Deployment

### Portfolio
* README lengkap
* Screenshots
* Architecture diagrams
* Demo video

# Future Roadmap
Tidak termasuk MVP.

## Version 2
### Financial Insights
* Spending Trends
* Savings Rate
* Budget Tracking

### AI Insights
* Spending Analysis
* Recommendation Engine

### OCR Improvement
* Multi Receipt Support
* Invoice Support

## Version 3
### Wealth Management
* Investment Tracking
* Portfolio Analysis
* Asset Allocation

### Advanced Analytics
* Forecasting
* Cash Flow Projection
* Retirement Planning

# Definition of MVP Completion
WorthFlow MVP dianggap selesai apabila:
* ✅ Mobile App berjalan
* ✅ Backend berjalan
* ✅ Offline First berjalan
* ✅ Asset Tracking berjalan
* ✅ OCR berjalan
* ✅ Email Parser berjalan
* ✅ Google Sheets Sync berjalan
* ✅ Admin Dashboard berjalan
* ✅ Digunakan keluarga minimal 30 hari
* ✅ Seluruh dokumentasi engineering tersedia