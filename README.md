# 🚀 NRF NETT - Telegram Userbot for MikroTik Monitoring

Userbot ini dibangun menggunakan [Telethon](https://github.com/LonamiWebs/Telethon) dan terhubung langsung ke router MikroTik kamu untuk memantau, mengontrol, dan mengelola jaringan secara real-time langsung dari Telegram.

---

## 📦 Fitur Utama

| Perintah Telegram        | Fungsi                                                                 |
|--------------------------|------------------------------------------------------------------------|
| `.ping`                  | Cek apakah bot aktif                                                   |
| `.pppoeactive`           | Menampilkan daftar user PPPoE yang sedang login                        |
| `.addpppoe <user> <pw>`  | Tambahkan user PPPoE manual melalui Telegram                           |
| `.delpppoe <user>`       | Hapus user PPPoE                                                       |
| `.dhcpactive`            | Menampilkan DHCP lease aktif                                           |
| `.pppoeinterface`        | Tampilkan status semua interface PPPoE                                 |
| `.ifaceinfo`             | Menampilkan status semua interface (ether/wlan/pppoe/etc)              |
| `.traffic <interface>`   | Lihat trafik upload/download interface tertentu (misal `ether1`)       |

---

## 📂 Struktur Folder

```
myuserbot/
├── userbot/
│   ├── main.py
│   ├── __init__.py
│   └── modules/
│       ├── __init__.py
│       ├── pppoe.py
│       └── network_monitor.py
├── config.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalasi & Setup

### 1. Install Python

Unduh dan install **Python 3.10+** dari [https://www.python.org](https://www.python.org)

> ⚠️ Jangan lupa centang "Add Python to PATH" saat instalasi!

---

### 2. Clone atau Buat Manual

```bash
git clone https://github.com/RizkyPutra25/kyubotjar
cd kyubotjar
```

Atau buat manual di laptop, lalu isi file sesuai struktur di atas.

---

### 3. Install Dependensi

```bash
python -m pip install -r requirements.txt
```

---

### 4. Isi file `.env`

```
API_ID=25*****
API_HASH=cd£££££*£*£*£**
STRING_SESSION=ISI_STRING_SESSION

MIKROTIK_HOST=192.***.*.*
MIKROTIK_PORT=8728
MIKROTIK_USER=admin
MIKROTIK_PASS=****
```

---

### 5. Jalankan Bot

```bash
python userbot/main.py
```

Bot akan mulai aktif dan siap menerima perintah dari Telegram.

---

## ✅ Versi Library yang Direkomendasikan

| Library         | Versi       |
|------------------|-------------|
| `telethon`      | `1.33.1`    |
| `routeros_api`  | `0.15.5`    |
| `python-dotenv` | `1.0.1`     |

---

## 🛡️ Keamanan

- Jangan upload file `.env` ke GitHub
- Gunakan repo **private**
- Rutin ganti password MikroTik

---

## 📝 Catatan Tambahan

- Bot ini cocok untuk jaringan RT/RW Net, warnet, kosan, dll
- Bisa ditambah fitur:
  - Struk pembayaran PDF
  - Reminder tagihan otomatis
  - Dashboard web FastAPI

---

## 👨‍💻 Developer

Made with ❤️ by **Muhamad Rizky Putra Mulya Ramdan**  
📡 NRF NETT — Network Reliable Fast  
📧 Email: [pmr58806@gmail.com](mailto:pmr58806@gmail.com)
