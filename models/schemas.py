
"""
Due to time constraints I define the schemas here.
There is probably a library where I can serialize/deserialize with a set schema
That will make it more scalable if it was a project
"""


class Transaction():
    def __init__(self, transactionObject):
        self.hash = transactionObject.hash
        self.time = transactionObject.time
        self.size = transactionObject.size

class Address():
    def __init__(self, addressObject):
        self.transactions = addressObject.transactions

class Balance():
    def __init__(self, balanceObject):
        # Grab the first key since it only checks one balance at a time. In the future we would want
        # to grab multiple balances (but not supported by this endpoint currently)
        self.final_balance = balanceObject[next(iter(balanceObject))].final_balance
