# ADR-010: Adopt a Managed Cloud Deployment Strategy

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow merupakan aplikasi Full Stack yang terdiri dari beberapa komponen.

- Flutter Web
- Flutter Mobile
- FastAPI Backend
- PostgreSQL Database
- Object Storage
- OCR Worker
- Background Sync

Pada fase MVP, deployment harus memenuhi beberapa tujuan utama.

- Sederhana untuk dikelola.
- Biaya operasional rendah.
- Deployment otomatis.
- Mudah dipindahkan ke provider lain.
- Mendukung pertumbuhan aplikasi.

Sebagai proyek yang dikembangkan oleh satu developer, kompleksitas infrastruktur harus dijaga seminimal mungkin.

---

# Decision

WorthFlow menggunakan **Managed Cloud Deployment Strategy**.

Setiap komponen dijalankan pada layanan yang paling sesuai dengan tanggung jawabnya.

```
Flutter Web

↓

Vercel


Flutter Mobile

↓

Google Play Store

↓

Apple App Store (Future)


FastAPI

↓

Docker Container

↓

Koyeb


Database

↓

Supabase PostgreSQL


Object Storage

↓

Supabase Storage


Source Code

↓

GitHub


CI/CD

↓

GitHub Actions
```

Deployment dilakukan secara otomatis melalui GitHub Actions.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Simplicity

Managed Platform mengurangi kebutuhan konfigurasi server.

Developer dapat fokus pada pengembangan fitur dibanding mengelola infrastruktur.

---

## Low Operational Cost

Seluruh platform menyediakan paket gratis atau biaya rendah yang cukup untuk kebutuhan MVP.

Hal ini membantu mengurangi biaya operasional pada tahap awal pengembangan.

---

## Automatic Deployment

Perubahan pada branch utama akan memicu pipeline CI/CD.

```
Git Push

↓

GitHub Actions

↓

Build

↓

Test

↓

Deploy
```

Deployment menjadi lebih konsisten dan mengurangi risiko kesalahan manual.

---

## Docker Portability

Backend dikemas menggunakan Docker.

Dengan demikian aplikasi dapat dipindahkan ke penyedia cloud lain tanpa perubahan besar.

---

## Scalability

Managed Platform memungkinkan peningkatan kapasitas secara bertahap.

Migrasi ke infrastruktur yang lebih kompleks dapat dilakukan apabila jumlah pengguna meningkat.

---

# Alternatives Considered

## Self-Hosted VPS

### Pros

- Kontrol penuh.
- Fleksibel.
- Biaya tetap.

### Cons

- Maintenance tinggi.
- Harus mengelola keamanan sendiri.
- Backup manual.
- Monitoring manual.

Decision:

Not Selected.

---

## Kubernetes Cluster

### Pros

- High Availability.
- Horizontal Scaling.
- Enterprise Standard.

### Cons

- Kompleks.
- Overkill untuk MVP.
- Membutuhkan DevOps.

Decision:

Not Selected.

---

## Managed Cloud Platform

### Pros

- Deployment cepat.
- Maintenance rendah.
- HTTPS otomatis.
- Auto restart.
- Integrasi GitHub.
- Monitoring dasar tersedia.

### Cons

- Bergantung pada layanan cloud.
- Opsi konfigurasi lebih terbatas.

Decision:

Selected.

---

# Consequences

## Positive

- Deployment sederhana.
- CI/CD otomatis.
- Maintenance rendah.
- Mudah dipelajari.
- Infrastruktur modular.
- Cocok untuk MVP.
- Mudah bermigrasi apabila diperlukan.

---

## Negative

- Ketergantungan pada managed service.
- Konfigurasi infrastruktur lebih terbatas.
- Beberapa fitur enterprise tidak tersedia.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 19-environments.md | Runtime Environment |
| 20-cicd.md | Deployment Pipeline |
| 21-deployment-guide.md | Production Deployment |
| 22-monitoring.md | Production Monitoring |
| 23-backup-recovery.md | Disaster Recovery |
| 24-release-process.md | Release Workflow |
| 27-api-testing.md | Production API Validation |
| 36-architecture-decision-records.md | ADR Index |

---

# Risks

Risiko utama.

- Downtime pada penyedia cloud.
- Perubahan harga layanan.
- Vendor lock-in.
- Batas penggunaan paket gratis.

Mitigasi.

- Menggunakan Docker untuk backend.
- Menyimpan backup database secara berkala.
- Memisahkan database, storage, dan backend.
- Mendokumentasikan proses migrasi ke provider lain.

---

# Implementation Notes

Deployment Architecture.

```
GitHub Repository

↓

GitHub Actions

↓

Build & Test

↓

Deploy Backend

↓

Koyeb

↓

FastAPI


Deploy Frontend

↓

Vercel

↓

Flutter Web


Database

↓

Supabase PostgreSQL


Object Storage

↓

Supabase Storage
```

Environment Variables.

```
Development

↓

Staging

↓

Production
```

Seluruh secret dikelola menggunakan Secret Manager pada GitHub Actions dan platform deployment masing-masing.

---

# Future Improvements

Apabila jumlah pengguna meningkat secara signifikan, infrastruktur dapat dikembangkan menjadi.

- Multi-region Deployment
- CDN
- Redis Cache
- Background Worker Cluster
- Load Balancer
- Dedicated Object Storage
- Kubernetes Orchestration

Seluruh peningkatan tersebut tetap mempertahankan arsitektur modular yang telah dibangun.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila.

- Infrastruktur tidak lagi mampu menangani beban aplikasi.
- Dibutuhkan High Availability multi-region.
- Biaya operasional meningkat secara signifikan.
- Tim engineering bertambah dan memerlukan orkestrasi container.

Review dilakukan sebelum setiap major release.

---

# References

Internal Documentation

- 19-environments.md
- 20-cicd.md
- 21-deployment-guide.md
- 22-monitoring.md
- 23-backup-recovery.md
- 24-release-process.md
- 36-architecture-decision-records.md

External References

- Docker Documentation
- GitHub Actions Documentation
- Vercel Documentation
- Koyeb Documentation
- Supabase Documentation

---

# Decision Summary

WorthFlow mengadopsi **Managed Cloud Deployment Strategy** dengan memanfaatkan **Vercel** untuk Flutter Web, **Docker + Koyeb** untuk FastAPI, **Supabase PostgreSQL** sebagai database, **Supabase Storage** untuk penyimpanan objek, serta **GitHub Actions** sebagai pipeline CI/CD.

Pendekatan ini memberikan keseimbangan terbaik antara kesederhanaan operasional, biaya, skalabilitas, dan kemudahan deployment. Dibandingkan pendekatan self-hosted maupun Kubernetes, strategi ini lebih sesuai dengan kebutuhan MVP, memungkinkan pengembangan yang cepat, sekaligus tetap menyediakan jalur migrasi yang jelas menuju infrastruktur yang lebih kompleks apabila WorthFlow berkembang di masa depan.