# ADR-009: Use JWT Authentication with Refresh Tokens

Status: Accepted

Date: 2026-07-23

Decision Makers:
- Project Owner
- Lead Developer

---

# Context

WorthFlow merupakan aplikasi keuangan keluarga yang menyimpan data sensitif seperti:

- Profil pengguna
- Data keluarga
- Riwayat transaksi
- Budget
- Aset
- OCR Receipt
- Audit Log

Seluruh komunikasi antara aplikasi Flutter dan backend FastAPI harus dilakukan melalui mekanisme autentikasi yang aman, scalable, dan tidak bergantung pada session server.

Selain itu, aplikasi mendukung arsitektur Offline-First sehingga proses autentikasi harus tetap memberikan pengalaman pengguna yang baik tanpa harus melakukan login berulang setiap kali aplikasi dibuka.

---

# Decision

WorthFlow menggunakan **JSON Web Token (JWT)** sebagai Access Token dan **Refresh Token** untuk mempertahankan sesi login.

Arsitektur autentikasi.

```
User Login

↓

FastAPI

↓

Verify Credentials

↓

Generate

• Access Token
• Refresh Token

↓

Flutter Secure Storage

↓

Authenticated API Requests
```

Access Token digunakan pada setiap request API.

Refresh Token digunakan untuk memperoleh Access Token baru ketika masa berlaku Access Token telah habis.

---

# Decision Drivers

Keputusan ini didasarkan pada beberapa pertimbangan utama.

## Stateless Authentication

JWT memungkinkan backend tetap stateless.

Server tidak perlu menyimpan session untuk setiap pengguna.

Hal ini membuat backend lebih sederhana dan lebih mudah diskalakan.

---

## Better Mobile Experience

Pengguna tidak perlu login setiap kali membuka aplikasi.

Refresh Token memungkinkan sesi tetap aktif tanpa mengorbankan keamanan.

---

## Offline-First Compatibility

Data lokal tetap dapat diakses ketika perangkat offline.

Autentikasi hanya diperlukan ketika:

- Login
- Sinkronisasi
- Mengakses endpoint yang memerlukan koneksi internet

---

## Security

JWT ditandatangani menggunakan secret key backend.

Refresh Token memiliki masa berlaku lebih panjang dan dapat dicabut apabila diperlukan.

Access Token memiliki masa berlaku pendek untuk mengurangi risiko penyalahgunaan.

---

## Backend Independence

Seluruh logika autentikasi berada di FastAPI.

WorthFlow tidak bergantung pada layanan autentikasi pihak ketiga sehingga lebih mudah dipindahkan ke infrastruktur lain di masa depan.

---

# Alternatives Considered

## Session-Based Authentication

### Pros

- Mudah dipahami.
- Banyak digunakan pada aplikasi web tradisional.

### Cons

- Membutuhkan penyimpanan session di server.
- Kurang cocok untuk REST API.
- Skalabilitas lebih rendah.
- Tidak ideal untuk aplikasi mobile.

Decision:

Not Selected.

---

## Supabase Auth

### Pros

- Mudah digunakan.
- Integrasi langsung dengan Supabase.
- Mendukung OAuth.

### Cons

- Menambah ketergantungan terhadap Supabase.
- Logika autentikasi berada di luar backend.
- Kurang fleksibel apabila ingin berpindah penyedia database.

Decision:

Not Selected.

---

## Firebase Authentication

### Pros

- Stabil.
- Mendukung banyak metode login.
- Dokumentasi lengkap.

### Cons

- Vendor lock-in.
- Tidak sejalan dengan backend FastAPI.
- Menambah kompleksitas integrasi.

Decision:

Not Selected.

---

## JWT + Refresh Token

### Pros

- Stateless.
- Scalable.
- Cocok untuk REST API.
- Sangat umum digunakan.
- Mudah dipadukan dengan FastAPI.

### Cons

- Membutuhkan mekanisme refresh token.
- Memerlukan penyimpanan token yang aman.

