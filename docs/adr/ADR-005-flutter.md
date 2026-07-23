# ADR-005: Use Flutter as the Primary Client Framework

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow membutuhkan aplikasi yang dapat berjalan pada beberapa platform dengan pengalaman pengguna yang konsisten.

Target platform MVP meliputi:

- Android
- Web

Sedangkan pada fase berikutnya akan mendukung:

- iOS
- Desktop (Windows/macOS/Linux)

Aplikasi juga memiliki kebutuhan khusus seperti:

- Offline First
- OCR Capture
- Camera Integration
- Local Database
- Background Synchronization
- Responsive Layout
- Shared Design System

Karena proyek dikembangkan oleh satu developer, penggunaan beberapa codebase terpisah akan meningkatkan biaya pengembangan dan maintenance.

---

# Decision

WorthFlow menggunakan **Flutter** sebagai framework utama untuk seluruh aplikasi client.

Flutter akan digunakan untuk membangun:

- Android Application
- Flutter Web

Pada fase berikutnya, codebase yang sama dapat digunakan untuk:

- iOS
- Windows
- macOS
- Linux

Seluruh platform menggunakan satu Design System dan satu Business Logic.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Single Codebase

Satu codebase dapat digunakan untuk berbagai platform.

```
Flutter

├── Android
├── Web
├── iOS (Future)
├── Windows (Future)
├── macOS (Future)
└── Linux (Future)
```

Hal ini mengurangi duplikasi kode dan mempercepat pengembangan.

---

## Offline-First Support

Flutter memiliki ekosistem yang sangat baik untuk aplikasi offline.

WorthFlow menggunakan:

- Drift SQLite
- Riverpod
- Dio
- Connectivity Plus

Seluruh library tersebut terintegrasi dengan baik.

---

## High Performance

Flutter melakukan rendering menggunakan engine sendiri sehingga tampilan lebih konsisten antar platform.

Animasi, scrolling, dan transisi lebih stabil dibanding pendekatan berbasis WebView.

---

## Consistent UI

WorthFlow memiliki Design System sendiri.

Flutter memungkinkan seluruh komponen UI dibuat secara konsisten tanpa bergantung pada komponen native masing-masing platform.

---

## Strong Ecosystem

Flutter memiliki package yang mendukung kebutuhan WorthFlow.

Contoh:

- Camera
- Image Picker
- Local Notification
- SQLite
- HTTP Client
- Secure Storage
- Charts
- QR Code
- PDF

---

## Developer Productivity

Flutter mendukung:

- Hot Reload
- Hot Restart
- Widget Inspector
- DevTools

Hal ini mempercepat proses pengembangan dan debugging.

---

# Alternatives Considered

## Native Android (Kotlin)

### Pros

- Performa maksimal.
- Integrasi penuh dengan Android.
- Dukungan fitur terbaru Android lebih cepat.

### Cons

- Harus membuat aplikasi lain untuk Web dan iOS.
- Biaya maintenance meningkat.
- Tidak sesuai untuk single developer.

Decision:

Not Selected.

---

## Native iOS (Swift)

### Pros

- Performa tinggi.
- Integrasi penuh dengan iOS.

### Cons

- Tidak dapat digunakan untuk Android.
- Membutuhkan codebase terpisah.

Decision:

Not Selected.

---

## React Native

### Pros

- JavaScript ecosystem besar.
- Banyak developer.
- Fast Refresh.

### Cons

- Bergantung pada native bridge.
- Konsistensi UI antar platform lebih sulit.
- Offline architecture membutuhkan konfigurasi tambahan.
- Flutter memberikan pengalaman rendering yang lebih konsisten.

Decision:

Not Selected.

---

## Progressive Web App (PWA)

### Pros

- Mudah diakses.
- Tidak memerlukan instalasi.

### Cons

- Akses hardware lebih terbatas.
- Offline capability tidak sekuat aplikasi native.
- Integrasi kamera dan penyimpanan lokal lebih terbatas.

Decision:

Not Selected.

---

# Consequences

## Positive

- Satu codebase.
- UI konsisten.
- Pengembangan lebih cepat.
- Maintenance lebih mudah.
- Sangat cocok untuk Offline First.
- Mudah diperluas ke platform lain.
- Design System dapat digunakan kembali.

---

## Negative

- Ukuran aplikasi lebih besar dibanding native.
- Bergantung pada Flutter SDK.
- Beberapa fitur platform memerlukan plugin tambahan.
- Upgrade Flutter perlu diuji secara berkala.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Client Architecture |
| 07-offline-first-design.md | Local Data Flow |
| 08-sync-engine.md | Repository Layer |
| 10-ocr-pipeline.md | Camera Integration |
| 14-api-spec.md | API Client |
| 25-test-strategy.md | Flutter Testing |
| 30-coding-standards.md | Flutter Coding Standards |
| 31-design-system.md | UI Components |
| 32-dependency-management.md | Flutter Dependencies |
| 34-developer-onboarding.md | Development Environment |

---

# Risks

Risiko utama.

- Perubahan besar pada Flutter SDK.
- Ketergantungan pada package pihak ketiga.
- Plugin tertentu mungkin tidak mendukung semua platform.

Mitigasi.

- Menggunakan Flutter Stable Channel.
- Mengunci versi dependency melalui pubspec.lock.
- Memilih package yang aktif dipelihara komunitas.
- Melakukan regression testing sebelum upgrade Flutter.

---

# Implementation Notes

Arsitektur aplikasi Flutter.

```
Presentation Layer

↓

Riverpod Providers

↓

Repository Layer

↓

Local Database (Drift)

↓

Sync Engine

↓

REST API

↓

FastAPI
```

Seluruh Business Logic berada pada Repository dan Service Layer.

UI hanya bertugas menampilkan data dan menerima interaksi pengguna.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Flutter tidak lagi memenuhi kebutuhan performa.
- Dukungan Web atau Mobile mengalami penurunan signifikan.
- Dibutuhkan platform yang tidak didukung Flutter.
- Framework lain memberikan keuntungan yang jauh lebih besar.

Review dilakukan setiap major release.

---

# References

Internal Documentation

- 06-system-architecture.md
- 07-offline-first-design.md
- 08-sync-engine.md
- 25-test-strategy.md
- 30-coding-standards.md
- 31-design-system.md
- 32-dependency-management.md
- 34-developer-onboarding.md
- 36-architecture-decision-records.md

External References

- https://flutter.dev
- https://docs.flutter.dev
- https://pub.dev

---

# Decision Summary

WorthFlow menggunakan **Flutter** sebagai framework utama untuk seluruh aplikasi client karena memungkinkan pengembangan lintas platform dengan satu codebase, memberikan performa tinggi, mendukung arsitektur Offline First, serta menyediakan ekosistem yang matang untuk kebutuhan aplikasi keuangan modern.

Dibandingkan Native Android, Native iOS, React Native, maupun Progressive Web App, Flutter memberikan keseimbangan terbaik antara produktivitas pengembangan, konsistensi antarmuka, kemudahan pemeliharaan, dan skalabilitas jangka panjang. Keputusan ini juga sejalan dengan visi WorthFlow sebagai aplikasi keuangan keluarga yang dapat berkembang ke berbagai platform tanpa harus membangun ulang aplikasi dari awal.