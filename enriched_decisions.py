from web3 import Web3
import math
import numpy as np
import requests

provider=Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/"))
pair_abi="""[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""
address="0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"
address_eoa="0x7bD045aB0AEe760130047432007E035266B63E1c"
usdc_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

def get_usd_value(token):
    formatted_address="ethereum:"+token
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return int(value["coins"][formatted_address]['price'])

def decode_approval(etherscan_txn):
    approver=etherscan_txn['from']
    token_address=etherscan_txn['to']
    input_data=etherscan_txn['input']
    spender=input_data[34:74]
    amount=int(input_data[74:],16)
    return {'approver':approver,'token_address':token_address,'spender':spender,'amount':amount}

def is_less_than_equal_volatility(provider,pair_address,pair_abi,block_depth,threshold):
    w3 = provider
    pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)
    prices = []
    latest_block = w3.eth.block_number

    for block in range(latest_block - (block_depth-1), latest_block):
        # Get reserves
        reserves = pair_contract.functions.getReserves().call(block_identifier=block)

        # Calculate price (reserve1 / reserve0)
        price = reserves[1] / reserves[0]

        prices.append(price)

    log_returns = [math.log(price / prices[i - 1]) for i, price in enumerate(prices)]
    return np.std(log_returns)<=threshold

def is_less_than_volatility(provider,pair_address,pair_abi,block_depth,threshold):
    w3 = provider
    pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)
    prices = []
    latest_block = w3.eth.block_number

    for block in range(latest_block - (block_depth-1), latest_block):
        # Get reserves
        reserves = pair_contract.functions.getReserves().call(block_identifier=block)

        # Calculate price (reserve1 / reserve0)
        price = reserves[1] / reserves[0]

        prices.append(price)

    log_returns = [math.log(price / prices[i - 1]) for i, price in enumerate(prices)]
    return np.std(log_returns)<threshold

def is_greater_than_equal_volatility(provider,pair_address,pair_abi,block_depth,threshold):
    w3 = provider
    pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)
    prices = []
    latest_block = w3.eth.block_number

    for block in range(latest_block - (block_depth-1), latest_block):
        # Get reserves
        reserves = pair_contract.functions.getReserves().call(block_identifier=block)

        # Calculate price (reserve1 / reserve0)
        price = reserves[1] / reserves[0]

        prices.append(price)

    log_returns = [math.log(price / prices[i - 1]) for i, price in enumerate(prices)]
    return np.std(log_returns)>=threshold

def is_greater_than_volatility(provider,pair_address,pair_abi,block_depth,threshold):
    w3 = provider
    pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)
    prices = []
    latest_block = w3.eth.block_number

    for block in range(latest_block - (block_depth-1), latest_block):
        # Get reserves
        reserves = pair_contract.functions.getReserves().call(block_identifier=block)

        # Calculate price (reserve1 / reserve0)
        price = reserves[1] / reserves[0]

        prices.append(price)

    log_returns = [math.log(price / prices[i - 1]) for i, price in enumerate(prices)]
    return np.std(log_returns)>threshold

#print(is_under_volatility(provider,address,pair_abi,100,0.5))

def is_externally_owned_account(provider,address):
    code=provider.eth.get_code(Web3.to_checksum_address(address)).hex()
    return code=="0x"

# print(is_externally_owned_account(provider,address))

def is_less_than_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']<usd_threshold

def is_less_than_equal_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']<=usd_threshold

def is_greater_than_equal_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']>=usd_threshold

def is_greater_than_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']>usd_threshold

def is_equal_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']==usd_threshold

def is_not_equal_usd_value(address,usd_threshold):
    formatted_address="ethereum:"+address
    value=requests.get(f"https://coins.llama.fi/prices/current/{formatted_address}".format(formatted_address)).json()
    return value["coins"][formatted_address]['price']!=usd_threshold

#print(is_less_than_usd_value(usdc_address,5))
def exceeds_max_concurrent_approval_count_on_token(your_address,token_address,max_concurrent_approvals,etherscan_api_key):
    payload=f"https://api.etherscan.io/api?module=account&sort=dsc&action=txlist&address={your_address}&apikey={etherscan_api_key}".format(your_address,etherscan_api_key)
    txns=requests.get(payload).json()['result']
    spenders=[]
    for txn in txns:
        if txn['isError']=="1":
            continue
        if txn['to']!=token_address:
            continue
        if txn['functionName']!='approve(address _spender, uint256 _value)':
            continue
        spender=decode_approval(txn)["spender"].lower()
        if spender in spenders:
            continue
        spenders.append(spender)
        if len(spenders)>=max_concurrent_approvals:
            return True
    return False

def exceeds_max_concurrent_approval_count(your_address,max_concurrent_approvals,etherscan_api_key):
    payload=f"https://api.etherscan.io/api?module=account&action=txlist&sort=dsc&address={your_address}&apikey={etherscan_api_key}".format(your_address,etherscan_api_key)
    txns=requests.get(payload).json()['result']
    spenders=[]
    for txn in txns:
        if txn['isError']=="1":
            continue
        if txn['functionName']!='approve(address _spender, uint256 _value)':
            continue
        spender=decode_approval(txn)["spender"].lower()
        if spender in spenders:
            continue
        spenders.append(spender)
        if len(spenders)>=max_concurrent_approvals:
            return True
    return False

def exceeds_max_cumulative_approval_amount_on_token(your_address,token_address,amount_to_approve,max_amount,in_usd,etherscan_api_key):
    if amount_to_approve>=max_amount:
        return True
    payload=f"https://api.etherscan.io/api?module=account&sort=dsc&action=txlist&address={your_address}&apikey={etherscan_api_key}".format(your_address,etherscan_api_key)
    txns=requests.get(payload).json()['result']
    spenders=[]
    amount=0
    if in_usd:
        usd_value=get_usd_value(token_address)
    else:
        usd_value=1

    for txn in txns:
        if txn['isError']=="1":
            continue
        if txn['to']!=token_address:
            continue
        if txn['functionName']!='approve(address _spender, uint256 _value)':
            continue
        decoded=decode_approval(txn)
        spender=decoded["spender"].lower()
        if spender in spenders:
            continue
        spenders.append(spender)
        amount+=decoded['amount']
        if (usd_value*amount)+amount_to_approve>max_amount:
            return True
    return False

def exceeds_max_cumulative_approval_amount_usd(your_address,amount_to_approve,max_amount,etherscan_api_key):
    
    #I've only built this function with only usd value to have continuity over all assets
    if amount_to_approve>=max_amount:
        return True
    payload=f"https://api.etherscan.io/api?module=account&action=txlist&sort=dsc&address={your_address}&apikey={etherscan_api_key}".format(your_address,etherscan_api_key)
    txns=requests.get(payload).json()['result']
    unique_approvals={}
    amount=0

    for txn in txns:
        if txn['isError']=="1":
            continue
        if txn['functionName']!='approve(address _spender, uint256 _value)':
            continue
        decoded=decode_approval(txn)
        spender=decoded["spender"].lower()

        if txn['to'] in unique_approvals.keys() and spender in unique_approvals['to']:
            continue
        if txn['to'] in unique_approvals.keys():
            unique_approvals['to'].append(spender)
        else:
            unique_approvals['to']=[spender]
        amount+=decoded['amount']*get_usd_value(txn['to'])
        if amount+amount_to_approve>max_amount:
            return True
    return False

print(exceeds_max_cumulative_approval_amount_usd(address_eoa,5,"PGJ5AYE9WGD77YPS4F3NGQ33MB5YI7JYS8"))