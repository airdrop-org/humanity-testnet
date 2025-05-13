Berikut adalah tutorial lengkap dalam format README.md yang dapat Anda gunakan untuk mendokumentasikan script klaim otomatis Humanity Protocol. Tutorial ini mencakup penjelasan script, cara penggunaan, dependensi, struktur file, dan langkah-langkah untuk menjalankan script dengan loop 24 jam. Saya menyesuaikan konten berdasarkan script terakhir yang hanya menggunakan token Bearer tanpa wallet address dan mendukung multiple akun.
markdown
# Humanity Protocol Auto Claim Bot

Bot ini dirancang untuk mengotomatiskan klaim reward harian dari **Humanity Protocol** (testnet) menggunakan **token Bearer** tanpa memerlukan wallet address. Script mendukung **multiple akun** (multiple token) dan berjalan secara otomatis setiap **24 jam** untuk klaim harian.

## Fitur
- **Otomatisasi 24 Jam**: Berjalan terus-menerus dengan jeda 24 jam untuk klaim harian.
- **Multiple Akun**: Mendukung banyak akun dengan memproses daftar token dari `token.txt`.
- **Token Bearer**: Hanya menggunakan token Bearer untuk autentikasi, tanpa wallet address.
- **Proxy**: Mendukung rotasi proxy dari `proxy.txt` (opsional).
- **Logging**: Menyimpan hasil klaim (sukses/gagal) ke `claim_log.txt` dengan timestamp.
- **Error Handling**: Menangani error file, request, dan penghentian manual dengan pesan jelas.
- **Optimasi**: Delay acak antar akun untuk menghindari rate limit dan timeout request.

## Prasyarat
- **Python 3.6+**: Pastikan Python terinstal di sistem Anda.
- **Dependensi**: Hanya membutuhkan library `requests`.
- **Sistem Operasi**: Linux (disarankan, misalnya Ubuntu), tetapi juga kompatibel dengan Windows/Mac.
- **Koneksi Internet**: Stabil untuk request HTTP.
- **Token Bearer**: Diperlukan untuk autentikasi (dijelaskan di bawah).

