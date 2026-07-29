# WorthFlow

WorthFlow adalah platform manajemen keuangan keluarga untuk mengumpulkan, mengorganisasi, dan menganalisis aktivitas keuangan dalam satu sistem terpadu.

Proyek ini mengutamakan pendekatan **mobile-first**, **offline-first**, kemudahan penggunaan, dan privasi data.

## Technology Stack

- Flutter untuk aplikasi Android dan Web
- FastAPI untuk backend API
- Supabase PostgreSQL untuk database
- Docker Compose untuk development environment

## Repository Structure

```text
WorthFlow/
├── backend/             # FastAPI backend
├── docs/                # Project documentation and ADR
├── worthflow/           # Flutter application
├── docker-compose.yml
└── README.md
```

## Requirements

- Git
- Flutter SDK
- Python 3.12+
- Docker Desktop
- Supabase development project

## Environment Setup

Salin konfigurasi contoh backend:

```powershell
Copy-Item backend\.env.example backend\.env
```

Kemudian isi `backend\.env` menggunakan konfigurasi Supabase Development Anda.

Jangan commit file `.env` atau credential lainnya ke Git.

## Run with Docker

Dari root repository:

```powershell
docker compose up --build
```

Backend tersedia di:

```text
http://localhost:8000
```

Health check:

```text
GET http://localhost:8000/admin/health
```

Untuk menghentikan environment:

```powershell
docker compose down
```

## Run Flutter

```powershell
cd worthflow
flutter pub get
flutter run
```

## Documentation

Dokumentasi arsitektur, product requirements, environment, deployment, dan Architecture Decision Records tersedia di folder [`docs`](docs).

## Project Status

Phase 01 — Project Bootstrap