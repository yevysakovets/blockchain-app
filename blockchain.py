"""
This file provides the baseline for the blockchain app.
"""

blockchain = []
open_transactions = []
owner = 'Zhenya'


def get_last_blockchain_value():
    """Returns the last value in the blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient,sender=owner, amount=1.0):
    # Append a new transaction to the open_transactions

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    # TODO add logic to append to blockchain
    pass


def get_transaction_value():
    """Return a tuple containing recipient and transaction amount."""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input("Transaction amount: "))
    return tx_recipient, tx_amount


def get_user_choice():
    """Gets user choice to either add a new transaction value or output current blockchain blocks"""
    return input("Your choice: ")


def print_blockchain_elements():
    """Print out elements in blockchain"""
    for block in blockchain:
        print('Outputting Block')
        print(block)
    print("-" * 20)
    print("-" * 20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break


print('Done!')
