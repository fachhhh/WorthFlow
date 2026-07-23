# Design System

Version: 1.0

---

# 1. Purpose

Dokumen ini mendefinisikan Design System WorthFlow.

Tujuan utama:

- Menjaga konsistensi antarmuka.
- Mempermudah pengembangan UI.
- Mempercepat proses desain.
- Menjadi acuan implementasi Flutter.
- Menjamin pengalaman pengguna yang konsisten.

Design System digunakan oleh:

- UI/UX Designer
- Frontend Developer
- Product Owner

---

# 2. Design Principles

WorthFlow dibangun berdasarkan lima prinsip utama.

## Clarity

Informasi keuangan harus mudah dipahami.

Setiap angka memiliki hirarki visual yang jelas.

---

## Simplicity

Kurangi elemen yang tidak diperlukan.

Fokus pada data penting.

---

## Trust

Aplikasi harus memberikan rasa aman seperti aplikasi perbankan.

- warna stabil
- tipografi jelas
- feedback konsisten

---

## Accessibility

Semua komponen harus mudah digunakan.

- ukuran sentuh minimum
- kontras tinggi
- mendukung screen reader

---

## Consistency

Semua halaman menggunakan pola yang sama.

---

# 3. Design Language

WorthFlow menggunakan gaya.

Modern Financial Dashboard

Karakteristik.

- Clean
- Minimal
- Rounded Corner
- Soft Shadow
- High Readability
- Spacious Layout

---

# 4. Color System

## Primary

Brand utama.

```
Primary 500

#2563EB
```

Digunakan untuk.

- Button
- Active State
- Link
- Progress

---

## Success

```
#16A34A
```

Income

Berhasil

Approve

---

## Error

```
#DC2626
```

Expense negatif

Error

Delete

---

## Warning

```
#F59E0B
```

Budget hampir habis

Pending

---

## Info

```
#0EA5E9
```

Informasi

Sync

Notification

---

## Neutral

```
Gray 50

Gray 100

Gray 200

Gray 300

Gray 500

Gray 700

Gray 900
```

---

# 5. Dark Mode

WorthFlow mendukung Dark Mode.

Prinsip.

- Hindari hitam murni.
- Gunakan surface gelap.
- Pertahankan kontras.

---

# 6. Typography

Font.

```
Inter
```

Fallback.

```
Roboto
```

Hierarki.

| Style | Size |
|---------|------|
| Display | 40 |
| H1 | 32 |
| H2 | 28 |
| H3 | 24 |
| H4 | 20 |
| Body Large | 18 |
| Body | 16 |
| Body Small | 14 |
| Caption | 12 |

---

# 7. Spacing System

Menggunakan skala 8-point grid.

```
4

8

12

16

24

32

40

48

64
```

Tidak menggunakan nilai acak.

---

# 8. Border Radius

Standar.

| Component | Radius |
|-----------|---------|
| Button | 12 |
| Card | 16 |
| Dialog | 20 |
| Bottom Sheet | 24 |
| Chip | 999 |

---

# 9. Elevation

| Level | Usage |
|---------|------|
| 0 | Background |
| 1 | Card |
| 2 | Floating Button |
| 3 | Dialog |
| 4 | Modal |

Gunakan shadow secara minimal.

---

# 10. Iconography

Menggunakan.

Material Symbols Rounded.

Kategori.

- Dashboard
- Transaction
- Budget
- Asset
- Receipt
- Email
- Settings

Ukuran standar.

24 px.

---

# 11. Grid System

Mobile.

4-column.

Tablet.

8-column.

Web.

12-column.

---

# 12. Layout

Safe Area selalu digunakan.

Padding horizontal.

16 px.

Section spacing.

24 px.

---

# 13. Buttons

Primary Button

- Filled
- Primary Color

Secondary Button

- Outlined

Tertiary Button

- Text

Danger Button

- Error Color

Disabled Button

- Gray

Loading Button

- Spinner

---

# 14. Form Components

Komponen.

- TextField
- Number Field
- Currency Field
- Dropdown
- Date Picker
- Checkbox
- Radio
- Switch