## Instalasi
1. **Clone Repository atau Buat Direktori**:
   ```bash
   git clone https://github.com/airdrop-org/humanity-testne.git
   cd humanity-testnet

Buat Virtual Environment (opsional, tetapi disarankan):
bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
Install Dependensi:
bash
pip install requests

Struktur File
Buat file berikut di direktori humanity:
token.txt:
Berisi daftar token Bearer, satu token per baris (setiap token mewakili satu akun).
Contoh:
AjBOmW2JBjgDyPz35D7/YciYN7KErx60xzerWuXAHOvIvRWOghrnXa7NEzmOHtMqptUe4BgPVF+qX68/KhIRhhZLbSpiCJkfU+H2cjm3dOYfrCpeXCXfi34gXVFwNa+PDMmWHtwAzr53kCwDH48+iTXglsx9eDmqlS+8LRREljg5NBvtzbEbbaZTLafwf8aExfMA4nBmotUCrLYyYI2Da//OVlBn/EAyTMH87jVn/FxKYBKPX14dgjlQdqlg13iO
YOUR_SECOND_TOKEN_HERE
YOUR_THIRD_TOKEN_HERE
proxy.txt (opsional):
Berisi daftar proxy untuk rotasi (format: user:pass@host:port atau host:port).
Kosongkan file jika tidak menggunakan proxy.
Contoh:
931060985fe45031da7a:39831eda9c3db68e@gw.dataimpulse.com:823
claim_log.txt:
File ini akan dibuat otomatis untuk menyimpan log hasil klaim.
Contoh isi:
2025-05-13 10:00:00,123 - INFO - Memulai siklus klaim pada 2025-05-13 10:00:00...
2025-05-13 10:00:00,456 - SUCCESS - Claim berhasil untuk token AjBOmW2JBj...: {'message': 'Daily reward claimed successfully.', 'daily_claimed': True, 'available': False}
Cara Mendapatkan Token Bearer
Token Bearer diperlukan untuk setiap akun. Ikuti langkah berikut untuk mendapatkannya:
Buka browser dan kunjungi https://testnet.humanity.org.
Buka Developer Tools (tekan F12) > tab Network.
Lakukan klaim manual:
Hubungkan wallet (jika diperlukan) atau lakukan tindakan yang menghasilkan klaim.
Klik tombol Claim di situs.
Cari request ke https://testnet.humanity.org/api/rewards/daily/claim di tab Network.
Di tab Headers, temukan header Authorization: Bearer <token>.
Salin token (bagian setelah Bearer ).
Tambahkan token ke token.txt, satu token per baris untuk setiap akun.
Catatan: Token memiliki masa kadaluarsa. Jika klaim gagal dengan error 401 (Invalid token), ulangi langkah ini untuk memperbarui token.
Cara Menjalankan
Siapkan File:
Pastikan token.txt berisi daftar token Bearer.
Siapkan proxy.txt (jika menggunakan proxy) atau biarkan kosong.
Jalankan Script:
Dari direktori humanity, jalankan:
bash
python3 bot.py
Script akan memproses semua token di token.txt dan mengulang setiap 24 jam.
Jalankan di Latar Belakang (opsional, disarankan):
Untuk menjalankan script tanpa terminal terbuka, gunakan nohup atau screen:
bash
nohup python3 bot.py &
Atau gunakan screen:
bash
screen -S humanity_bot
python3 bot.py
Tekan Ctrl+A, D untuk detach dari session. Kembali dengan screen -r humanity_bot.
Hentikan Script:
Tekan Ctrl+C di terminal untuk menghentikan.
Jika menggunakan nohup, temukan PID dan hentikan:
bash
ps aux | grep python3
kill <PID>
Contoh Output
[INFO] Memulai script klaim Humanity Protocol dengan loop 24 jam...
[INFO] Memulai siklus klaim pada 2025-05-13 10:00:00...
[INFO] Menemukan 3 akun (token).
[INFO] Memproses akun 1/3 (token: AjBOmW2JBj...) dengan proxy: 931060985fe45031da7a:39831eda9c3db68e@gw.dataimpulse.com:823
[SUCCESS] Claim berhasil untuk token AjBOmW2JBj...: {'message': 'Daily reward claimed successfully.', 'daily_claimed': True, 'available': False}
[INFO] Menunggu 3.18 detik sebelum akun berikutnya...
[INFO] Memproses akun 2/3 (token: YOUR_SECON...) dengan proxy: 931060985fe45031da7a:39831eda9c3db68e@gw.dataimpulse.com:823
[FAILED] Claim gagal untuk token YOUR_SECON...: 401 - {"name":"AuthorizationRequiredError","message":"Invalid token. Please provide a valid one.","errors":[]}
[INFO] Menunggu 2.78 detik sebelum akun berikutnya...
[INFO] Memproses akun 3/3 (token: YOUR_THIRD...) dengan proxy: 931060985fe45031da7a:39831eda9c3db68e@gw.dataimpulse.com:823
[SUCCESS] Claim berhasil untuk token YOUR_THIRD...: {'message': 'Daily reward claimed successfully.', 'daily_claimed': True, 'available': False}
[INFO] Menunggu 4.12 detik sebelum akun berikutnya...
[INFO] Siklus selesai. Menunggu 24 jam untuk klaim berikutnya (hingga 2025-05-14 10:00:00)...
Troubleshooting
Error 401 (Invalid Token):
Token di token.txt kedaluwarsa atau tidak valid.
Perbarui token dengan langkah di bagian Cara Mendapatkan Token Bearer.
Pastikan token sesuai dengan akun yang ingin diklaim.
Error 400/403:
Endpoint mungkin memerlukan parameter dalam payload (misalnya, {"type": "daily"}).
Periksa payload di browser (Developer Tools > Network > Payload).
Modifikasi fungsi claim_reward di bot.py:
python
payload = {"type": "daily"}
Proxy Gagal:
Jika request gagal karena proxy, coba tanpa proxy (kosongkan proxy.txt).
Ganti proxy dengan yang valid.
Token.txt Kosong:
Script akan menunggu 1 jam sebelum memeriksa ulang. Tambahkan token ke token.txt untuk melanjutkan.
Klaim Harian Tidak Tersedia:
Jika respons menunjukkan daily_claimed: False dan available: False, periksa aturan klaim di situs (misalnya, waktu reset harian).
Coba lagi setelah 24 jam atau sesuaikan interval di DAILY_INTERVAL (misalnya, 23 jam).
Log Debugging:
Periksa claim_log.txt untuk detail error.
Bagikan isi log jika membutuhkan bantuan.
Modifikasi Opsional
Ubah Interval Klaim:
Untuk interval berbeda (misalnya, 23 jam), ubah DAILY_INTERVAL:
python
DAILY_INTERVAL = 23 * 60 * 60  # 82,800 detik
Tambahkan Retry Otomatis:
Jika klaim gagal, script bisa mencoba lagi. Tambahkan ke fungsi claim_reward:
python
def claim_reward(token, proxy, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload, proxies=proxies, timeout=10)
            if response.status_code == 200:
                msg = f"Claim berhasil untuk token {token[:10]}...: {response.json()}"
                print(f"[SUCCESS] {msg}")
                logging.info(msg)
                return
            else:
                msg = f"Claim gagal untuk token {token[:10]}...: {response.status_code} - {response.text}"
                print(f"[FAILED] {msg}")
                logging.error(msg)
        except requests.exceptions.RequestException as e:
            msg = f"Error saat claim untuk token {token[:10]}...: {e}"
            print(f"[ERROR] {msg}")
            logging.error(msg)
        if attempt < max_retries - 1:
            retry_delay = random.uniform(30, 60)
            print(f"[INFO] Mencoba lagi dalam {retry_delay:.2f} detik...")
            logging.info(f"Mencoba lagi dalam {retry_delay:.2f} detik...")
            time.sleep(retry_delay)
Panggil dengan claim_reward(token, proxy, max_retries=3) di process_tokens.
Pemberitahuan:
Tambahkan notifikasi via Telegram/email untuk hasil klaim. Hubungi pengembang untuk implementasi.
Catatan Keamanan
Jangan bagikan token di tempat umum, karena token sensitif dan dapat disalahgunakan.
Simpan token.txt di lokasi aman.
Gunakan proxy terpercaya untuk melindungi privasi.
Kontribusi
Jika Anda ingin menambahkan fitur (misalnya, retry otomatis, notifikasi, atau jadwal kustom), buka issue atau kirim pull request di repository ini (jika menggunakan Git).
Lisensi
Script ini dibagikan di bawah MIT License (LICENSE). Gunakan dengan tanggung jawab.
Dukungan
Jika mengalami masalah atau membutuhkan fitur tambahan, hubungi melalui [email/discord] atau buka issue di repository.
Happy Claiming!

### Penjelasan README
- **Struktur**: Dibagi menjadi bagian yang jelas (Fitur, Prasyarat, Instalasi, Struktur File, dll.) untuk memudahkan pengguna.
- **Detail Teknis**: Menjelaskan cara mendapatkan token, menjalankan script, dan menangani error.
- **Keamanan**: Menekankan pentingnya menjaga token tetap aman.
- **Fleksibilitas**: Memberikan opsi untuk modifikasi (interval, retry, notifikasi) dan langkah debugging.
- **Contoh**: Menyertakan contoh file, perintah, dan output untuk kejelasan.

### Langkah untuk Menambahkan ke README.md
1. Buat file `README.md` di direktori `humanity`:
   ```bash
   touch README.md
