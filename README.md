# cointracker-project

# Scope of the work
- server-side API that will get the transactions or balances for an address

### GET  /:address/txs
- This endpoint will retrieve the transactions for a given address and can also take in values for limit and offset so that we can page data

### GET /:address/balance
- This endpoint will retrieve the current balance of the given address in BTC

### Assumptions
- can only get one address at a time (the blockchain api allows for getting multiple address balances at one time)
- no rate limiting or security checks are in place for abusive traffic
- the transaction object passes back the hash, time, and size, but other fields may be passed if needed on the frontend
- no schema/data validation is in place (api endpoints may change over time. Even in the blockchain api docs Address's field transactions used be a field called "txs". That name is still present in the docs: https://www.blockchain.com/api/blockchain_api, but it updated to be called "transactions" on the github object field definitions  [blockexplorer.md](https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md))

## Running
Run `./bootstrap.sh` to run the virtual environment and set up the server.

## Examples

### Gives the balance of address 3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd
`curl localhost:5000/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/balance`

```
{"final_balance":3887413}
```

### Gives the transactions of address 3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd
`curl localhost:5000/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/transactions`

```
{"1645033345":{"hash":"df81f02a0bd5d84676c629c6f9d6a2d72ece901b37775c2c3d9325819de5f9ac","size":6088,"time":1645033345},"1645078934":{"hash":"baf95eee366ae45c0cf968ae00026496e908f2b8126f263cb32b1ad6cb785bc9","size":3545,"time":1645078934},"1645134998":{"ha...
```

### Gives the transactions of address 3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd with a limit of 2
`curl "localhost:5000/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/transactions?limit=2"`

```
{"1651450081":{"hash":"c99e6bf98e4d76777e2299da37a7a1cb3d51539501c01c07a80190a9473df3fb","size":5490,"time":1651450081},"1651454148":{"hash":"33dc2f336651a14476363b881cf1d3a60a210c1a44c72db97d8ad9308749ceeb","size":3056,"time":1651454148}}
```

### Gives the transactions of address 3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd with a limit of 4 and offset of 2
`curl "localhost:5000/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/transactions?limit=4&offset=2"`

```
{"1651384320":{"hash":"3b46c1a47067623c9494082f923364f9355a1e097abd8eedd751a7b6aae97ea1","size":3589,"time":1651384320},"1651385732":{"hash":"d064cb63ed1e76d1fd82c56019827b9f9231aa6182518439a2af37a2d0df4841","size":152,"time":1651385732},"1651427975":{"hash":"d707e63c441865a8c21a03f8a6f72e1c0124e0bd7ebc907c5192f27cf4fe1fd0","size":192,"time":1651427975},"1651449540":{"hash":"2b726275b40395b347ab905f751bea3118e532cb19b0a21109216a35e0191ce7","size":5603,"time":1651449540}}
```

### Improvements for future
- Have the Transaction and Address be predefined schemas that can be serialized/deserialized from the Blockchain API. (Instead of manually mapping the values over since the returned results need to be JSON serializable)
- Allow for more parameters to be passed to the endpoint to customize the results further than limit and offset
- time is given as an EPOCH time, could be translated to a human-readable format
- the final balance is given with a few digits of precision, this can tweaked to show it more accurately (3887413 is actually 0.03887413 BTC)
