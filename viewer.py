from transactions import get_block_transactions, view_block_transactions

while True:
    enter_block_number = input("Enter <int> block number from AKASH blockchain or any <str> to exit: ")
    if enter_block_number.isdigit():
        block_number = int(enter_block_number)
        transactions = get_block_transactions(block_number)
        view = view_block_transactions(transactions, block_number)
    else:
        break
