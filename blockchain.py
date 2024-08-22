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


def get_transaction_value():
    """Gets transaction amount from the user input."""
    return float(input("Transaction amount: "))


def get_user_choice():
    """Gets user choice to either add a new transaction value or output current blockchain blocks"""
    return input("Your choice: ")


def print_blockchain_elements():
    """Print out elements in blockchain"""
    for block in blockchain:
        print("Outputting Block")
        print(block)


# Get first transaction input and add value to blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print("q: Quit")
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "q":
        break
    else:
        print("Input was invalid, please pick a value from the list!")

print("Done!")
