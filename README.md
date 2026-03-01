# 🖥️ Flynn Taxonomy — Parallel Computing Classification

> Tugas Mata Kuliah **Komputasi Paralel dan Sistem Terdistribusi**  
> Pertemuan Ke-2: Klasifikasi SISD, SIMD, MISD, dan MIMD

---

## 👤 Identitas

| | |
|---|---|
| **Nama** | `[ISI NAMA KAMU]` |
| **NIM** | `[ISI NIM KAMU]` |
| **Kelas** | `[ISI KELAS KAMU]` |
| **Dosen** | `[ISI NAMA DOSEN]` |

---

## 📌 Deskripsi

Repository ini berisi implementasi empat klasifikasi arsitektur komputer paralel berdasarkan **Flynn Taxonomy** yang diperkenalkan oleh Michael Flynn pada tahun 1966. Setiap klasifikasi diimplementasikan menggunakan Python dengan output yang menampilkan cara kerja masing-masing arsitektur secara langkah demi langkah.

---

## 🗂️ Struktur File

```
📦 repository
 ┣ 📄 sisd.py       → Single Instruction, Single Data
 ┣ 📄 simd.py       → Single Instruction, Multiple Data
 ┣ 📄 misd.py       → Multiple Instruction, Single Data
 ┣ 📄 mimd.py       → Multiple Instruction, Multiple Data
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📚 Penjelasan Klasifikasi

### 🔹 SISD — Single Instruction, Single Data
Satu prosesor menjalankan satu instruksi pada satu data dalam satu waktu. Ini adalah model komputasi serial klasik — tidak ada paralelisme sama sekali.

**Contoh nyata:** Komputer single-core lama, loop biasa di Python.

---

### 🔹 SIMD — Single Instruction, Multiple Data
Satu instruksi yang sama dijalankan secara bersamaan pada banyak data sekaligus. Semua elemen diproses dalam satu waktu dengan operasi yang identik.

**Contoh nyata:** GPU, operasi NumPy, pemrosesan gambar.

---

### 🔹 MISD — Multiple Instruction, Single Data
Banyak instruksi berbeda dijalankan pada data yang sama secara bersamaan. Arsitektur ini jarang digunakan di dunia nyata — umumnya untuk sistem toleransi kesalahan.

**Contoh nyata:** Sistem flight control pesawat ulang-alik NASA (redundancy check).

---

### 🔹 MIMD — Multiple Instruction, Multiple Data
Banyak prosesor menjalankan instruksi berbeda pada data yang berbeda secara bersamaan. Ini adalah arsitektur paralel yang paling umum digunakan saat ini.

**Contoh nyata:** Multi-core CPU, server cluster, sistem terdistribusi.

---

## 📊 Perbandingan

| Tipe | Instruksi | Data | Contoh |
|------|-----------|------|--------|
| **SISD** | Tunggal | Tunggal | Loop serial biasa |
| **SIMD** | Tunggal | Banyak | NumPy, GPU |
| **MISD** | Banyak | Tunggal | Sistem fault-tolerant |
| **MIMD** | Banyak | Banyak | Multiprocessing Python |

---

## ⚙️ Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/[USERNAME]/[NAMA-REPO].git
cd [NAMA-REPO]
```

### 2. Buat dan aktifkan virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan masing-masing file
```bash
python sisd.py
python simd.py
python misd.py
python mimd.py
```

---

## 🛠️ Library yang Digunakan

| Library | Jenis | Kegunaan |
|---------|-------|----------|
| `numpy` | Install via pip | Operasi array/matriks untuk SIMD |
| `threading` | Bawaan Python | Simulasi proses paralel untuk SIMD |
| `multiprocessing` | Bawaan Python | Proses paralel nyata untuk MIMD |
| `time` | Bawaan Python | Simulasi waktu proses |

---

## 📝 Catatan

- File `mimd.py` **wajib** dijalankan dengan blok `if __name__ == "__main__":` agar `multiprocessing` bekerja dengan benar, terutama di Windows.
- Output pada `simd.py` mungkin tampil **tidak berurutan** — ini adalah hal yang normal dan justru membuktikan bahwa proses berjalan secara paralel.