Decision:

Selected.

---

# Consequences

## Positive

- Backend tetap stateless.
- Mudah diskalakan.
- Login lebih nyaman bagi pengguna.
- Tidak bergantung pada vendor autentikasi.
- Sangat cocok untuk Flutter dan REST API.
- Integrasi sederhana dengan FastAPI.

---

## Negative

- Membutuhkan implementasi refresh token.
- Token harus disimpan secara aman.
- Perlu mekanisme pencabutan token pada kondisi tertentu.

---

# Impact

Keputusan ini memengaruhi dokumen berikut.

| Document | Impact |
|----------|--------|
| 06-system-architecture.md | Authentication Architecture |
| 14-api-spec.md | Authorization Header |
| 15-auth-flow.md | Login Flow |
| 16-security-design.md | API Security |
| 17-threat-model.md | Authentication Threats |
| 18-audit-log.md | Login Audit |
| 25-test-strategy.md | Authentication Testing |
| 27-api-testing.md | API Authorization |
| 29-security-testing.md | Security Validation |

---

# Risks

Risiko utama.

- Token dicuri.
- Refresh Token bocor.
- Access Token digunakan setelah logout.
- Replay Attack.

Mitigasi.

- HTTPS untuk seluruh komunikasi.
- Access Token berumur pendek (misalnya 15 menit).
- Refresh Token memiliki masa berlaku lebih panjang dan dapat dicabut.
- Penyimpanan token menggunakan Flutter Secure Storage.
- Logout menghapus seluruh token dari perangkat.

---

# Implementation Notes

Flow autentikasi.

```
Flutter

↓

POST /auth/login

↓

FastAPI

↓

Verify Password

↓

Generate JWT

↓

Generate Refresh Token

↓

Flutter Secure Storage

↓

Authorization

Bearer <Access Token>
```

Ketika Access Token kedaluwarsa.

```
Flutter

↓

POST /auth/refresh

↓

FastAPI

↓

Validate Refresh Token

↓

Generate New Access Token

↓

Continue Request
```

Logout.

```
Delete Local Token

↓

Invalidate Refresh Token

↓

Return to Login Screen
```

---

# Token Lifetime

| Token | Lifetime |
|---------|----------|
| Access Token | 15 Minutes |
| Refresh Token | 30 Days |

Nilai tersebut dapat diubah melalui konfigurasi environment.

---

# Review Criteria

ADR ini perlu ditinjau ulang apabila:

- Dibutuhkan Single Sign-On (SSO).
- Dibutuhkan OAuth Provider tambahan.
- Arsitektur backend berubah secara signifikan.
- Muncul kebutuhan autentikasi berbasis passkey atau passwordless.

Review dilakukan setiap major release.

---

# References

Internal Documentation

- 06-system-architecture.md
- 14-api-spec.md
- 15-auth-flow.md
- 16-security-design.md
- 17-threat-model.md
- 18-audit-log.md
- 27-api-testing.md
- 29-security-testing.md
- 36-architecture-decision-records.md

External References

- RFC 7519 — JSON Web Token (JWT)
- OWASP Authentication Cheat Sheet
- FastAPI Security Documentation
- flutter_secure_storage Documentation

---

# Decision Summary

WorthFlow menggunakan **JWT Authentication dengan Refresh Token** sebagai mekanisme autentikasi utama karena memberikan keseimbangan terbaik antara keamanan, skalabilitas, dan pengalaman pengguna. Pendekatan ini memungkinkan backend FastAPI tetap stateless, mendukung arsitektur REST API, serta tidak bergantung pada penyedia autentikasi pihak ketiga.

Dibandingkan Session-Based Authentication, Supabase Auth, maupun Firebase Authentication, pendekatan ini memberikan kontrol penuh terhadap proses autentikasi dan memudahkan migrasi infrastruktur di masa depan. Keputusan ini juga selaras dengan arsitektur Offline-First yang menjadi fondasi utama WorthFlow.