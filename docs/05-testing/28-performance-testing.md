# Performance Testing

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan strategi Performance Testing pada WorthFlow.

Tujuan utama:

- Mengukur performa sistem.
- Mengidentifikasi bottleneck.
- Menentukan baseline performa.
- Memastikan pengalaman pengguna tetap responsif.
- Memvalidasi target SLA sebelum release.

Dokumen ini melengkapi:

- 22-monitoring.md
- 25-test-strategy.md
- 27-api-testing.md

---

# 2. Performance Goals

WorthFlow dirancang sebagai aplikasi keluarga.

Target utama.

- Startup cepat
- Dashboard responsif
- Sinkronisasi stabil
- OCR cukup cepat
- Email Parser berjalan di background
- Penggunaan memori efisien

---

# 3. Performance Scope

Seluruh komponen diuji.

Frontend

- Flutter Mobile
- Flutter Web

Backend

- FastAPI

Database

- PostgreSQL

Storage

- Supabase Storage

Automation

- OCR Worker
- Email Parser
- Sync Engine

---

# 4. Performance Metrics

Metrik utama.

| Metric | Description |
|----------|------------|
| Response Time | Lama request diproses |
| Latency | Waktu komunikasi |
| Throughput | Request per detik |
| CPU Usage | Penggunaan CPU |
| Memory Usage | Penggunaan RAM |
| Database Query Time | Lama query |
| Error Rate | Persentase error |
| Startup Time | Waktu membuka aplikasi |

---

# 5. SLA Target

| Component | Target |
|------------|---------|
| App Startup | <2 detik |
| Login | <300 ms |
| Dashboard | <500 ms |
| Transaction List | <500 ms |
| Asset List | <500 ms |
| Budget | <500 ms |
| Upload Receipt | <2 detik |
| OCR | <5 detik |
| Email Sync | <10 detik |
| Offline Sync | <30 detik |

---

# 6. Mobile Performance

Yang diuji.

Startup

↓

Navigation

↓

Scrolling

↓

Animation

↓

Memory Usage

↓

Battery Usage

Target.

Scrolling tetap 60 FPS.

---

# 7. Web Performance

Yang diuji.

- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Time To Interactive (TTI)
- Cumulative Layout Shift (CLS)

Target mengikuti rekomendasi Google Core Web Vitals.

---

# 8. Backend Performance

Pengujian.

- API Response Time
- Concurrent Request
- Query Time
- Background Job
- Connection Pool

Target.

Error Rate

<1%

---

# 9. Database Performance

Pengujian.

- Query Duration
- Index Usage
- Slow Query
- Connection Pool
- Migration Time

Semua query utama menggunakan index yang sesuai.

---

# 10. OCR Performance

Pipeline.

Upload

↓

OCR

↓

AI Parsing

↓

Draft

↓

Database

Target.

OCR selesai.

<5 detik

---

# 11. Email Parser Performance

Pipeline.

Connect

↓

Download

↓

Parse

↓

Draft

↓

Complete

Target.

<10 detik.

---

# 12. Offline Sync Performance

Pipeline.

SQLite

↓

Queue

↓

Sync

↓

Server

↓

Dashboard

Target.

Sinkronisasi selesai.

<30 detik.

---

# 13. Load Testing

Beban simulasi.

| Scenario | Concurrent User |
|----------|-----------------|
| Development | 5 |
| Staging | 20 |
| Production (Target) | 50 |

Walaupun aplikasi digunakan keluarga, pengujian dilakukan untuk memastikan skalabilitas.

---

# 14. Stress Testing

Skenario.

Normal Load

↓

High Load

↓

Peak Load

↓

Failure

↓

Recovery

Yang diamati.

- Error Rate
- Response Time
- Recovery Time

---

# 15. Endurance Testing

Simulasi.

Backend berjalan.

24 Jam

Yang diamati.

- Memory Leak
- CPU Spike
- Connection Leak

---

# 16. Database Benchmark

Target.

| Query | Maximum |
|---------|----------|
| Dashboard | 300 ms |
| Transaction | 200 ms |
| Asset | 200 ms |
| Budget | 200 ms |
| Analytics | 500 ms |

---

# 17. Frontend Benchmark

Target.

| Operation | Target |
|-----------|---------|
| App Startup | <2 s |
| Login Screen | <1 s |
| Dashboard Render | <1 s |
| Open Transaction | <500 ms |
| Open Asset | <500 ms |

---

# 18. Resource Utilization

Backend.

CPU

<70%

Memory

<512 MB

Worker.

Memory

<256 MB

Flutter.

Memory stabil tanpa peningkatan terus-menerus (memory leak).

---

# 19. Testing Tools

| Layer | Tool |
|---------|------|
| API Benchmark | k6 |
| Backend Profiling | py-spy |
| Flutter | DevTools |
| Database | EXPLAIN ANALYZE |
| Web | Lighthouse |
| CI | GitHub Actions |

---

# 20. Automation

Performance Test dijalankan.

Sebelum Release

↓

Benchmark

↓

Generate Report

↓

Compare Baseline

↓

Approve Release

---

# 21. Reporting

Laporan minimal memuat.

- Average Response Time
- P95 Response Time
- Maximum Response Time
- Error Rate
- Throughput
- CPU
- Memory

Grafik benchmark disimpan pada folder:

```
reports/performance/
```

---

# 22. Acceptance Criteria

Release dapat dilakukan apabila.

✓ SLA tercapai.

✓ Error Rate <1%.

✓ Tidak ada Memory Leak.

✓ OCR memenuhi target.

✓ Dashboard memenuhi target.

---

# 23. Future Improvements

Roadmap.

- Distributed Load Testing
- Automated Benchmark Dashboard
- Continuous Performance Testing
- AI-assisted Performance Analysis
- Multi-region Benchmark

---

# 24. Summary

WorthFlow menerapkan Performance Testing pada seluruh lapisan sistem mulai dari aplikasi Flutter, backend FastAPI, database PostgreSQL, OCR Pipeline, Email Parser, hingga mekanisme Offline Sync.

Seluruh hasil benchmark dibandingkan dengan baseline performa dan target SLA yang telah ditentukan sehingga setiap rilis dapat dipastikan tetap responsif, stabil, dan memberikan pengalaman pengguna yang konsisten.