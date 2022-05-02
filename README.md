# cointracker-project

# Scope of the work
- server-side API that will get the transactions or balances for an address

### GET  /:address/txs
- This endpoint will retrieve the transactions for a given address and can also take in values for limit and offset so that we can page data

### GET /:address/balance
- This endpoint will retrieve the current balance of the given address in BTC


## Running

Run `./bootstrap.sh` to run the virtual environment and set up the server.
