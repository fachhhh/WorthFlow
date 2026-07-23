# ADR-004: Do Not Use Kubernetes for the MVP

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow saat ini berada pada tahap **Minimum Viable Product (MVP)**.

Target utama fase ini adalah:

- Memvalidasi kebutuhan pengguna.
- Mengembangkan fitur inti secepat mungkin.
- Menjaga biaya operasional tetap rendah.
- Menyederhanakan proses deployment.
- Mengurangi beban maintenance.

Tim pengembang juga masih sangat kecil (single developer), sehingga seluruh infrastruktur harus mudah dipahami dan dikelola.

---

# Decision

WorthFlow **tidak menggunakan Kubernetes** pada fase MVP.

Sebagai gantinya, deployment dilakukan menggunakan kombinasi berikut:

```
Flutter Web

↓

Vercel


FastAPI

↓

Docker

↓

Koyeb


Database

↓

Supabase
```

Seluruh service dikemas menggunakan Docker sehingga tetap mudah dipindahkan ke platform lain apabila diperlukan.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Simplicity

Prioritas utama MVP adalah membangun fitur, bukan mengelola infrastruktur.

Menambahkan Kubernetes akan meningkatkan kompleksitas tanpa memberikan manfaat yang sebanding pada tahap awal.

---

## Small Team

WorthFlow dikembangkan oleh satu developer.

Kubernetes umumnya lebih cocok digunakan ketika:

- Tim DevOps tersedia.
- Banyak microservice.
- Banyak developer bekerja secara paralel.

Kondisi tersebut belum berlaku untuk WorthFlow.

---

## Low Operational Cost

Platform seperti Koyeb, Vercel, dan Supabase menyediakan deployment yang sederhana dengan biaya rendah bahkan gratis pada tahap awal.

Tidak diperlukan cluster Kubernetes sendiri.

---

## Fast Deployment

Deployment dapat dilakukan hanya dengan:

```
Git Push

↓

GitHub Actions

↓

Deploy

↓

Production
```

Tanpa konfigurasi cluster, ingress, service mesh, maupun autoscaler.

---

## Docker Compatibility

Seluruh service tetap dikemas menggunakan Docker.

Dengan demikian, apabila di masa depan diperlukan Kubernetes, proses migrasi akan jauh lebih mudah.

---

# Alternatives Considered

## Kubernetes

### Pros

- High Availability
- Horizontal Scaling
- Self Healing
- Rolling Update
- Enterprise Standard

### Cons

- Kurva belajar tinggi.
- Konfigurasi kompleks.
- Membutuhkan monitoring tambahan.
- Membutuhkan cluster.
- Tidak sebanding dengan kebutuhan MVP.

Decision:

Not Selected.

---

## Docker Compose

### Pros

- Sangat sederhana.
- Cocok untuk development.
- Mudah dipelajari.

### Cons

- Tidak ideal untuk deployment production skala besar.

Decision:

Selected untuk Local Development.

---

## Managed Platform (Koyeb)

### Pros

- Deployment cepat.
- HTTPS otomatis.
- Auto Restart.
- Integrasi GitHub.
- Biaya rendah.

### Cons

- Bergantung pada penyedia layanan.
- Fitur scaling lebih terbatas dibanding Kubernetes.

Decision:

Selected.

---

# Consequences

## Positive

- Infrastruktur lebih sederhana.
- Deployment lebih cepat.
- Maintenance lebih ringan.
- Fokus pada pengembangan fitur.
- Biaya operasional rendah.
- Onboarding developer lebih mudah.

---

## Negative

- Tidak memiliki fitur autoscaling tingkat lanjut.
- Tidak memiliki rolling deployment kompleks.
- Tidak memiliki self-healing cluster.
- Skalabilitas horizontal lebih terbatas.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Deployment Architecture |
| 19-environments.md | Runtime Environment |
| 20-cicd.md | CI/CD Pipeline |
| 21-deployment-guide.md | Deployment Process |
| 22-monitoring.md | Infrastructure Monitoring |
| 23-backup-recovery.md | Disaster Recovery |
| 24-release-process.md | Release Workflow |
| 36-architecture-decision-records.md | ADR Index |

---

# Risks

Risiko utama.

- Pertumbuhan pengguna lebih cepat dari perkiraan.
- Kebutuhan scaling meningkat.
- Satu instance backend menjadi bottleneck.

Mitigasi.

- Menggunakan Docker sejak awal.
- Mendesain aplikasi agar stateless.
- Memisahkan service berdasarkan tanggung jawab.
- Menyiapkan migrasi ke Kubernetes apabila diperlukan.

---

# Migration Strategy

Apabila kebutuhan meningkat, migrasi dapat dilakukan secara bertahap.

```
Current

Docker

↓

Koyeb

↓

Supabase


Future

Docker

↓

Kubernetes

↓

Managed PostgreSQL

↓

Object Storage
```

Karena aplikasi telah menggunakan Docker, perpindahan ke Kubernetes tidak memerlukan perubahan besar pada kode aplikasi.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Jumlah pengguna meningkat secara signifikan.
- Dibutuhkan High Availability multi-region.
- Dibutuhkan autoscaling yang lebih kompleks.
- Infrastruktur berkembang menjadi banyak microservice.
- Tim engineering bertambah dan membutuhkan orkestrasi container.

Review dilakukan sebelum setiap major release atau ketika terdapat perubahan signifikan pada kebutuhan operasional.

---

# References

Internal Documentation

- 06-system-architecture.md
- 19-environments.md
- 20-cicd.md
- 21-deployment-guide.md
- 22-monitoring.md
- 24-release-process.md
- 36-architecture-decision-records.md

External References

- Kubernetes Documentation
- Docker Documentation
- Koyeb Documentation
- Vercel Documentation

---

# Decision Summary

WorthFlow **tidak menggunakan Kubernetes pada fase MVP** karena kompleksitas operasionalnya tidak sebanding dengan kebutuhan proyek saat ini. Sebagai gantinya, aplikasi menggunakan kombinasi **Docker**, **Koyeb**, **Vercel**, dan **Supabase** yang lebih sederhana, hemat biaya, dan memungkinkan deployment yang cepat.

Keputusan ini menjaga fokus tim pada pengembangan fitur dan validasi produk, sekaligus tetap mempertahankan jalur migrasi yang jelas menuju Kubernetes di masa depan melalui penggunaan container Docker yang konsisten.