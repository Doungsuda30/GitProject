import json
from web3 import Web3

def web3_init():
# Fill in your infura API key here
	url = 'http://127.0.0.1:7545'
	web3 = Web3(Web3.HTTPProvider(url))

	abi = json.loads("""
	[
		{
			"inputs": [
				{
					"internalType": "address",
					"name": "id",
					"type": "address"
				},
				{
					"internalType": "uint256",
					"name": "HN",
					"type": "uint256"
				},
				{
					"internalType": "string",
					"name": "name",
					"type": "string"
				}
			],
			"name": "addPatient",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "address",
					"name": "id",
					"type": "address"
				},
				{
					"internalType": "string",
					"name": "temp",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "hr",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "spo2",
					"type": "string"
				}
			],
			"name": "addVitalSign",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "address",
					"name": "id",
					"type": "address"
				}
			],
			"name": "getPatient",
			"outputs": [
				{
					"internalType": "uint256",
					"name": "",
					"type": "uint256"
				},
				{
					"internalType": "string",
					"name": "",
					"type": "string"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "address",
					"name": "id",
					"type": "address"
				}
			],
			"name": "getVitalsign",
			"outputs": [
				{
					"components": [
						{
							"internalType": "address",
							"name": "ID",
							"type": "address"
						},
						{
							"internalType": "string",
							"name": "temp",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "hr",
							"type": "string"
						},
						{
							"internalType": "string",
							"name": "spo2",
							"type": "string"
						},
						{
							"internalType": "uint256",
							"name": "time",
							"type": "uint256"
						}
					],
					"internalType": "struct CovidPatients.VitalSign[]",
					"name": "",
					"type": "tuple[]"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "owner",
			"outputs": [
				{
					"internalType": "address",
					"name": "",
					"type": "address"
				}
			],
			"stateMutability": "view",
			"type": "function"
		}
	]
	""")

	pt_address = "0xBCE699Ea4B5b4d8600208052648540Fc24Da4Cc1"

	abi_address = "0xfaf1F8a0Ef876218E92560Daf53a5F83089BFab8"
	web3.eth.defaultAccount = web3.eth.accounts[0]
	contract = web3.eth.contract(address=abi_address, abi=abi)

	pt_info = contract.functions.getPatient(pt_address).call()

	ret_data = contract.functions.getVitalsign(pt_address).call()

	#print(pt_info)
	#print(ret_data[1])

	str_pt = """
		{
			"name" : "-",
			"HN" : 0,
			"address": "-",
			"data" :[]
		}
	"""

	json_pt = json.loads(str_pt)
	json_pt['name'] = pt_info[1]
	json_pt['HN'] = pt_info[0]
	json_pt['address'] = pt_address

	for i in ret_data:
		print(i)
		vs = """
		{
					"timestamp" : 1675503501,
					"temperature" : 37.0,
					"heartrate" : 120,
					"spo2" : 99.0
		}
		"""
		json_vs = json.loads(vs)
		json_vs['temperature'] = i[1]
		json_vs['heartrate'] = i[2]
		json_vs['spo2'] = i[3]
		json_vs['timestamp'] = i[4]
		json_pt['data'].append(json_vs)
	print(json_pt)

print (web3_init())

#tx_hash = contract.functions.getVitalsign(pt_address).transact()
# Wait for transaction to be mined
#print(tx_hash)
#web3.eth.waitForTransactionReceipt(tx_hash)