Salin konten di atas ke README.md menggunakan editor teks (misalnya, nano, vim, atau VS Code).
Simpan dan pastikan file berada di direktori yang sama dengan bot.py.
Catatan Tambahan
Token JWT: Jika token JWT (eyJhbGciOiJSUzI1Ni...) diperlukan untuk beberapa akun, tambahkan ke token.txt bersama token lain (misalnya, AjBOmW2JBjgDyPz35D7...).
Kustomisasi: Jika Anda ingin menyesuaikan README (misalnya, menambahkan logo, link repository, atau kontak spesifik), beri tahu saya.
Eksekusi Latar Belakang: Tutorial sudah menyertakan cara menjalankan di latar belakang dengan nohup atau screen, yang cocok untuk server Linux seperti yang Anda gunakan (root@vmi2362760).
Error Handling: README mencakup solusi untuk error umum (401, 400, proxy gagal, dll.) berdasarkan diskusi sebelumnya.
Langkah Selanjutnya
Tambahkan README.md ke direktori humanity.
Siapkan token.txt dengan daftar token.
Jalankan bot.py dengan nohup atau screen untuk memastikan berjalan terus-menerus.
Pantau claim_log.txt untuk hasil klaim harian.
Jika ada error atau Anda ingin fitur tambahan (misalnya, retry otomatis, notifikasi Telegram), beri tahu saya!
Apakah Anda ingin saya menambahkan sesuatu ke README (misalnya, bagian FAQ, gambar, atau link ke Humanity Protocol)? Atau perlu bantuan menjalankan script di latar belakang?# humanity-testnet
