import ccxt

# Inisialisasi exchange Binance

exchange = ccxt.binance()

# Memperoleh daftar pasangan aset future

markets = exchange.load_markets()

# Mencetak daftar pasangan aset future

for symbol in markets:

    if 'future' in markets[symbol]['info']['pairType']:

        print(symbol)

