import streamlit as st
from web3 import Web3


# Initialize Web3
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))  
contract_address = "0x629356703d9B59e37d264cf74c46bE06C29EdB2d"  
contract_abi = """[
	{
		"inputs": [],
		"name": "claimWinnings",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bool",
				"name": "teamAWon",
				"type": "bool"
			}
		],
		"name": "decideOutcome",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bool",
				"name": "forTeamA",
				"type": "bool"
			}
		],
		"name": "placeBet",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bool",
				"name": "open",
				"type": "bool"
			}
		],
		"name": "toggleBetting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_feeRecipient",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "admin",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "betsTeamA",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "betsTeamB",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "bettingOpen",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "feeRecipient",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAdmins",
		"outputs": [
			{
				"internalType": "address",
				"name": "contractAdmin",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "feeReceiver",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "bettor",
				"type": "address"
			}
		],
		"name": "getBetDetails",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "betTeamA",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "betTeamB",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOutcome",
		"outputs": [
			{
				"internalType": "enum Betting.Outcome",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalBets",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "totalBetsA",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "totalBetsB",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "outcome",
		"outputs": [
			{
				"internalType": "enum Betting.Outcome",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalBetsTeamA",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalBetsTeamB",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]""" 

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

st.title('Betting App')
st.sidebar.write("Please connect with your Ethereum Private Key")
private_key = st.sidebar.text_input('Your Ethereum Private Key', type="password") 

if private_key:
    try:
        account = w3.eth.account.privateKeyToAccount(private_key).address
        st.sidebar.write(f"Connected Wallet Address: **{account}**")
    except:
        st.sidebar.error("Invalid private key!")
        account = None
else:
    account = None

bet_team = st.radio("Select Team to Bet On", ["Team A", "Team B"])
amount = st.text_input('Bet Amount (ETH)', "0.1")

# Fetch contract data
outcome_map = {0: "Pending", 1: "Team A Won", 2: "Team B Won"}
outcome = contract.functions.getOutcome().call()

# Display outcome
if outcome == 0:
    st.write(f"**Outcome:** {outcome_map[outcome]}")
else:
    st.markdown(f"<span style='color:red'>**Outcome:** {outcome_map[outcome]}</span>", unsafe_allow_html=True)

total_bets_teamA = w3.fromWei(contract.functions.getTotalBets().call()[0], 'ether')
total_bets_teamB = w3.fromWei(contract.functions.getTotalBets().call()[1], 'ether')
contract_balance = w3.fromWei(w3.eth.getBalance(contract_address), 'ether')

# Odds calculation
if total_bets_teamA == 0 or total_bets_teamB == 0:
    st.warning("Odds cannot be calculated yet.")
    odds_teamA = odds_teamB = 0.0  
else:
    odds_teamA = float(total_bets_teamB) / float(total_bets_teamA)  # Convert to float
    odds_teamB = float(total_bets_teamA) / float(total_bets_teamB)  # Convert to float

# Expected payout
try:
    bet_amount_eth = float(amount)
    
    if bet_team == "Team A":
        raw_payout = bet_amount_eth * odds_teamA
        # The maximum payout is limited by the funds of Team B
        expected_payout = min(raw_payout, total_bets_teamB)
    else:
        raw_payout = bet_amount_eth * odds_teamB
        # The maximum payout is limited by the funds of Team A
        expected_payout = min(raw_payout, total_bets_teamA)
except ValueError:
    expected_payout = 0

st.write(f"**Contract Balance:** {contract_balance} ETH")
st.write(f"**Total Bets for Team A:** {total_bets_teamA} ETH")
st.write(f"**Total Bets for Team B:** {total_bets_teamB} ETH")
st.write(f"**Odds for Team A:** {odds_teamA:0.2f}")
st.write(f"**Odds for Team B:** {odds_teamB:0.2f}")

if st.button("Place Bet") and account:
    nonce = w3.eth.getTransactionCount(account)
    if bet_team == "Team A":
        tx = contract.functions.placeBet(True).buildTransaction({
            'from': account,
            'value': w3.toWei(amount, 'ether'),
            'gas': 2000000,  
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': nonce,
        })
    else:
        tx = contract.functions.placeBet(False).buildTransaction({
            'from': account,
            'value': w3.toWei(amount, 'ether'),
            'gas': 2000000,  
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': nonce,
        })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    st.write(f"Transaction Hash: {tx_hash.hex()}")
    st.success("Bet placed successfully!")

st.markdown(f"<span style='color:green'>**Expected Payout (if you win):** {expected_payout:0.2f} ETH</span>", unsafe_allow_html=True)


if st.button("Claim Winnings") and account:
    nonce = w3.eth.getTransactionCount(account)
    tx = contract.functions.claimWinnings().buildTransaction({
        'from': account,
        'gas': 2000000,  
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': nonce,
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    st.write(f"Transaction Hash: {tx_hash.hex()}")
    st.success("Winnings claimed successfully!")


if __name__ == '__main__':
    st.write("Developed using Streamlit and web3.py")
