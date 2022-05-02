from flask import Flask, jsonify, request
from models.schemas import Address, Transaction, Balance
from blockchain import blockexplorer
app = Flask(__name__)

def convertToTransactionJSONSerializable(transactionObject):
    return dict(hash=transactionObject.hash, time=transactionObject.time, size=transactionObject.size)

@app.route('/<string:address>/balance', methods=['GET'])
def get_balance(address):
    balance = Balance(blockexplorer.get_balance(address))
    return jsonify(dict(final_balance=balance.final_balance))

@app.route('/<string:address>/transactions', methods=['GET'])
def get_transactions(address):
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    address = Address(blockexplorer.get_address(address, limit=limit, offset=offset))

    transactions = {}
    for transaction in address.transactions:
        transactions[transaction.time] = convertToTransactionJSONSerializable(Transaction(transaction))
    return jsonify(transactions)
