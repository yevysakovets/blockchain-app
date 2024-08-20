"""
This file provides the baseline for the blockchain app
"""
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ append new value as well as last blockchain value to the blockchain

    Arguments:
        :transaction_amount: amount that should be added
        :last_transaction: last blockchain transaction (default is [1]
    """

    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input("Transaction amount: "))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
