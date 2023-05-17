import ccxt

import time

import statistics

# Inisialisasi exchange Binance

exchange = ccxt.binance()

# Fungsi untuk mendapatkan harga aset di pasar future

def get_future_price(symbol):

    future_ticker = exchange.fetch_ticker(symbol)

    return float(future_ticker['bid'])

# Fungsi untuk mendapatkan harga aset di pasar spot

def get_spot_price(symbol):

    spot_ticker = exchange.fetch_ticker(symbol)

    return float(spot_ticker['bid'])

# Fungsi untuk menghitung persentase keuntungan/kerugian

def calculate_profit_loss(initial_value, final_value):

    return ((final_value - initial_value) / initial_value) * 100

# Fungsi untuk menghitung threshold

def calculate_threshold(price_history):

    if len(price_history) < 2:

        return None

    mean_price = statistics.mean(price_history)

    std_dev = statistics.stdev(price_history)

    if mean_price == 0:

        print("Mean price is zero. Cannot calculate threshold.")

        return None

    threshold = (std_dev / mean_price) * 100

    return threshold
# Fungsi utama untuk menjalankan strategi arbitrase

def run_arbitrage(symbol, quantity, target_profit):

    price_history = []

    while True:

        future_price = get_future_price(symbol)

        spot_price = get_spot_price(symbol)

        price_diff = future_price - spot_price

        price_history.append(spot_price)

        if len(price_history) > 10:

            price_history.pop(0)

        print("===================================")

        print("Waktu:", time.ctime())

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih harga:", price_diff)

        # Menghitung threshold secara dinamis

        threshold = calculate_threshold(price_history)

        if threshold is None:

            threshold = 10  # Nilai default jika terjadi kesalahan

        print("Threshold:", threshold)

        print("Kuantitas yang akan dieksekusi:", quantity)

        print("===================================")

        if price_diff > threshold:

            # Logika pembelian dan penjualan

            # Implementasikan strategi Anda di sini

            # Misalnya, melakukan pembelian di pasar spot dan menjual di pasar future

            # Membeli aset di pasar spot

            buy_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

            print("Order pembelian di pasar spot:", buy_order)

            buy_price = float(buy_order['fills'][0]['price'])

            # Menjual aset di pasar future

            sell_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

            print("Order penjualan di pasar future:", sell_order)

            sell_price = float(sell_order['fills'][0]['price'])

            profit_loss_percentage = calculate_profit_loss(buy_price, sell_price)

            print("Peluang arbitrase terdeteksi!")

            print("Harga future:", future_price)

            print("Harga spot:", spot_price)

            print("Selisih harga:", price_diff)

            print("Keuntungan/Kerugian (%):", profit_loss_percentage)
# Fungsi untuk menjalankan program

def main():

    symbol = 'BTC/USDT'  # Simbol aset yang diperdagangkan

    quantity = 0.01  # Kuantitas aset yang akan diperdagangkan

    target_profit = 2  # Target keuntungan dalam persentase

    run_arbitrage(symbol, quantity, target_profit)

if __name__ == '__main__':

    main()

# Fungsi untuk menjalankan program

def main():

    symbol = 'BTC/USDT'  # Simbol aset yang diperdagangkan

    quantity = 0.01  # Kuantitas aset yang akan diperdagangkan

    target_profit = 2  # Target keuntungan dalam persentase

    run_arbitrage(symbol, quantity, target_profit)

if __name__ == '__main__':

    main()


            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

                print("Order penutupan pembelian di pasar spot:", close_buy_order)

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

                print("Order penutupan penjualan di pasar future:", close_sell_order)

        time.sleep(5)  # Jeda 5 detik sebelum iterasi berikutnya

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

                print("Order penutupan pembelian di pasar spot:", close_buy_order)

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

                print("Order penutupan penjualan di pasar future:", close_sell_order)

        time.sleep(5)  # Jeda 5 detik sebelum iterasi berikutnya

# Fungsi untuk menghitung threshold yang optimal

def calculate_threshold(price_history):

    price_changes = []

    # Menghitung perubahan harga antar waktu

    for i in range(1, len(price_history)):

        price_changes.append((price_history[i] - price_history[i-1]) / price_history[i-1])

    mean_change = statistics.mean(price_changes)

    std_dev = statistics.stdev(price_changes)

    threshold = (std_dev / mean_change) * 100

    return threshold

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

                print("Order penutupan pembelian di pasar spot:", close_buy_order)

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

                print("Order penutupan penjualan di pasar future:", close_sell_order)

        time.sleep(5)  # Jeda 5 detik sebelum iterasi berikutnya

# Fungsi untuk menghitung threshold yang optimal

def calculate_threshold(price_history):

    price_changes = []

    # Menghitung perubahan harga antar waktu

    for i in range(1, len(price_history)):

        price_changes.append((price_history[i] - price_history[i-1]) / price_history[i-1])

    mean_change = statistics.mean(price_changes)

    std_dev = statistics.stdev(price_changes)

    threshold = (std_dev / mean_change) * 100

    return threshold

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

                print("Order penutupan pembelian di pasar spot:", close_buy_order)

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

                print("Order penutupan penjualan di pasar future:", close_sell_order)

        time.sleep(5)  # Jeda 5 detik sebelum iterasi berikutnya

# Fungsi untuk menghitung threshold yang optimal

def calculate_threshold(price_history):

    price_changes = []

    # Menghitung perubahan harga antar waktu

    for i in range(1, len(price_history)):

        price_changes.append((price_history[i] - price_history[i-1]) / price_history[i-1])

    mean_change = statistics.mean(price_changes)

    std_dev = statistics.stdev(price_changes)

    threshold = (std_dev / mean_change) * 100

    return threshold

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

# Fungsi utama untuk menjalankan strategi arbitrase

def run_arbitrage(symbol, quantity, target_profit):

    price_history = []

    while True:

        future_price = get_future_price(symbol)

        spot_price = get_spot_price(symbol)

        price_diff = future_price - spot_price

        print("===============================")

        print("Waktu:", time.ctime())

        print("Harga Future:", future_price)

        print("Harga Spot:", spot_price)

        print("Selisih Harga:", price_diff)

        print("===============================")

        price_history.append(spot_price)

        if len(price_history) > 20:

            price_history.pop(0)

        if len(price_history) == 20:

            threshold = calculate_threshold(price_history)

            print("Threshold:", threshold)

            if price_diff > threshold:

                # Implementasikan logika pembelian dan penjualan di sini

                # ...

        time.sleep(5)  # Jeda 5 detik sebelum iterasi berikutnya

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan ter

