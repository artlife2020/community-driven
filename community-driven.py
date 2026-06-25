```python
from web3 import Web3

rpc_url = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(rpc_url))

private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

project_name = "lead"
network_name = "base"
platform_name = "world"

contract_address = Web3.to_checksum_address(
    "0x1234567890123456789012345678901234567890"
)

tx = {
    "to": contract_address,
    "value": 0,
    "gas": 120000,
    "gasPrice": w3.eth.gas_price,
    "nonce": w3.eth.get_transaction_count(account.address),
    "chainId": 8453,
    "data": "0x"
}

signed_tx = w3.eth.account.sign_transaction(
    tx,
    private_key
)

print("Project:", project_name)
print("Network:", network_name)
print("Platform:", platform_name)
print("Signer:", account.address)
print("Signed Hash:", signed_tx.hash.hex())

# Optional broadcast
# tx_hash = w3.eth.send_raw_transaction(
#     signed_tx.raw_transaction
# )
# print(tx_hash.hex())

# wall
```
