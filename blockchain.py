"""
This file provides the baseline for the blockchain app.
"""

blockchain = []


def get_last_blockchain_value():
    """Returns the last value in the blockchain."""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """Append a new transaction to the blockchain.

    Arguments:
        transaction_amount: The amount that should be added.
        last_transaction: The last blockchain transaction. Defaults to the first transaction [1].
    """

    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """Gets transaction amount from the user input."""
    return float(input("Transaction amount: "))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
