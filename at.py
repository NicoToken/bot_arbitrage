import os

import requests

import time

from terra_sdk.client.lcd import LCDClient

from terra_sdk.key.mnemonic import MnemonicKey

LCD_URL = "https://phoenix-lcd.terra.dev"

MNEMONIC = "rapid maple cage easily kangaroo now slogan toss trouble paper yard culture able earth aware biology fever truly theory dragon antique deal better desk"

ASTROPORT_ROUTER_ADDRESS = "terra1j8hayvehh3yy02c2vtw5fdhz9f4drhtee8p5n5rguvg3nyd6m83qd2y90a"

TERRASWAP_ROUTER_ADDRESS = "terra13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzqcu7chk"

# Inisialisasi Terra Station LCD Client dan kontrak Astroport dan Terraswap

lcd = LCDClient(chain_id="phoenix-1", url=LCD_URL)

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

