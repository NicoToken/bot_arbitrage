import ccxt

# Inisialisasi exchange Binance

exchange = ccxt.binance()

# Fungsi untuk mendapatkan ticker harga aset future

def get_future_ticker(symbol):

    future_ticker = exchange.fetch_ticker(symbol)

    return future_ticker

# Meminta input dari pengguna untuk simbol kripto

symbol = input("Masukkan simbol kripto (misalnya BTC/USDT): ")

# Mendapatkan ticker harga aset future

future_ticker = get_future_ticker(symbol)

# Menampilkan informasi ticker

print("Simbol:", future_ticker['symbol'])

print("Harga terakhir:", future_ticker['last'])

print("Harga tertinggi:", future_ticker['high'])

print("Harga terendah:", future_ticker['low'])

print("Volume 24 jam:", future_ticker['quoteVolume'])

