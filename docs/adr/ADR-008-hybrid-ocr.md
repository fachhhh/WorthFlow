# ADR-008: Adopt a Hybrid OCR Pipeline for Receipt Processing

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

Salah satu fitur utama WorthFlow adalah membantu pengguna mencatat transaksi hanya dengan memotret struk belanja.

Pipeline OCR harus mampu:

- Mengekstrak teks dari gambar.
- Mengidentifikasi merchant.
- Mengambil tanggal transaksi.
- Mengambil total pembayaran.
- Menghasilkan draft transaksi.
- Tetap dapat digunakan ketika tidak ada koneksi internet.

Selain akurasi, pipeline juga harus mempertimbangkan:

- Biaya operasional.
- Kecepatan pemrosesan.
- Konsistensi hasil.
- Privasi data pengguna.
- Kemampuan fallback ketika AI tidak tersedia.

---

# Decision

WorthFlow menggunakan **Hybrid OCR Pipeline**.

Pipeline terdiri dari beberapa tahap.

```
Receipt Image

↓

Image Preprocessing

↓

Tesseract OCR

↓

Rule-based Parsing
(Regex + Pattern Matching)

↓

AI Enhancement (Optional)

↓

Transaction Draft

↓

User Review

↓

Approved Transaction
```

AI bukan merupakan komponen wajib.

Apabila AI tidak tersedia, pipeline tetap dapat menghasilkan draft transaksi menggunakan OCR dan rule-based parsing.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Offline Capability

WorthFlow mengadopsi prinsip Offline-First.

Dengan menggunakan Tesseract OCR sebagai tahap utama, proses ekstraksi teks tetap dapat dilakukan tanpa koneksi internet.

---

## Cost Efficiency

Model AI Vision umumnya mengenakan biaya berdasarkan jumlah request atau token.

Menggunakan AI pada seluruh gambar akan meningkatkan biaya operasional secara signifikan.

Hybrid Pipeline hanya menggunakan AI apabila benar-benar diperlukan.

---

## Deterministic Parsing

Data seperti:

- Total
- Tanggal
- Pajak
- Nomor Invoice

sering kali memiliki pola yang dapat dikenali menggunakan Regular Expression.

Pendekatan rule-based memberikan hasil yang lebih konsisten dibanding selalu mengandalkan model AI.

---

## Privacy

OCR dilakukan terlebih dahulu di perangkat atau backend sendiri.

Data tidak selalu perlu dikirim ke layanan AI eksternal.

Hal ini mengurangi paparan data sensitif.

---

## Graceful Fallback

Apabila AI gagal atau tidak tersedia.

Pipeline tetap berjalan.

```
Receipt

↓

OCR

↓

Regex

↓

Draft

↓

Approve
```

Pengguna tetap dapat menggunakan aplikasi.

---

# Alternatives Considered

## AI-Only OCR

### Pros

- Akurasi tinggi.
- Dapat memahami konteks.
- Mampu menangani format yang beragam.

### Cons

- Membutuhkan internet.
- Biaya operasional tinggi.
- Bergantung pada layanan pihak ketiga.
- Hasil dapat berubah antar versi model.
- Tidak deterministic.

Decision:

Not Selected.

---

## OCR Only

### Pros

- Dapat berjalan offline.
- Gratis.
- Konsisten.
- Tidak bergantung pada AI.

### Cons

- Sulit memahami konteks.
- Merchant berbeda memiliki format berbeda.
- Akurasi lebih rendah pada struk kompleks.

Decision:

Not Selected.

---

## Manual Input

### Pros

- Sangat sederhana.
- Tidak membutuhkan OCR.

### Cons

- Pengguna harus mengetik seluruh transaksi.
- User experience buruk.
- Tidak sesuai dengan visi WorthFlow.

Decision:

Not Selected.

---

## Hybrid OCR

### Pros

- Offline tetap berfungsi.
- Biaya rendah.
- Akurasi tinggi.
- Memiliki fallback.
- Dapat berkembang seiring waktu.

### Cons

- Pipeline lebih kompleks.
- Membutuhkan beberapa tahap pemrosesan.

Decision:

