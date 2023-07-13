import requests
import base64

# Function returns list of decoded transactions if GET status is "200: OK", otherwise returns None
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

# Function adds user-friendly context for transactions
def view_block_transactions(txs_list, block_number):
    if txs_list:
        print("There are", len(txs_list), "transactions in block", block_number)
        for tx in txs_list:
            print(tx)
    else:
        print("Couldn't get transactions from block", block_number)

# Example of both functions on block 11260637
if __name__ == "__main__":
    block_number = 11260637
    transactions = get_block_transactions(block_number)
    view = view_block_transactions(transactions, block_number)
