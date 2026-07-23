# ADR-006: Use Riverpod for State Management

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow merupakan aplikasi Flutter yang memiliki arsitektur cukup kompleks.

Aplikasi harus menangani:

- Authentication
- Family Workspace
- Offline Database
- Sync Queue
- Background Synchronization
- OCR Pipeline
- REST API
- Analytics
- Theme Management

Selain itu aplikasi harus:

- Mudah diuji (Testable)
- Mudah dikembangkan
- Mendukung Dependency Injection
- Tidak bergantung pada BuildContext
- Cocok untuk Clean Architecture

State management menjadi fondasi utama karena hampir seluruh fitur bergantung padanya.

---

# Decision

WorthFlow menggunakan **Riverpod** sebagai state management framework utama.

Riverpod digunakan untuk mengelola:

- Global Application State
- Authentication State
- Family State
- Transaction State
- Budget State
- Sync Status
- Theme
- Settings
- Dependency Injection

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Compile-Time Safety

Riverpod memanfaatkan type system Dart.

Kesalahan dependency dapat diketahui saat proses compile, bukan ketika aplikasi dijalankan.

Hal ini meningkatkan stabilitas aplikasi.

---

## No BuildContext Dependency

Provider dapat diakses tanpa bergantung pada `BuildContext`.

Contoh.

```
Repository

↓

Riverpod Provider

↓

Business Logic

↓

UI
```

Arsitektur menjadi lebih bersih dan fleksibel.

---

## Excellent Testability

Provider dapat dengan mudah dioverride saat testing.

Hal ini mempermudah:

- Unit Test
- Widget Test
- Integration Test

tanpa memerlukan konfigurasi yang rumit.

---

## Dependency Injection

Riverpod juga berfungsi sebagai dependency injection container.

Contoh dependency yang dikelola:

- Dio Client
- Repository
- Local Database
- API Service
- Sync Engine
- Authentication Service

Hal ini mengurangi kebutuhan framework DI tambahan.

---

## Scalable Architecture

Riverpod cocok untuk aplikasi kecil maupun besar.

WorthFlow diperkirakan akan berkembang dengan fitur seperti:

- Shared Budget
- Investment Tracking
- AI Insights
- Push Notification

Riverpod tetap dapat menangani pertumbuhan tersebut tanpa perubahan arsitektur besar.

---

## Strong Flutter Ecosystem

Riverpod dikembangkan oleh komunitas Flutter yang aktif dan memiliki dokumentasi yang baik.

Integrasinya dengan:

- Flutter Hooks
- AsyncValue
- Code Generation

mendukung pengembangan aplikasi modern.

---

# Alternatives Considered

## Provider

### Pros

- Mudah dipelajari.
- Resmi direkomendasikan Flutter pada awal perkembangan.
- Ringan.

### Cons

- Bergantung pada BuildContext.
- Dependency Injection terbatas.
- Kurang nyaman untuk aplikasi besar.
- Sulit mengelola dependency kompleks.

Decision:

Not Selected.

---

## Bloc

### Pros

- Sangat terstruktur.
- Cocok untuk enterprise.
- Komunitas besar.
- Banyak contoh implementasi.

### Cons

- Boilerplate cukup banyak.
- Kurva belajar lebih tinggi.
- Pengembangan fitur sederhana menjadi lebih lambat.
- Kurang fleksibel untuk solo developer.

Decision:

Not Selected.

---

## GetX

### Pros

- Sangat sederhana.
- Cepat digunakan.
- Banyak fitur bawaan.

### Cons

- Pendekatan terlalu opinionated.
- Menggabungkan banyak tanggung jawab dalam satu framework.
- Sulit dipisahkan pada Clean Architecture.
- Tidak sejalan dengan arsitektur modular WorthFlow.

Decision:

Not Selected.

---

## MobX

### Pros

- Reactive Programming.
- Code Generation.

### Cons

- Bergantung pada generated code.
- Ekosistem lebih kecil.
- Tidak sepopuler Riverpod pada proyek Flutter modern.

Decision:

Not Selected.

---

# Consequences

## Positive

- Compile-time safety.
- Dependency Injection bawaan.
- Sangat mudah diuji.
- Tidak bergantung pada BuildContext.
- Cocok untuk Clean Architecture.
- Boilerplate lebih sedikit dibanding Bloc.
- Mudah dipelihara dalam jangka panjang.

---

## Negative

- Memerlukan pemahaman konsep Provider.
- Pola AsyncValue perlu dipelajari.
- Dokumentasi cukup luas sehingga membutuhkan waktu adaptasi.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Client Architecture |
| 07-offline-first-design.md | Repository Pattern |
| 08-sync-engine.md | Sync State |
| 10-ocr-pipeline.md | OCR State |
| 25-test-strategy.md | Widget Testing |
| 26-test-cases.md | Provider Testing |
| 30-coding-standards.md | Flutter Coding Standards |
| 31-design-system.md | UI Architecture |
| 32-dependency-management.md | Flutter Dependencies |
| 34-developer-onboarding.md | Development Setup |

---

# Risks

Risiko utama.

- Perubahan API pada versi mayor Riverpod.
- Developer baru belum familiar dengan pola Riverpod.
- Penggunaan provider yang tidak terstruktur dapat menyebabkan kompleksitas.

Mitigasi.

- Menggunakan Flutter Riverpod Stable.
- Menetapkan standar penamaan provider.
- Mendokumentasikan pola penggunaan pada Coding Standards.
- Menambahkan contoh implementasi pada repository.

---

# Implementation Notes

Struktur state management.

```
Presentation

↓

ConsumerWidget

↓

Riverpod Provider

↓

Repository

↓

Local Database

↓

REST API
```

Contoh provider.

```
authProvider

familyProvider

transactionProvider

budgetProvider

assetProvider

syncProvider

analyticsProvider

settingsProvider

themeProvider
```

Repository menjadi satu-satunya lapisan yang berkomunikasi dengan database maupun API.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Riverpod tidak lagi memenuhi kebutuhan aplikasi.
- Flutter merekomendasikan pendekatan baru yang lebih baik.
- Dibutuhkan pola state management yang lebih sesuai untuk skala aplikasi.

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

- https://riverpod.dev
- https://docs.flutter.dev
- https://pub.dev/packages/flutter_riverpod

---

# Decision Summary

WorthFlow menggunakan **Riverpod** sebagai framework state management utama karena memberikan compile-time safety, dependency injection bawaan, kemudahan pengujian, serta arsitektur yang sangat sesuai dengan pendekatan Clean Architecture dan Offline-First.

Dibandingkan Provider, Bloc, GetX, maupun MobX, Riverpod memberikan keseimbangan terbaik antara kesederhanaan, skalabilitas, dan maintainability. Keputusan ini mendukung pengembangan aplikasi lintas platform yang tetap mudah dipelihara meskipun fitur dan kompleksitas WorthFlow terus berkembang.