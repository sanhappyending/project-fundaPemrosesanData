# Project Fundamental Pemrosesan Data — ETL Pipeline

Proyek ETL (Extract, Transform, Load) sederhana untuk mengambil, memproses, dan menyimpan data produk fashion kompetitor menggunakan Python.

## 📌 Deskripsi Project

Project ini merupakan submission akhir dari kelas **Belajar Fundamental Pemrosesan Data**.

Pada project ini, dibangun sebuah ETL pipeline sederhana yang bertugas untuk:

* Mengambil data produk fashion dari website kompetitor
* Membersihkan dan mentransformasi data
* Menyimpan data hasil transformasi ke format yang siap digunakan

Studi kasus project berfokus pada perusahaan retail fashion yang ingin melakukan analisis kompetitor terhadap produk dari:

> Fashion Studio

Website sumber data:

https://fashion-studio.dicoding.dev

Seluruh data pada website bersifat fiktif dan hanya digunakan untuk kebutuhan pembelajaran dan submission.

---

## 🎯 Objectives

* Melakukan web scraping data produk fashion
* Membersihkan dan memproses data
* Membangun ETL pipeline sederhana
* Menyimpan data hasil transformasi
* Mengimplementasikan automasi pemrosesan data menggunakan Python

---

## ⚙️ ETL Process

### 1. Extract

Mengambil data produk fashion dari website kompetitor menggunakan teknik scraping.

### 2. Transform

Melakukan proses:

* cleaning data
* formatting
* handling missing values
* normalisasi data

### 3. Load

Menyimpan data hasil transformasi ke dalam file CSV agar siap digunakan untuk analisis lebih lanjut.

---

## 🛠️ Tech Stack

* Python
* Pandas
* BeautifulSoup
* Requests
* Pytest

---

## 📂 Project Structure

```bash id="wlt94k"
project-fundaPemrosesanData/
│
├── test/
├── utils/
├── README.md
├── fashion_product.csv
├── main.py
├── requirements.txt
└── submission.txt
```

---

## 🚀 Installation

Clone repository:

```bash id="p4o4he"
git clone https://github.com/sanhappyending/project-fundaPemrosesanData.git
```

Masuk ke folder project:

```bash id="e2o1xu"
cd project-fundaPemrosesanData
```

Install dependencies:

```bash id="kpx3ql"
pip install -r requirements.txt
```

---

## ▶️ Run Project

Jalankan ETL pipeline:

```bash id="3h1z8x"
python main.py
```

---

## 🧪 Run Testing

Untuk menjalankan testing:

```bash id="0qk3nr"
pytest
```

---

## 📊 Output

Hasil ETL pipeline akan disimpan dalam file:

```bash id="ukmncc"
fashion_product.csv
```

File tersebut berisi data produk fashion yang telah dibersihkan dan diproses.

---

## 📌 Features

* Web scraping fashion products
* Data cleaning & preprocessing
* Automated ETL workflow
* CSV export
* Project testing
