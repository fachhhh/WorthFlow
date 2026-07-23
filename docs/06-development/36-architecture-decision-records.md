# Architecture Decision Records (ADR)

Version: 1.0

---

# 1. Purpose

Dokumen ini merupakan indeks seluruh keputusan arsitektur (Architecture Decision Records / ADR) pada proyek WorthFlow.

Tujuan utama:

- Mendokumentasikan alasan di balik setiap keputusan teknis.
- Menghindari hilangnya konteks saat proyek berkembang.
- Memudahkan onboarding developer baru.
- Menjadi referensi ketika melakukan evaluasi atau perubahan arsitektur.
- Menjelaskan trade-off dari setiap teknologi yang dipilih.

Setiap keputusan arsitektur penting harus memiliki ADR tersendiri.

---

# 2. What is an ADR?

Architecture Decision Record (ADR) adalah dokumen singkat yang menjelaskan:

- Masalah yang dihadapi.
- Alternatif yang dipertimbangkan.
- Keputusan yang dipilih.
- Alasan pemilihan.
- Konsekuensi jangka pendek dan jangka panjang.

ADR tidak bertujuan membuktikan bahwa suatu keputusan adalah yang terbaik, tetapi menjelaskan mengapa keputusan tersebut diambil pada saat itu.

---

# 3. ADR Lifecycle

```
Problem

↓

Research

↓

Evaluate Alternatives

↓

Decision

↓

Implementation

↓

Review

↓

Superseded (optional)
```

Keputusan dapat diperbarui apabila terdapat perubahan kebutuhan bisnis, teknologi, atau arsitektur.

---

# 4. ADR Status

Setiap ADR memiliki salah satu status berikut.

| Status | Description |
|----------|-------------|
| Proposed | Sedang didiskusikan |
| Accepted | Disetujui dan digunakan |
| Superseded | Digantikan ADR lain |
| Deprecated | Tidak lagi digunakan |
| Rejected | Ditolak |

---

# 5. ADR Template

Setiap ADR menggunakan format berikut.

```
# ADR-XXX

Title

Status

Context

Decision

Alternatives Considered

Consequences

References
```

---

# 6. ADR Index

| ADR | Status | Description |
|------|--------|-------------|
| ADR-001 | Accepted | Menggunakan FastAPI sebagai backend framework |
| ADR-002 | Accepted | Menggunakan Supabase PostgreSQL sebagai database |
| ADR-003 | Accepted | Mengadopsi arsitektur Offline First |
| ADR-004 | Accepted | Tidak menggunakan Kubernetes pada MVP |

ADR baru akan ditambahkan apabila terdapat keputusan arsitektur yang signifikan.

---

# 7. Engineering Decision Summary

Berikut adalah ringkasan keputusan teknis utama pada WorthFlow.

| Area | Decision | Reason |
|------|----------|--------|
| Mobile | Flutter | Satu codebase untuk Android, iOS, dan Web |
| Backend | FastAPI | Performa tinggi, type-safe, dokumentasi OpenAPI otomatis |
| Database | PostgreSQL (Supabase) | Managed service, RLS, free tier, mudah diintegrasikan |
| Local Storage | Drift (SQLite) | Mendukung Offline First dan sinkronisasi lokal |
| State Management | Riverpod | Compile-time safety, scalable, mudah diuji |
| Networking | Dio | Interceptor, timeout, retry, multipart upload |
| OCR | Tesseract OCR | Open source, berjalan offline, tanpa biaya API |
| AI Parsing | Gemini (Opsional) | Membantu parsing OCR tetapi bukan ketergantungan utama |
| Authentication | JWT + Refresh Token | Stateless dan umum digunakan |
| Deployment Backend | Koyeb | Gratis untuk MVP, deployment sederhana |
| Deployment Frontend | Vercel | Integrasi GitHub dan deployment cepat |
| CI/CD | GitHub Actions | Gratis untuk open source dan workflow fleksibel |
| Containerization | Docker | Konsisten di semua environment |
| License | Apache 2.0 | Perlindungan paten dan tetap ramah open source |

---

# 8. Major Trade-offs

## Flutter vs Native

Dipilih:

Flutter

Keuntungan.

- Satu codebase.
- Pengembangan lebih cepat.
- UI konsisten.

Konsekuensi.

- Ukuran aplikasi lebih besar.
- Bergantung pada Flutter SDK.

---

## FastAPI vs Django

Dipilih:

FastAPI

Keuntungan.

- Async.
- Performa tinggi.
- Dokumentasi otomatis.

Konsekuensi.

- Ekosistem lebih kecil dibanding Django.

---

## Supabase vs Firebase

Dipilih:

Supabase

Keuntungan.

- PostgreSQL.
- SQL.
- Row Level Security.
- Tidak terkunci pada NoSQL.

Konsekuensi.

- Ekosistem lebih kecil dibanding Firebase.

---

## Offline First vs Online Only

Dipilih:

Offline First.

Keuntungan.

- Tetap dapat digunakan tanpa internet.
- Cocok untuk kondisi jaringan tidak stabil.

Konsekuensi.

- Sinkronisasi menjadi lebih kompleks.

---

## Hybrid OCR vs AI-only OCR

Dipilih.

Hybrid OCR.

Pipeline.

```
Receipt

↓

Tesseract

↓

Rule-based Parsing

↓

Gemini (Optional)

↓

Transaction Draft
```

Keuntungan.

- Tetap berjalan tanpa AI.
- Biaya lebih rendah.
- Mudah melakukan fallback.

Konsekuensi.

- Pipeline lebih kompleks.

---

# 9. Future ADR Candidates

Beberapa keputusan yang kemungkinan memerlukan ADR di masa depan.

- Shared Budget
- Recurring Transaction Engine
- Push Notification Service
- Cloud Storage Provider
- AI Recommendation Engine
- End-to-End Encryption
- Event-driven Architecture
- CQRS
- GraphQL API

---

# 10. Review Process

ADR harus ditinjau kembali apabila.

- Ada perubahan arsitektur.
- Ada dependency utama yang diganti.
- Ada perubahan kebutuhan bisnis.
- Ada masalah performa atau keamanan yang signifikan.

Review dilakukan minimal setiap enam bulan atau sebelum major release.

---

# 11. Related Documents

- 06-system-architecture.md
- 11-erd.md
- 12-schema-design.md
- 14-api-spec.md
- 16-security-design.md
- docs/adr/

---

# 12. Summary

Architecture Decision Records (ADR) mendokumentasikan alasan di balik setiap keputusan arsitektur yang diambil pada WorthFlow.

Dengan adanya ADR, setiap perubahan teknologi dapat ditelusuri konteksnya, dipahami trade-off-nya, dan dievaluasi secara objektif tanpa kehilangan sejarah pengambilan keputusan. Dokumen ini berfungsi sebagai indeks utama yang menghubungkan seluruh ADR individual serta merangkum keputusan teknis penting yang membentuk arsitektur WorthFlow.