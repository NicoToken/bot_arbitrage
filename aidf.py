from terra_sdk.client.lcd import LCDClient

from terra_sdk.key.mnemonic import MnemonicKey

from terra_sdk.core import Coins, MsgExecuteContract

from itertools import permutations

# Inisialisasi LCDClient

terra_lcd = LCDClient(chain_id="columbus-4", url="https://lcd.terra.dev")

# Meminta input dari pengguna untuk kata kunci mnemonic

mnemonic = input("Masukkan kata kunci mnemonic: ")

key = MnemonicKey(mnemonic=mnemonic)

# Menginisialisasi klien menggunakan kunci

terra_client = terra_lcd.wallet(key)

# Fungsi untuk mengeksekusi order arbitrase

def execute_arbitrage_order(pair, amount):

    # Kode eksekusi order di sini

    # Misalnya, mengirimkan transaksi ke kontrak smart contract untuk melakukan arbitrase

    # Contoh penggunaan fungsi MsgExecuteContract:

    msg = MsgExecuteContract(

        sender=terra_client.key.acc_address,

        contract=pair.contract_address,

        execute_msg={

            "execute_trade": {

                "offer_asset": {

                    "info": {

                        "native_token": {

                            "denom": pair.base_symbol,

                        }

                    },

                    "amount": str(amount)

                },

                "offer_asset_2": {

                    "info": {

                        "native_token": {

                            "denom": pair.quote_symbol,

                        }

                    },

                    "amount": str(amount)

                },

            }

        },

        coins=Coins(uluna=amount),  # Jumlah dana yang akan digunakan untuk arbitrase

    )

    tx_result = terra_client.tx.create_and_broadcast(

        msgs=[msg],

        gas_prices="0.15uluna",  # Biaya gas yang ditentukan dalam ULuna

        gas_adjustment="1.4",  # Penyesuaian gas

        fee_denoms=["uluna"],

    )

    return tx_result

# Fungsi untuk mencari semua kombinasi pasangan aset

def find_asset_pairs(assets):

    pairs = list(permutations(assets, 3))

    return pairs

# Fungsi untuk melakukan screening arbitrase

def perform_arbitrage_screening(assets, target_profit, required_funds):

    pairs = find_asset_pairs(assets)

    for pair in pairs:

        base_symbol, quote_symbol = pair[0], pair[2]

        # Lakukan pengecekan persyaratan arbitrase

        # Misalnya, memeriksa spread, likuiditas, dll.

        # Contoh pemeriksaan arbitrase:

        spread = calculate_spread(pair)

        if spread >= target_profit:

            print(f"Arbitrase ditemukan pada pasangan {base_symbol}/{quote_symbol}")

            print(f"Spread: {spread}%")

            # Mengeksekusi order arbitrase

            amount = required_funds  # Jumlah dana yang akan digunakan untuk arbitrase

            tx_result = execute_arbitrage_order(pair, amount)

            # Menampilkan hasil transaksi

            print("Transaksi berhasil!")

            print("Hash Transaksi:", tx_result.txhash)

            print("-----------------------------")

# Meminta input dari pengguna untuk pasangan aset, target profit, dan dana yang dibutuhkan

pair_base_symbols = input("Masukkan simbol aset base (pisahkan dengan koma): ")

pair_quote_symbols = input("Masukkan simbol aset kutipan (pisahkan dengan koma): ")

target_profit = float(input("Masukkan target keuntungan (%): "))

required_funds = float(input("Masukkan jumlah dana yang dibutuhkan: "))

# Memisahkan pasangan simbol aset berdasarkan koma

base_symbols = pair_base_symbols.split(",")

quote_symbols = pair_quote_symbols.split(",")

# Menggabungkan pasangan aset yang valid

asset_pairs = [(base, quote) for base in base_symbols for quote in quote_symbols]

# Melakukan screening dan eksekusi arbitrase

perform_arbitrage_screening(asset_pairs, target_profit, required_funds)
