Karena Anda sedang membangun jembatan antara **Python (Flask)** dan **n8n**, dokumentasi yang rapi akan sangat membantu saat Anda melakukan konfigurasi node di n8n.

Berikut adalah dokumentasi API sederhana untuk proyek Anda:

---

## 📄 Dokumentasi API: User Management (Local/VPS)

API ini digunakan untuk menyimpan dan mengambil data pengguna (nama & email) menggunakan database SQLite.

### **Base URL**
* **Lokal:** `http://localhost:5000`
* **VPS:** `http://IP_VPS_ANDA:5000`

---

### **1. Get All Users (Read)**
Mengambil semua daftar user yang tersimpan di database.

* **Endpoint:** `/users`
* **Method:** `GET`
* **Response (JSON):**
    ```json
    [
      {
        "id": 1,
        "nama": "Budi Santoso",
        "email": "budi@example.com"
      }
    ]
    ```

### **2. Create New User (Create)**
Menambahkan user baru ke dalam database SQLite.

* **Endpoint:** `/users`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Body (JSON):**
    ```json
    {
      "nama": "John Doe",
      "email": "john@n8n.io"
    }
    ```
* **Response (JSON):**
    ```json
    {
      "id": 2,
      "message": "User berhasil dibuat"
    }
    ```

---

## 🛠 Cara Penggunaan di n8n

Berikut adalah langkah teknis untuk menghubungkan n8n ke API Anda:

### **A. Menggunakan GET (Menarik Data)**
1.  Tambahkan node **HTTP Request**.
2.  Set **Method** ke `GET`.
3.  Masukkan **URL**: `http://IP_VPS_ANDA:5000/users`.
4.  Klik **Execute Node**. Data dari SQLite akan muncul di panel output n8n.

### **B. Menggunakan POST (Mengirim Data)**
1.  Tambahkan node **HTTP Request**.
2.  Set **Method** ke `POST`.
3.  Masukkan **URL**: `http://IP_VPS_ANDA:5000/users`.
4.  Aktifkan **Send Body** (Toggle On).
5.  Pilih **Body Content Type**: `JSON`.
6.  Di bagian **Specify Body**, pilih `Using Fields Below`.
7.  Tambahkan Parameter:
    * `nama` : `{{ $json.nama_dari_node_sebelumnya }}`
    * `email`: `{{ $json.email_dari_node_sebelumnya }}`
8.  Klik **Execute Node**.

---

## ⚠️ Tips Troubleshooting

* **Port 5000:** Jika n8n memberikan error *Connection Refused*, pastikan aplikasi Python sudah jalan dan port 5000 tidak diblokir firewall.
* **Data Kosong:** Saat pertama kali dijalankan, `GET` akan menghasilkan array kosong `[]` karena SQLite baru saja dibuat. Lakukan `POST` terlebih dahulu untuk mengisi data.
* **Format JSON:** n8n sangat sensitif terhadap format. Pastikan saat memilih `Using JSON` di body, format kurung kurawal `{}` sudah benar.



Apakah Anda ingin saya tambahkan fitur **Basic Authentication** (Username & Password) pada kode Python tersebut agar API Anda lebih aman saat diakses dari internet?
