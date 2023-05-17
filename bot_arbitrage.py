import ccxt

# Inisialisasi exchange Binance

exchange = ccxt.binance({

    'apiKey': 'YOUR_API_KEY',

    'secret': 'YOUR_API_SECRET'

})

# Fungsi untuk mendapatkan harga aset di pasar future

def get_future_price(symbol):

    future_ticker = exchange.fapiPublic_get_ticker_bookticker({'symbol': symbol})

    return float(future_ticker['bidPrice'])

# Fungsi untuk mendapatkan harga aset di pasar spot

def get_spot_price(symbol):

    spot_ticker = exchange.public_get_ticker_bookticker({'symbol': symbol})

    return float(spot_ticker['bidPrice'])

# Fungsi utama untuk menjalankan strategi arbitrase

def run_arbitrage(symbol, threshold):

    future_price = get_future_price(symbol)

    spot_price = get_spot_price(symbol)

    price_diff = future_price - spot_price

    

    if price_diff > threshold:

        # Logika pembelian dan penjualan

        # Implementasikan strategi Anda di sini

        # Misalnya, melakukan pembelian di pasar spot dan menjual di pasar future

        

        print("Peluang arbitrase terdeteksi!")

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih harga:", price_diff)

    else:

        print("Tidak ada peluang arbitrase saat ini.")

# Menjalankan bot dengan simbol dan threshold tertentu

symbol = 'BTC/USDT'  # Ganti dengan pasangan aset yang diinginkan

threshold = 10  # Ganti dengan threshold perbedaan harga yang diinginkan

run_arbitrage(symbol, threshold)

