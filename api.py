from flask import Flask, json
import requests
from binance.client import Client
import blockcypher
from flask import request
from flask import jsonify
import json
import datetime
import logging
api = Flask(__name__)

logging.basicConfig(filename='demo.log', level=logging.DEBUG)


#blockcypher api key
blockcypher_api_key = '0e58e194d85c4120a641aadf3c0c7883'

# api_key that we request
requested_api_key = '4A404E635266556A586E3272357538782F4125442A472D4B6150645367566B59'

#error codes
@api.errorhandler(401)
def unauthorized(error=None):
    message = {
            'status': 401,
            'message': 'Api Key Required: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 401

    return resp


@api.route('/get_cryptocurrency_prices', methods=['GET'])
def get_cryptocurrency_prices():

    api_key = request.headers.get('api_key')
    
    ### get authenticated to binance
    client = Client('aCOMJtcUCKyMxGcZ9KaUB521MwfjeIXxAIiH0emEE6GwWd4KmRdEobk6eyIoI1lW', 
    '68xBDA81ok4fMx7hTFxCsCx1vk6xGGJpHNetXI3C8c9mqPEmyEG6o91dI9URBuBH')

    ###get prices from binance
    #USD-TRY
    usd_try_json = client.get_avg_price(symbol='BUSDTRY')
    usd_try = usd_try_json['price']
    #EUR-TRY
    eur_usd_json = client.get_avg_price(symbol='EURBUSD')
    eur_usd = eur_usd_json['price']
    eur_try = float(eur_usd) * float(usd_try)
    #BTC-USD
    btc_usd_json = client.get_avg_price(symbol='BTCUSDT')
    btc_usd = btc_usd_json['price']
    btc_usd_sell = float(btc_usd) * float(1.01)
    btc_usd_buy = float(btc_usd) * float(0.99)
    #BTC-EUR
    btc_eur = float(btc_usd) / float(eur_usd)
    btc_eur_sell = float(btc_eur) * float(1.01)
    btc_eur_buy = float(btc_eur) * float(0.99)
    #BTC-TRY
    btc_try = float(btc_usd) * float(usd_try)
    btc_try_sell = float(btc_try) * float(1.01)
    btc_try_buy = float(btc_try) * float(0.99)
    #eth-USD
    eth_usd_json = client.get_avg_price(symbol='ETHUSDT')
    eth_usd = eth_usd_json['price']
    eth_usd_sell = float(eth_usd) * float(1.01)
    eth_usd_buy = float(eth_usd) *float(0.99)
    #eth-EUR
    eth_eur = float(eth_usd) / float(eur_usd)
    eth_eur_sell = float(eth_eur) * float(1.01)
    eth_eur_buy = float(eth_eur) *float(0.99)
    #eth-TRY
    eth_try = float(eth_usd) * float(usd_try)
    eth_try_sell = float(eth_try) * float(1.01)
    eth_try_buy = float(eth_try) *float(0.99)
    #ltc-USD
    ltc_usd_json = client.get_avg_price(symbol='LTCUSDT')
    ltc_usd = ltc_usd_json['price']
    ltc_usd_sell = float(ltc_usd) * float(1.01)
    ltc_usd_buy = float(ltc_usd) * float(0.99)
    #ltc-EUR
    ltc_eur = float(ltc_usd) / float(eur_usd)    
    ltc_eur_sell = float(ltc_eur) * float(1.01)
    ltc_eur_buy = float(ltc_eur) *float(0.99)
    #ltc-TRY
    ltc_try = float(ltc_usd) * float(usd_try)
    ltc_try_sell = float(ltc_try) * float(1.01)
    ltc_try_buy = float(ltc_try) * float(0.99)
    #xrp-USD
    xrp_usd_json = client.get_avg_price(symbol='XRPUSDT')
    xrp_usd = xrp_usd_json['price']
    xrp_usd_sell = float(xrp_usd) * float(1.01)
    xrp_usd_buy = float(xrp_usd) * float(0.99)
    #xrp-EUR
    xrp_eur = float(xrp_usd) / float(eur_usd)
    xrp_eur_sell = float(xrp_eur) * float(1.01)
    xrp_eur_buy = float(xrp_eur) *float(0.99)
    #xrp-TRY
    xrp_try = float(xrp_usd) * float(usd_try)
    xrp_try_sell = float(xrp_try) * float(1.01)
    xrp_try_buy = float(xrp_try) *float(0.99)

    if api_key == requested_api_key:
        return {
                'usd_try': float(usd_try),
                'eur_try': eur_try,
                'btc_usd_buy': float(btc_usd_buy),
                'btc_eur_buy': float(btc_eur_buy),
                'btc_try_buy': float(btc_try_buy),
                'btc_usd_sell': float(btc_usd_sell),
                'btc_eur_sell': float(btc_eur_sell),
                'btc_try_sell': float(btc_try_sell),
                'eth_usd_buy': float(eth_usd_buy),
                'eth_eur_buy': float(eth_eur_buy),
                'eth_try_buy': float(eth_try_buy),
                'eth_usd_sell': float(eth_usd_sell),
                'eth_eur_sell': float(eth_eur_sell),
                'eth_try_sell': float(eth_try_sell),
                'ltc_usd_buy': float(ltc_usd_buy),
                'ltc_eur_buy': float(ltc_eur_buy),
                'ltc_try_buy': float(ltc_try_buy),
                'ltc_usd_sell': float(ltc_usd_sell),
                'ltc_eur_sell': float(ltc_eur_sell),
                'ltc_try_sell': float(ltc_try_sell),
                'xrp_usd_buy': float(xrp_usd_buy),
                'xrp_eur_buy': float(xrp_eur_buy),
                'xrp_try_buy': float(xrp_try_buy),
                'xrp_usd_sell': float(xrp_usd_sell),
                'xrp_eur_sell': float(xrp_eur_sell),
                'xrp_try_sell': float(xrp_try_sell)
        }

            
    else:
        return unauthorized()
    

@api.route('/get_account_balance', methods=['GET'])
def get_account_balance():
    #api_key = request.headers.get('api_key')
    api_key = request.headers.get('api_key')
    coin_symbol = request.headers.get('coin_symbol')
    ''' 
    coin_symbol = request.headers.get('coin_symbol')
    address = request.headers.get('address')
        
    if coin_symbol == 'xrp':
        url = 'https://data.ripple.com/v2/accounts/' + address + '/balance_changes'
        r = requests.get(url)
        response = r.json()
    else:
        url = 'https://api.blockcypher.com/v1/' + coin_symbol + '/main/addrs/' + address + '/balance'
        r = requests.get(url)
        response = r.json()
    '''
    if coin_symbol == 'all':
        with open('./deposit_wallet/btc/wallet.json') as json_file:
            data = json.load(json_file)
            btc_wallet_address = data['address']
            btc_wallet_balance = blockcypher.get_address_overview(btc_wallet_address)

        with open('./deposit_wallet/btc_testnet/wallet.json') as json_file:
            data = json.load(json_file)
            btc_testnet_wallet_address = data['address']
            btc_testnet_wallet_balance = blockcypher.get_address_overview(btc_testnet_wallet_address,coin_symbol="btc-testnet")

        with open('./deposit_wallet/ltc/wallet.json') as json_file:
            data = json.load(json_file)
            ltc_wallet_address = data['address']
            ltc_wallet_balance = blockcypher.get_address_overview(ltc_wallet_address, coin_symbol="ltc")

        with open('./atm0001_wallet/btc/wallet.json') as json_file:
            data = json.load(json_file)
            btc_atm0001_wallet_address = data['address']
            btc_atm0001_wallet_balance = blockcypher.get_address_overview(btc_atm0001_wallet_address)

        with open('./atm0001_wallet/btc_testnet/wallet.json') as json_file:
            data = json.load(json_file)
            btc_atm0001_testnet_wallet_address = data['address']
            btc_atm0001_testnet_wallet_balance = blockcypher.get_address_overview(btc_atm0001_testnet_wallet_address, coin_symbol="btc-testnet")
        
        with open('./atm0001_wallet/ltc/wallet.json') as json_file:
            data = json.load(json_file)
            ltc_atm0001_wallet_address = data['address']
            ltc_atm0001_wallet_balance = blockcypher.get_address_overview(ltc_atm0001_wallet_address, coin_symbol="ltc")
        result = {
                "btc_balance": btc_wallet_balance,
                "ltc_balance": ltc_wallet_balance,
                "btc-tesnet_balance": btc_testnet_wallet_balance,
                "atm0001_wallet": {
                    "btc_balance": btc_atm0001_wallet_balance,
                    "ltc_balance": ltc_atm0001_wallet_balance,
                    "btc-testnet_balance": btc_atm0001_testnet_wallet_balance
                }
        }



    if coin_symbol == 'btc':
        with open('./deposit_wallet/btc/wallet.json') as json_file:
            data = json.load(json_file)
            btc_wallet_address = data['address']
            btc_wallet_balance = blockcypher.get_address_overview(btc_wallet_address)
        result = {
            "btc": btc_wallet_balance
            }
            
    if coin_symbol == 'ltc':
        with open('./deposit_wallet/ltc/wallet.json') as json_file:
            data = json.load(json_file)
            ltc_wallet_address = data['address']
            ltc_wallet_balance = blockcypher.get_address_overview(ltc_wallet_address, coin_symbol="ltc")
        result = {
            "ltc": ltc_wallet_balance
            }

    if coin_symbol == 'btc-testnet':
        with open('./deposit_wallet/btc_testnet/wallet.json') as json_file:
            data = json.load(json_file)
            btc_testnet_wallet_address = data['address']
            btc_testnet_wallet_balance = blockcypher.get_address_overview(btc_testnet_wallet_address,coin_symbol="btc-testnet")
        result = {
            "btc-testnet": btc_testnet_wallet_balance
            }

    

    if api_key == requested_api_key:
        return result
    else:
        return unauthorized()


@api.route('/check_wallet_validity', methods=['GET'])
def check_wallet_validity():
    api_key = request.headers.get('api_key')
    address = request.headers.get('address')
    coin_symbol = request.headers.get('coin_symbol')
    try:
        blockcypher.get_address_details(address,coin_symbol=coin_symbol)
        result = 'True'
    except:
        result = 'False'

    if api_key == requested_api_key:
        return result
    else:
        return unauthorized()


@api.route('/initiate_transaction', methods=['GET'])
def initiate_transaction():
    to_address = request.headers.get('to_address')
    to_satoshis = request.headers.get('to_satoshis')
    coin_symbol = request.headers.get('coin_symbol')
    api_key = request.headers.get('api_key')
    order_id = request.headers.get('order_id')
    
    if coin_symbol == 'btc':
        with open('./deposit_wallet/btc/wallet.json') as json_file:
            data = json.load(json_file)
            from_privkey = data['private']
    if coin_symbol == 'btc-testnet':    
        with open('./deposit_wallet/btc_testnet/wallet.json') as json_file:
            data = json.load(json_file)
            from_privkey = data['private']
    if coin_symbol == 'ltc':
        with open('./deposit_wallet/ltc/wallet.json') as json_file:
            data = json.load(json_file)
            from_privkey = data['private']

    
    #if coin_symbol == 'btc' or 'ltc' or 'btc-testnet':
    try:
        transaction_id = blockcypher.simple_spend(from_privkey=from_privkey, 
                                        to_address=to_address, 
                                        to_satoshis=int(to_satoshis), 
                                        coin_symbol=coin_symbol, 
                                        api_key=blockcypher_api_key, 
                                        privkey_is_compressed=True)
        status = 'Success'
    except:
        status = 'Failure'
    #get current date and time
    current_date = datetime.datetime.now()

    #get transaction fee from tx id
    transaction_output = blockcypher.get_transaction_details(transaction_id,coin_symbol='btc-testnet')
    transaction_fee = float(transaction_output['fees']) / 100000000 #convert satoshi to bitcoin
    if api_key == requested_api_key:
        return {
                "transaction_id": transaction_id,
                "status": status,
                "timestamp": current_date.isoformat(),
                "order_id": order_id,
                "costomers_wallet": to_address,
                "transaction_amount": to_satoshis,
                "transaction_fee": transaction_fee
        }

    else:
        return unauthorized()


@api.route('/calculate_transaction_fee', methods=['GET'])
def calculate_transaction_fee():
    coin_symbol = request.headers.get('coin_symbol')
    api_key = request.headers.get('api_key')
   
    if coin_symbol == 'btc':
        #get btc tx fees, calculate fees by multiplying average tx bytes(400) and divide to btc equivalent
        r = requests.get(url='https://api.blockcypher.com/v1/btc/test3')
        response = r.json()
        btc_high_fee_per_kb = response['high_fee_per_kb']
        btc_medium_fee_per_kb = response['medium_fee_per_kb']
        btc_low_fee_per_kb = response['low_fee_per_kb']
        high_fee = float(btc_high_fee_per_kb) * 0.4 * 0.00000001
        medium_fee = float(btc_medium_fee_per_kb) * 0.4 * 0.00000001
        low_fee = float(btc_low_fee_per_kb) * 0.4 * 0.00000001

    if coin_symbol == 'btc-testnet':
        #get btc tx fees, calculate fees by multiplying average tx bytes(400) and divide to btc equivalent
        r = requests.get(url='https://api.blockcypher.com/v1/btc/main')
        response = r.json()
        btc_high_fee_per_kb = response['high_fee_per_kb']
        btc_medium_fee_per_kb = response['medium_fee_per_kb']
        btc_low_fee_per_kb = response['low_fee_per_kb']
        high_fee = float(btc_high_fee_per_kb) * 0.4 * 0.00000001
        medium_fee = float(btc_medium_fee_per_kb) * 0.4 * 0.00000001
        low_fee = float(btc_low_fee_per_kb) * 0.4 * 0.00000001
    
    if coin_symbol == 'ltc':
        #get ltc tx fees, calculate fees by multiplying average tx bytes(400) and divide to ltc equivalent
        r = requests.get(url='https://api.blockcypher.com/v1/ltc/main')
        response = r.json()
        ltc_high_fee_per_kb = response['high_fee_per_kb']
        ltc_medium_fee_per_kb = response['medium_fee_per_kb']
        ltc_low_fee_per_kb = response['low_fee_per_kb']
        high_fee = float(ltc_high_fee_per_kb) * 0.4 * 0.00000001
        medium_fee = float(ltc_medium_fee_per_kb) * 0.4 * 0.00000001
        low_fee = float(ltc_low_fee_per_kb) * 0.4 * 0.00000001

    #get usd,eur,try prices for conversion
    client = Client('aCOMJtcUCKyMxGcZ9KaUB521MwfjeIXxAIiH0emEE6GwWd4KmRdEobk6eyIoI1lW', 
    '68xBDA81ok4fMx7hTFxCsCx1vk6xGGJpHNetXI3C8c9mqPEmyEG6o91dI9URBuBH')

    #USD-TRY
    usd_try_json = client.get_avg_price(symbol='BUSDTRY')
    usd_try = usd_try_json['price']
    #EUR-TRY
    eur_usd_json = client.get_avg_price(symbol='EURBUSD')
    eur_usd = eur_usd_json['price']
    eur_try = float(eur_usd) * float(usd_try)
    #BTC-USD
    btc_usd_json = client.get_avg_price(symbol='BTCUSDT')
    btc_usd = btc_usd_json['price']

    high_fee_as_usd = high_fee * float(btc_usd)
    medium_fee_as_usd = medium_fee * float(btc_usd)
    low_fee_as_usd = low_fee * float(btc_usd)
    high_fee_as_eur = high_fee * float(btc_usd) / float(eur_usd)
    medium_fee_as_eur = medium_fee * float(btc_usd) / float(eur_usd)
    low_fee_as_eur = low_fee * float(btc_usd) / float(eur_usd)
    high_fee_as_try = high_fee * float(btc_usd) * float(usd_try)
    medium_fee_as_try = high_fee * float(btc_usd) * float(usd_try)
    low_fee_as_try = high_fee * float(btc_usd) * float(usd_try)


    if api_key == requested_api_key:
        return {
                "high_fee": format(high_fee,'.9f'),
                "medium_fee": format(medium_fee,'.9f'),
                "low_fee": format(low_fee,'.9f'),
                "high_fee_as_usd": format(high_fee_as_usd,'.9f'),
                "medium_fee_as_usd": format(medium_fee_as_usd,'.9f'),
                "low_fee_as_usd": format(low_fee_as_usd,'.9f'),
                "high_fee_as_eur": format(high_fee_as_eur,'.9f'),
                "medium_fee_as_eur": format(medium_fee_as_eur,'.9f'),
                "low_fee_as_eur": format(low_fee_as_eur,'.9f'),
                "high_fee_as_try": format(high_fee_as_try,'.9f'),
                "medium_fee_as_try": format(medium_fee_as_try,'.9f'),
                "low_fee_as_try": format(low_fee_as_try,'.9f'),
        }

    else:
        return unauthorized()


@api.route('/check_transaction_confirmation', methods=['GET'])
def check_transaction_confirmation():
    coin_symbol = request.headers.get('coin_symbol')
    address = request.headers.get('address')
    amount = request.headers.get('amount')
    api_key = request.headers.get('api_key')


    if coin_symbol == 'btc' or 'ltc' or 'btc-testnet':
        response = blockcypher.get_address_details(address,coin_symbol=coin_symbol)
        '''
        print (response)
        for txrefs in response.items():
            print (amount)
            
            # for value, confirmations in txrefs.items():
            #    print (value)
                #if value == amount:
                #    result = confirmations 

    '''
    
    else:
        result = '0'   
    #print (confirmations)


    if api_key == requested_api_key:
        return response
    else:
        return unauthorized()


if __name__ == '__main__':
    api.run()