Seluruh field memiliki.

Label

Helper Text

Validation

Error State

---

# 15. Navigation

Mobile.

Bottom Navigation.

Menu.

- Dashboard
- Transactions
- Assets
- Budget
- Settings

Web.

Sidebar Navigation.

---

# 16. Cards

Jenis.

Transaction Card

Receipt Card

Asset Card

Budget Card

Analytics Card

Semua card menggunakan pola visual yang konsisten.

---

# 17. Charts

Jenis.

- Line Chart
- Bar Chart
- Pie Chart
- Budget Progress
- Cash Flow

Prinsip.

Gunakan warna seminimal mungkin.

Fokus pada data.

---

# 18. Empty States

Setiap halaman wajib memiliki Empty State.

Contoh.

Belum ada transaksi.

↓

Tampilkan ilustrasi.

↓

CTA.

"Tambah Transaksi"

---

# 19. Loading States

Gunakan.

Skeleton Loading.

Bukan spinner penuh.

Kecuali.

OCR

Email Sync

---

# 20. Feedback

Komponen.

Snackbar

Toast

Dialog

Confirmation

Success Message

Semua aksi penting memberikan feedback.

---

# 21. Motion

Animasi.

Pendek.

Natural.

Durasi.

150–300 ms.

Hindari animasi berlebihan.

---

# 22. Accessibility

Minimal memenuhi WCAG 2.1 AA.

Checklist.

✓ Kontras warna.

✓ Focus Indicator.

✓ Screen Reader.

✓ Dynamic Font Size.

✓ Touch Target ≥48dp.

---

# 23. Responsive Design

Breakpoints.

| Device | Width |
|----------|-------|
| Mobile | <600 |
| Tablet | 600–1024 |
| Desktop | >1024 |

Layout menyesuaikan ukuran layar.

---

# 24. Component Library

Komponen dasar.

- AppBar
- Bottom Navigation
- Navigation Rail
- Drawer
- Button
- TextField
- Card
- Dialog
- Bottom Sheet
- Snackbar
- Chip
- Avatar
- Badge
- Progress Indicator
- Search Bar
- Filter Chip
- Floating Action Button

Semua komponen berasal dari Design System dan tidak dibuat secara ad hoc.

---

# 25. Design Tokens

Seluruh nilai visual diimplementasikan sebagai Design Tokens.

Contoh.

Color.

```
color.primary
```

Spacing.

```
spacing.md
```

Radius.

```
radius.lg
```

Typography.

```
typography.bodyLarge
```

Dengan pendekatan ini, perubahan tema dapat dilakukan secara terpusat.

---

# 26. Figma Structure

Struktur file Figma.

```
📁 Foundations
    Colors
    Typography
    Icons
    Spacing

📁 Components
    Buttons
    Cards
    Inputs
    Navigation
    Charts

📁 Templates
    Mobile
    Web

📁 Screens
    Authentication
    Dashboard
    Transaction
    Asset
    Budget
    Settings
```

---

# 27. Flutter Mapping

Setiap komponen Figma memiliki implementasi Flutter.

Contoh.

```
PrimaryButton
```

↓

```
AppPrimaryButton
```

```
BudgetCard
```

↓

```
BudgetCardWidget
```

```
TransactionCard
```

↓

```
TransactionCardWidget
```

Hal ini menjaga konsistensi antara desain dan implementasi.

---

# 28. Future Improvements

Roadmap.

- Interactive Component Documentation
- Storybook untuk Flutter
- Automated Design Token Export
- Figma Variables
- Material 3 Dynamic Color
- Motion Specification
- Design QA Checklist

---

# 29. Summary

Design System WorthFlow mendefinisikan bahasa visual aplikasi mulai dari prinsip desain, warna, tipografi, layout, komponen, hingga implementasi Flutter melalui Design Tokens.

Dengan pendekatan ini, proses desain dan pengembangan dapat berjalan lebih konsisten, efisien, dan mudah dipelihara seiring bertambahnya fitur maupun anggota tim.