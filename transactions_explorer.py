import requests
import base64

def get_block_transactions(block_number):
    base_url = "https://akash-mainnet-rpc.cosmonautstakes.com/block?height="
    url = base_url + str(block_number)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        txs = data.get("result",{}).get("block", {}).get("data", {}).get("txs", [])
        decoded_txs = []
        for tx in txs:
            decoded_tx = base64.b64decode(tx)
            decoded_txs.append(decoded_tx)
        return decoded_txs
    else:
        return None

# Example of function's usage on block 11260637
block_number = 11260637
transactions = get_block_transactions(block_number)
if transactions:
    for tx in transactions:
        print(tx)
else:
    print("No transactions in block", block_number)
