from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/<int:address>/balance', methods=['GET'])
def get_balance(address):
    pass


@app.route('/<int:address>/transactions', methods=['GET'])
def get_transactions(address):
  pass
