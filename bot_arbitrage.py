import ccxt

# Inisialisasi exchange Binance

exchange = ccxt.binance({

    'apiKey': 'hbX0DUDCzJRpICSUsAyagghbG7oII3XETOHvC1c1zs1Pr5SfzVA46xDzIA0iI2Hs',

    'secret': 'p6kM0rlWoRK2QISVEWgowx0ReCYn2JZzbzoMqDLKSyqLJAKo7D8e8miG0nIFtFXJ'

})

# Fungsi untuk mendapatkan harga aset di pasar future

def get_future_price(symbol):

    future_ticker = exchange.fetch_ticker(symbol)

    return float(future_ticker['bid'])

# Fungsi untuk mendapatkan harga aset di pasar spot

def get_spot_price(symbol):

    spot_ticker = exchange.fetch_ticker(symbol)

    return float(spot_ticker['bid'])

# Fungsi utama untuk menjalankan strategi arbitrase

def run_arbitrage(symbol, threshold, quantity):

    future_price = get_future_price(symbol)

    spot_price = get_spot_price(symbol)

    price_diff = future_price - spot_price

    

    if price_diff > threshold:

        # Logika pembelian dan penjualan

        # Implementasikan strategi Anda di sini

        # Misalnya, melakukan pembelian di pasar spot dan menjual di pasar future

        

        # Membeli aset di pasar spot

        buy_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

        print("Order pembelian di pasar spot:", buy_order)

        

        # Menjual aset di pasar future

        sell_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

        print("Order penjualan di pasar future:", sell_order)

        

        print("Peluang arbitrase terdeteksi!")

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih harga:", price_diff)

    else:

        print("Tidak ada peluang arbitrase saat ini.")

# Menjalankan bot dengan simbol, threshold, dan quantity tertentu

symbol = 'BTC/USDT'  # Ganti dengan pasangan aset yang diinginkan

threshold = 10  # Ganti dengan threshold perbedaan harga yang diinginkan

quantity = 0.001  # Ganti dengan jumlah aset yang diinginkan

run_arbitrage(symbol, threshold, quantity)

