# Authentication & Authorization Flow

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan mekanisme Authentication dan Authorization pada WorthFlow.

Dokumen ini menjadi acuan untuk:

- Mobile Application
- Web Dashboard
- Backend API
- Supabase Authentication
- Row Level Security (RLS)

Dokumen ini melengkapi:

- 12-schema-design.md
- 14-api-spec.md
- 16-security-design.md

---

# 2. Authentication Principles

WorthFlow menggunakan prinsip berikut:

- Authentication dikelola oleh Supabase Auth.
- Authorization dikelola oleh Backend + PostgreSQL RLS.
- JWT digunakan sebagai Access Token.
- Refresh Token digunakan untuk memperbarui sesi.
- Backend tidak menyimpan password pengguna.

---

# 3. Authentication Architecture

                    User
                      │
             Email & Password
                      │
                      ▼
              Supabase Auth
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
   Access Token               Refresh Token
        │
        ▼
      Mobile App / Web
        │
        ▼
   Authorization Header
        │
        ▼
      FastAPI Backend
        │
        ▼
 JWT Verification (Supabase)
        │
        ▼
 Family Validation
        │
        ▼
 PostgreSQL (RLS)

---

# 4. Identity Model

WorthFlow memiliki tiga konsep identitas.

## Auth User

Akun autentikasi yang dikelola Supabase.

Contoh:

- email
- password
- session
- refresh token

---

## User

Representasi akun pada database aplikasi.

Menyimpan informasi seperti:

- email
- status
- auth_user_id

---

## Family Member

Representasi anggota keluarga.

Contoh:

- Ayah
- Ibu
- Anak
- Adik SD

FamilyMember dapat memiliki ataupun tidak memiliki akun login.

---

# 5. Login Flow

User

↓

Input Email

↓

Input Password

↓

Supabase Auth

↓

Credential Validation

↓

Generate JWT

↓

Generate Refresh Token

↓

Return Session

↓

Store Securely

↓

Access API

---

# 6. Session Flow

Login

↓

Receive JWT

↓

Store Token

↓

API Request

↓

JWT Validation

↓

Authorized

↓

Response

---

# 7. Refresh Token Flow

JWT Expired

↓

Client Detects

↓

Send Refresh Token

↓

Supabase

↓

Generate New JWT

↓

Continue Session

---

# 8. Logout Flow

User Logout

↓

Invalidate Session

↓

Delete Local Token

↓

Delete Refresh Token

↓

Redirect Login

---

# 9. Authorization Flow

Incoming Request

↓

JWT Validation

↓

Extract User ID

↓

Find User

↓

Find Family Member

↓

Find Family

↓

Apply Permission

↓

Execute Request

---

# 10. Family Access Model

Semua data berada dalam konteks Family.

Contoh:

Family A

- Ayah
- Ibu
- Anak

↓

Transactions

↓

Assets

↓

Reports

User dari Family lain tidak dapat mengakses data tersebut.

---

# 11. Permission Model

## Owner

Hak akses penuh.

Dapat:

- Mengubah Family
- Menghapus Asset
- Mengelola Member
- Mengelola Email
- Mengakses Audit

---

## Parent

Dapat:

- CRUD Transaction
- CRUD Asset
- Review OCR
- Review Email Draft
- Melihat Dashboard

---

## Child

Dapat:

- Input Transaction
- Melihat Dashboard
- Upload Receipt

Tidak dapat:

- Menghapus Family
- Mengelola Member

---

## Viewer (Future)

Hanya dapat membaca data.

---

# 12. JWT Claims

JWT minimal memiliki informasi berikut.

sub

Auth User ID

family_id

Current Family

member_id

Family Member

role

Permission

exp

Expired Time

iat

Issued At

---

# 13. API Authentication

Semua endpoint privat menggunakan:

Authorization

Bearer <JWT>

Header wajib.

Jika tidak tersedia:

401 Unauthorized

---

# 14. Authorization Rules

Transaction

↓

Harus berasal dari Family yang sama.

---

Asset

↓

Harus dimiliki Family yang sama.

---

Category

↓

Harus milik Family yang sama.

---

Draft

↓

Harus berasal dari Family yang sama.

---

Audit Log

↓

Hanya Owner.

---

# 15. Row Level Security

WorthFlow memanfaatkan PostgreSQL RLS.

Contoh aturan:

User hanya dapat membaca data dengan:

family_id

yang sesuai dengan Family tempat dirinya menjadi anggota.

Semua query otomatis dibatasi oleh policy RLS.

---

# 16. Secure Token Storage

## Mobile

Menggunakan:

- flutter_secure_storage

Jangan menyimpan token pada:

- SharedPreferences

---

## Web

Menggunakan:

- Secure HttpOnly Cookie (future)
- Memory Storage (SPA)

Hindari penggunaan Local Storage untuk token sensitif.

---

# 17. Session Expiration

Access Token

- Short-lived
- ±1 jam

Refresh Token

- Long-lived
- Dapat diperbarui

Jika Refresh Token tidak valid:

↓

User wajib Login kembali.

---

# 18. Failed Authentication Flow

Request

↓

JWT Invalid

↓

401 Unauthorized

↓

Client Refresh Token

↓

Success

↓

Retry Request

atau

↓

Login Screen

---

# 19. Multi Device Support

Satu akun dapat login pada:

- Android
- iPhone
- Web

Setiap device memiliki session masing-masing.

Logout pada satu device tidak otomatis menghapus session device lain (future configurable).

---

# 20. Future Authentication

WorthFlow dirancang agar mendukung:

- Google Login
- Apple Login
- Magic Link
- Passkey (WebAuthn)
- Two Factor Authentication (2FA)
- Biometric Login
- Device Trust

---

# 21. Authentication Lifecycle

User

↓

Login

↓

Supabase Auth

↓

JWT

↓

Backend

↓

Family Validation

↓

Row Level Security

↓

API Response

↓

Refresh Token

↓

Continue Session

↓

Logout

---

# 22. Security Considerations

Seluruh proses autentikasi mengikuti prinsip berikut:

- Password tidak pernah disimpan oleh aplikasi.
- Seluruh komunikasi menggunakan HTTPS.
- JWT diverifikasi pada setiap request.
- Refresh Token tidak dikirim pada setiap request API.
- Authorization selalu divalidasi terhadap Family aktif.
- Semua aktivitas sensitif dicatat pada Audit Log.

---

# 23. Summary

WorthFlow menggunakan arsitektur Authentication berbasis Supabase Auth dan Authorization berbasis Family Context.

Model ini memberikan beberapa keuntungan:

- Tidak perlu mengelola password sendiri.
- Mendukung multi-device.
- Mudah diintegrasikan dengan Mobile dan Web.
- Aman melalui JWT dan Refresh Token.
- Data terisolasi menggunakan Family Context dan Row Level Security.
- Siap dikembangkan dengan OAuth, Passkey, dan 2FA di masa depan.