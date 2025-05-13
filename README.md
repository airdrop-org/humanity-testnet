## 🚀 Fitur

- ✅ **Klaim Otomatis Setiap 24 Jam**
- 🧑‍🤝‍🧑 **Dukungan Multi-Akun**: Proses banyak token dalam satu kali jalan
- 🔐 **Tanpa Wallet Address**: Hanya gunakan Bearer token
- 🌐 **Proxy Support**: Dukungan rotasi proxy (opsional)
- 📜 **Logging Lengkap**: Simpan semua aktivitas klaim ke `claim_log.txt`
- 🔁 **Delay Acak Antar Token**: Hindari rate limit otomatis
- ⚠️ **Error Handling**: Tahan banting, tidak langsung crash

---

## 📦 Prasyarat

- Python 3.6+
- Library: `requests`
- OS: Linux (disarankan), Windows, Mac
- Koneksi internet stabil
- File Bearer Token (`token.txt`)

---

## 🛠️ Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/airdrop-org/humanity-testnet.git
cd humanity-testnet
````

### 2. Buat Virtual Environment (opsional tapi direkomendasikan)

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
.\venv\Scripts\activate         # Windows
```

### 3. Install Dependensi

```bash
pip install requests
```

---

## 📁 Struktur File

```
humanity-testnet/
├── bot.py
├── token.txt
├── proxy.txt       (opsional)
├── claim_log.txt   (otomatis dibuat)
└── README.md
```

### `token.txt`

Berisi daftar token Bearer, satu per baris:

```
AjBOmW2JBj... (token 1)
eyJhbGciOiJ... (token 2)
...
```

### `proxy.txt` *(opsional)*

Format:

```
username:password@host:port
host:port
```

---

## 🔐 Cara Mendapatkan Bearer Token

1. Buka situs: [https://testnet.humanity.org](https://testnet.humanity.org/login?ref=daimun)
2. Buka **DevTools (F12)** → Tab **Network**
3. Klik tombol **Claim**
4. Cari request ke `/api/rewards/daily/claim`
5. Buka tab **Headers** → cari `Authorization: Bearer <token>`
6. Salin token dan tempel ke `token.txt`
![Cuplikan layar 2025-05-13 110253](https://github.com/user-attachments/assets/8a89d789-9fab-4b05-a5d9-f969d379632d)
⚠️ *Token bersifat sensitif dan dapat kadaluarsa. Perbarui jika klaim gagal.*

---

## ▶️ Menjalankan Bot

### Jalankan Manual

```bash
python3 bot.py
```

### Jalankan di Background (Linux)

```bash
nohup python3 bot.py &
# atau
screen -S humanity_bot
python3 bot.py
# lalu Ctrl+A, D untuk detach
```

### Hentikan Bot

```bash
ps aux | grep python3
kill <PID>
# atau di screen:
screen -r humanity_bot
Ctrl+C
```

---

## 📝 Contoh Output

```log
[INFO] Memulai klaim pada 2025-05-13 10:00:00...
[INFO] 3 akun ditemukan
[SUCCESS] Claim berhasil untuk token AjBOmW2JBj...: {'message': 'Daily reward claimed successfully.'}
[FAILED] Claim gagal untuk token YOUR_TOKEN: 401 - Invalid token.
[INFO] Siklus selesai. Menunggu 24 jam hingga 2025-05-14 10:00:00...
```

---

## 🧪 Troubleshooting

| Masalah              | Penyebab                      | Solusi                                           |
| -------------------- | ----------------------------- | ------------------------------------------------ |
| 401 Unauthorized     | Token kadaluarsa / salah      | Perbarui dari browser                            |
| 400/403 Error        | Payload kurang / salah format | Tambahkan payload `{"type": "daily"}` di request |
| Proxy Error          | Proxy mati / salah format     | Ganti atau kosongkan proxy.txt                   |
| `token.txt` kosong   | Tidak ada akun untuk diproses | Tambahkan token dan restart                      |
| Klaim tidak tersedia | Belum saatnya klaim harian    | Tunggu hingga waktu reset harian                 |

---

## 🧩 Kustomisasi

### 🔄 Ubah Interval Klaim

Di `bot.py`, ubah:

```python
DAILY_INTERVAL = 23 * 60 * 60  # 23 jam
```

### 🔁 Retry Otomatis (Opsional)

Modifikasi fungsi `claim_reward()` agar mencoba ulang jika gagal:

```python
def claim_reward(token, proxy, max_retries=3):
    for attempt in range(max_retries):
        try:
            ...
        except:
            ...
        if attempt < max_retries - 1:
            time.sleep(random.uniform(30, 60))
```

### 🔔 Notifikasi Telegram

Tambahkan pengiriman log atau hasil ke Telegram melalui bot. Hubungi pengembang jika ingin integrasi ini.

---

## 🔐 Tips Keamanan

* Jangan membagikan `token.txt`
* Simpan token di server aman
* Gunakan proxy terpercaya

---

## 🙌 Kontribusi

Pull request dan issue sangat disambut. Fitur seperti:

* Retry otomatis
* Notifikasi Telegram
* Web dashboard

Silakan fork repo dan kembangkan!

---

## 📄 Lisensi

MIT License © 2025 — Gunakan dengan tanggung jawab.

---

## 📬 Bantuan

Butuh bantuan atau ingin fitur baru?
📧 Email: `support@humanity-bot.dev`
💬 Discord: `discord.gg/humanity-testnet` *(contoh)*
atau buka **Issue** di GitHub.

---

## ✨ Selamat Klaim Harian! ✨

```

---

Jika kamu ingin:
- Menambahkan **logo Humanity** di bagian atas
- Menyematkan **badge GitHub** (build passing, license, stars)
- Mengubah tema warna dokumen
- Menambahkan link langsung ke `bot.py`

Beritahu saja! Saya bisa bantu integrasikan langsung ke tampilan markdown yang menarik.
```
