# 🚀 Auto Commit GitHub (Daily Random 1-10)

Automasi commit harian ke GitHub secara acak antara 1 hingga 10 commit setiap hari menggunakan **GitHub Actions** (berjalan otomatis di cloud tanpa perlu menyalakan komputer) dan didukung script lokal Python & PowerShell.

---

## ✨ Fitur Utama
- ⏰ **100% Otomatis di Cloud**: Berjalan setiap hari menggunakan GitHub Actions cron schedule.
- 🎲 **Commit Acak 1-10**: Setiap eksekusi memilih angka random antara 1 sampai 10 commit.
- 📝 **Pesan Commit Bervariasi**: Menggunakan format Conventional Commits yang rapi (`chore`, `docs`, `refactor`, `perf`, `feat`, dll).
- 📊 **Log Aktivitas Rapi**: Mencatat tanggal & waktu (WIB / UTC+7) pada file [`ACTIVITY.md`](ACTIVITY.md).
- 🟢 **Mendukung GitHub Green Contribution**: Dikonfigurasi dengan nama & email GitHub akun Anda (`Isronursalaam@gmail.com`).
- 🔘 **Manual Trigger**: Bisa dijalankan kapan saja langsung dari tab **Actions** di GitHub dengan sekali klik (*Run workflow*).

---

## 🛠️ Langkah Menghubungkan ke GitHub

### 1. Buat Repository Baru di GitHub
1. Buka browser dan login ke akun GitHub Anda: [https://github.com/new](https://github.com/new)
2. Masukkan **Repository name**: `AutoCommit` (atau nama lain yang Anda inginkan).
3. Pilih **Public** (agar kontribusi langsung terlihat hijau di profil) atau **Private** (jika Private, pastikan mengaktifkan *"Private contributions"* di setting profil GitHub Anda).
4. **JANGAN** centang *Add a README file*, *.gitignore*, atau *license* (karena sudah kita buat secara lokal).
5. Klik **Create repository**.

### 2. Hubungkan & Push Repository Lokal ke GitHub
Jalankan perintah berikut di terminal / PowerShell folder ini:

```powershell
git remote add origin https://github.com/Isronursalaam/AutoCommit.git
git branch -M main
git push -u origin main
```

*(Jika diminta login oleh GitHub, selesaikan otentikasi melalui browser / Git Credential Manager)*.

### 3. Aktifkan Izin Tulis untuk GitHub Actions (PENTING! ⚠️)
Agar GitHub Actions dapat melakukan push commit otomatis setiap hari:
1. Buka repository Anda di GitHub: `https://github.com/Isronursalaam/AutoCommit`
2. Klik tab **Settings** (di menu atas repository).
3. Di sidebar sebelah kiri, klik **Actions** -> **General**.
4. Scroll ke bawah ke bagian **Workflow permissions**.
5. Pilih opsi **"Read and write permissions"**.
6. Centang juga **"Allow GitHub Actions to create and approve pull requests"** (opsional).
7. Klik tombol **Save**.

---

## ⚙️ Cara Kerja GitHub Actions

File konfigurasi berada di [`.github/workflows/auto-commit.yml`](.github/workflows/auto-commit.yml):
- **Jadwal Otomatis**: Berjalan otomatis setiap hari pada jam `02:00 UTC` (pukul **09:00 WIB**).
- **Manual Trigger**:
  1. Masuk ke tab **Actions** di repository GitHub Anda.
  2. Klik workflow **Daily Auto Commit** di menu kiri.
  3. Klik tombol dropdown **Run workflow** -> klik tombol hijau **Run workflow**.

---

## 💻 Menjalankan Secara Lokal (Opsional)

Jika ingin menjalankan secara manual dari komputer lokal Anda:

### Menggunakan Python:
```bash
# Hanya membuat commit lokal
python auto_commit.py

# Membuat commit lokal dan langsung push ke GitHub
python auto_commit.py --push
```

### Menggunakan PowerShell:
```powershell
# Jalankan dan push ke GitHub
.\auto_commit.ps1 -Push
```

---

## 📌 Catatan untuk Grafik Kontribusi Hijau (Contribution Graph)
Agar titik hijau muncul di profil GitHub Anda:
1. Email commit harus sama dengan email yang terdaftar di akun GitHub (`Isronursalaam@gmail.com`).
2. Commit harus berada di branch default (`main`).
3. Jika repository disetel ke **Private**, pastikan Anda mengaktifkan opsi *"Private contributions"* di pengaturan profil GitHub:
   - Buka profil GitHub Anda -> klik dropdown di kanan atas grafik kontribusi -> centang **"Private contributions"**.
