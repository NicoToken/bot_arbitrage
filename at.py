import os

import requests

import time

from terra_sdk.client.lcd import LCDClient

from terra_sdk.key.mnemonic import MnemonicKey

LCD_URL = "<lcd_url>"

MNEMONIC = "<your_mnemonic>"

ASTROPORT_ROUTER_ADDRESS = "<astroport_router_address>"

TERRASWAP_ROUTER_ADDRESS = "<terraswap_router_address>"

# Inisialisasi Terra Station LCD Client dan kontrak Astroport dan Terraswap

lcd = LCDClient(chain_id="columbus-5", url=LCD_URL)

mnemonic_key = MnemonicKey(mnemonic=MNEMONIC)

wallet = lcd.wallet(mnemonic_key)

astroport_router = lcd.wasm.contract(ASTROPORT_ROUTER_ADDRESS)

terraswap_router = lcd.wasm.contract(TERRASWAP_ROUTER_ADDRESS)

# Mendapatkan saldo akun

def get_balance(asset, address):

    balance = wallet.balance(address, asset)

    return balance.amount

# Mendapatkan harga token di Astroport

def get_price_on_astroport(token):

    result = astroport_router.query(

        {"simulation": {"offer_asset": {"amount": "1000000", "info": token}, "to": ["uusd"]}}

    )

    return result["return_amount"]

# Mendapatkan harga token di Terraswap

def get_price_on_terraswap(token):

    result = terraswap_router.query(

        {"simulation": {"offer_asset": {"amount": "1000000", "info": token}, "to": ["uusd"]}}

    )

    return result["return_amount"]

# Mendapatkan selisih harga antara Astroport dan Terraswap

def get_price_difference(token):

    astroport_price = get_price_on_astroport(token)

    terraswap_price = get_price_on_terraswap(token)

    price_difference = astroport_price - terraswap_price

    return price_difference

# Main function untuk bot arbitrase

def run_arbitrage_bot():

    while True:

        astroport_pairs = get_token_pairs(ASTROPORT_ROUTER_ADDRESS)

        terraswap_pairs = get_token_pairs(TERRASWAP_ROUTER_ADDRESS)

        common_pairs = set(astroport_pairs).intersection(terraswap_pairs)

        for pair in common_pairs:

            token1, token2 = pair.split("/")

            price_difference = get_price_difference(token1)

            percentage_difference = (price_difference / get_price_on_terraswap(token1)) * 100

            print("Pair: {} - Percentage Difference: {:.2f}%".format(pair, percentage_difference))

        time.sleep(5)

# Mendapatkan daftar pasangan token yang tersedia di suatu router

def get_token_pairs(router_address):

    result = lcd.wasm.contract_query(router_address, {"pairs": {}})

    pairs = result["pairs"]

    return pairs

run_arbitrage_bot()

