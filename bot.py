import requests
import json
import time
import random

# Fungsi untuk membaca file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"[ERROR] Gagal membaca {file_path}: {e}")
        return []

# Fungsi untuk memvalidasi address Ethereum
def is_valid_address(address):
    return isinstance(address, str) and len(address) == 42 and address.startswith("0x")

# Fungsi untuk melakukan claim
def claim_reward(address, token, proxy):
    url = "https://testnet.humanity.org/api/rewards/daily/claim"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Referer": "https://testnet.humanity.org/",
        "Origin": "https://testnet.humanity.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    payload = {
        "address": address
    }

    proxies = {"http": proxy, "https": proxy} if proxy else {}
    try:
        response = requests.post(url, headers=headers, json=payload, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"[SUCCESS] Claim berhasil untuk {address}: {response.json()}")
        else:
            print(f"[FAILED] Claim gagal untuk {address}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error saat claim untuk {address}: {e}")

# Fungsi untuk mendapatkan daftar akun (address dan token)
def get_accounts():
    print("Masukkan akun (format: address:token, pisahkan dengan koma untuk multiple akun, kosongkan untuk keluar):")
    user_input = input("> ").strip()
    
    if not user_input:
        print("[INFO] Tidak ada akun dimasukkan. Keluar.")
        return []
    
    accounts = []
    for account in user_input.split(","):
        try:
            address, token = account.strip().split(":")
            if is_valid_address(address):
                accounts.append({"address": address, "token": token})
            else:
                print(f"[WARNING] Address tidak valid: {address}")
        except ValueError:
            print(f"[WARNING] Format salah untuk: {account}. Gunakan address:token")
    
    if not accounts:
        print("[ERROR] Tidak ada akun valid yang dimasukkan.")
    return accounts

def main():
    # Membaca proxies
    proxies = read_file("proxy.txt")
    
    # Mendapatkan daftar akun
    accounts = get_accounts()
    if not accounts:
        return

    # Proses setiap akun
    for account in accounts:
        address = account["address"]
        token = account["token"]
        proxy = random.choice(proxies) if proxies else None
        print(f"[INFO] Memproses address: {address[:10]}... dengan proxy: {proxy if proxy else 'Tanpa proxy'}")
        
        claim_reward(address, token, proxy)
        
        # Delay untuk menghindari rate limit
        delay = random.uniform(2, 5)
        print(f"[INFO] Menunggu {delay:.2f} detik sebelum akun berikutnya...")
        time.sleep(delay)

if __name__ == "__main__":
    try:
        print("[INFO] Memulai script klaim Humanity Protocol...")
        main()
        print("[INFO] Selesai memproses semua akun.")
    except KeyboardInterrupt:
        print("[INFO] Script dihentikan oleh pengguna.")
    except Exception as e:
        print(f"[ERROR] Kesalahan tak terduga: {e}")