Selected.

---

# Consequences

## Positive

- Tetap dapat digunakan tanpa internet.
- Mengurangi biaya AI.
- Pipeline lebih andal.
- AI hanya digunakan ketika diperlukan.
- Akurasi lebih baik dibanding OCR murni.
- Privasi pengguna lebih terjaga.
- Mudah menambahkan model AI baru di masa depan.

---

## Negative

- Implementasi lebih kompleks.
- Membutuhkan rule parser.
- Membutuhkan preprocessing gambar.
- Membutuhkan evaluasi akurasi setiap tahap.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | OCR Architecture |
| 07-offline-first-design.md | Offline OCR |
| 09-email-ingestion.md | Email Receipt Parsing |
| 10-ocr-pipeline.md | OCR Pipeline |
| 11-erd.md | OCR Draft Entity |
| 12-schema-design.md | OCR Draft Schema |
| 13-data-flow.md | Receipt Processing Flow |
| 28-performance-testing.md | OCR Benchmark |
| 29-security-testing.md | Receipt Data Protection |

---

# Risks

Risiko utama.

- OCR gagal membaca teks.
- Format struk tidak dikenal.
- Merchant baru memiliki layout berbeda.
- AI menghasilkan interpretasi yang salah.
- Kualitas gambar buruk.

Mitigasi.

- Image preprocessing.
- Regex berbasis pola.
- User review sebelum transaksi disimpan.
- Retry OCR.
- Manual editing.
- Menyimpan confidence score setiap hasil OCR.

---

# Implementation Notes

Pipeline implementasi.

```
Capture Receipt

↓

Crop & Enhance Image

↓

Tesseract OCR

↓

Extract Raw Text

↓

Regex Parser

↓

Identify

• Merchant
• Date
• Total
• Currency

↓

Confidence Check

↓

Confidence High

↓

Create Draft

↓

Confidence Low

↓

Gemini Enhancement (Optional)

↓

Updated Draft

↓

User Approval

↓

Transaction Saved
```

AI hanya dijalankan apabila confidence parser berada di bawah ambang batas yang telah ditentukan.

---

# Future Improvements

Pipeline dapat dikembangkan menjadi:

- Merchant Template Recognition
- Receipt Layout Classification
- Barcode Detection
- QRIS Detection
- Custom OCR Dictionary
- Local Machine Learning Model
- Multi-language OCR
- Line Item Extraction
- Automatic Expense Categorization

Seluruh peningkatan tersebut tetap mempertahankan prinsip Hybrid OCR.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Tersedia OCR engine yang lebih akurat.
- Model AI lokal menjadi cukup ringan untuk dijalankan di perangkat.
- Biaya AI berubah secara signifikan.
- Kebutuhan bisnis berubah sehingga memerlukan ekstraksi informasi yang lebih kompleks.

Review dilakukan setiap major release.

---

# References

Internal Documentation

- 06-system-architecture.md
- 07-offline-first-design.md
- 09-email-ingestion.md
- 10-ocr-pipeline.md
- 11-erd.md
- 12-schema-design.md
- 13-data-flow.md
- 28-performance-testing.md
- 29-security-testing.md
- 36-architecture-decision-records.md

External References

- Tesseract OCR Documentation
- Google ML Kit Documentation
- Google Gemini API Documentation
- OpenCV Documentation

---

# Decision Summary

WorthFlow mengadopsi **Hybrid OCR Pipeline** yang menggabungkan Tesseract OCR, rule-based parsing, dan AI enhancement sebagai komponen opsional. Pendekatan ini memberikan keseimbangan terbaik antara akurasi, biaya operasional, privasi, dan kemampuan bekerja secara offline.

Dibandingkan pendekatan AI-Only maupun OCR-Only, Hybrid OCR memungkinkan aplikasi tetap berfungsi tanpa koneksi internet, menghasilkan proses yang lebih deterministik, dan hanya memanfaatkan AI ketika benar-benar diperlukan. Keputusan ini sejalan dengan prinsip Offline-First serta tujuan WorthFlow untuk menyediakan pengalaman pencatatan transaksi yang cepat, andal, dan efisien.