# Environments

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi Environment Management untuk seluruh ekosistem WorthFlow.

Environment digunakan untuk:

- Memisahkan proses development, testing, dan production.
- Mengurangi risiko deployment.
- Menjaga keamanan credential.
- Mendukung CI/CD.
- Memastikan konfigurasi aplikasi konsisten di seluruh platform.

Dokumen ini menjadi acuan untuk:

- Flutter Mobile
- Flutter Web
- FastAPI Backend
- GitHub Actions
- Vercel
- Koyeb
- Supabase

---

# 2. Environment Overview

WorthFlow menggunakan tiga environment utama.

```
Development
        │
        ▼
Staging
        │
        ▼
Production
```

Masing-masing environment memiliki:

- Database sendiri
- Storage sendiri
- API Endpoint sendiri
- Secret sendiri
- Build Configuration sendiri

---

# 3. Environment Matrix

| Component | Development | Staging | Production |
|------------|------------|----------|------------|
| Mobile | Debug | Beta | Release |
| Web | localhost | Preview | Production |
| Backend | Localhost | Koyeb Staging | Koyeb Production |
| Database | Supabase Dev | Supabase Staging | Supabase Production |
| Storage | receipt-dev | receipt-stage | receipt-prod |
| Auth | Dev Project | Stage Project | Production Project |

---

# 4. Development Environment

Tujuan:

Digunakan untuk pengembangan fitur sehari-hari.

Configuration:

APP_ENV

```
development
```

API

```
http://localhost:8000/api/v1
```

Flutter

```
Debug Mode
```

Database

```
Supabase Development
```

Storage

```
receipt-dev
```

OCR

```
Chandra OCR
```

Gemini

```
Optional
```

Logging

```
Verbose
```

---

# 5. Staging Environment

Tujuan

Digunakan sebelum aplikasi dirilis ke keluarga.

Environment

```
staging
```

API

```
https://worthflow-api-stage.koyeb.app/api/v1
```

Flutter

```
Profile Build
```

Database

```
Supabase Staging
```

Storage

```
receipt-stage
```

Logging

```
Info
Warning
Error
```

Digunakan untuk:

- UAT
- Regression Testing
- Beta Testing

---

# 6. Production Environment

Environment

```
production
```

API

```
https://worthflow-api.koyeb.app/api/v1
```

Flutter

```
Release
```

Database

```
Supabase Production
```

Storage

```
receipt-prod
```

Logging

```
Warning
Error
```

Monitoring aktif.

Backup aktif.

HTTPS wajib.

---

# 7. Flutter Flavors

WorthFlow menggunakan Flutter Flavor.

```
lib/

main_dev.dart

main_stage.dart

main_prod.dart
```

Flavor

Development

↓

Staging

↓

Production

Setiap flavor memiliki konfigurasi endpoint sendiri.

---

# 8. Backend Configuration

Backend menggunakan file konfigurasi berdasarkan environment.

```
.env.development

.env.staging

.env.production
```

Configuration meliputi:

- Database
- JWT
- Supabase
- OCR
- Gemini
- Logging

---

# 9. Environment Variables

Contoh variable.

```
APP_ENV

DATABASE_URL

SUPABASE_URL

SUPABASE_ANON_KEY

SUPABASE_SERVICE_ROLE_KEY

GEMINI_API_KEY

JWT_SECRET

LOG_LEVEL

API_PORT

SYNC_INTERVAL
```

Seluruh variable dibaca saat startup aplikasi.

---

# 10. Secret Management

Secret **tidak boleh**:

- Hardcoded
- Disimpan di Git
- Dicantumkan pada README

Secret hanya disimpan pada:

GitHub Secrets

↓

Koyeb Environment Variables

↓

Vercel Environment Variables

↓

Supabase Dashboard

---

# 11. Database Environment

Setiap environment memiliki project Supabase terpisah.

Development

worthflow-dev

↓

Staging

worthflow-stage

↓

Production

worthflow-prod

Migration dilakukan menggunakan SQL Migration.

Tidak ada sharing database antar environment.

---

# 12. Storage Environment

Bucket dipisahkan.

Development

receipt-dev

↓

Staging

receipt-stage

↓

Production

receipt-prod

Semua bucket bersifat private.

---

# 13. API Endpoint Configuration

Development

```
http://localhost:8000
```

Staging

```
https://worthflow-api-stage.koyeb.app
```

Production

```
https://worthflow-api.koyeb.app
```

Frontend tidak boleh melakukan hardcode endpoint.

Endpoint berasal dari Environment Configuration.

---

# 14. Logging Configuration

Development

- Debug
- Info
- Warning
- Error

Staging

- Info
- Warning
- Error

Production

- Warning
- Error

Data sensitif tidak boleh muncul pada seluruh log.

---

# 15. Feature Flag

Fitur eksperimental hanya aktif pada:

Development

atau

Staging

Contoh.

```
AI Insight

Budget Prediction

Investment Module

Fraud Detection
```

---

# 16. Build Configuration

Flutter

Development

```
flutter run
```

Staging

```
flutter build apk --flavor staging
```

Production

```
flutter build appbundle --release
```

Backend

Development

```
uvicorn app.main:app --reload
```

Production

Docker Container

↓

Koyeb

---

# 17. Deployment Pipeline

Developer

↓

Git Push

↓

GitHub Actions

↓

Lint

↓

Unit Test

↓

Build

↓

Deploy

↓

Health Check

↓

Done

---

# 18. Environment Validation Checklist

Development

✓ Debug Enabled

✓ Local API

✓ Mock Data

✓ Hot Reload

---

Staging

✓ Build Success

✓ Migration Success

✓ API Connected

✓ OCR Working

✓ Email Sync Working

---

Production

✓ HTTPS

✓ Secret Loaded

✓ Database Connected

✓ Monitoring Enabled

✓ Backup Enabled

✓ Health Check Passed

---

# 19. Future Environment

Roadmap.

Development

↓

QA

↓

Staging

↓

Production

↓

Disaster Recovery

↓

Multi Region

---

# 20. Summary

WorthFlow menerapkan strategi multi-environment untuk memisahkan proses pengembangan, pengujian, dan penggunaan sehari-hari.

Setiap environment memiliki database, storage, endpoint API, secret, dan konfigurasi yang terisolasi sehingga deployment menjadi lebih aman, mudah dipelihara, dan siap dikembangkan seiring bertambahnya kompleksitas aplikasi.

Strategi ini juga memastikan proses CI/CD dapat berjalan secara konsisten tanpa memengaruhi data produksi yang digunakan oleh anggota keluarga.