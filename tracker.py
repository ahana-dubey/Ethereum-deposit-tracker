from web3 import Web3
from telegram import Bot
import time
import logging

alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/0n6xxxxxxxxXYwRHj-hPvxxxxxxv39"

web3 = Web3(Web3.HTTPProvider(alchemy_url))

if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Connection failed")

beacon_deposit_contract = '0x00000000219ab540356cBB839Cbe05303d7705Fa'

def fetch_block_transactions(block_number):
    block = web3.eth.get_block(block_number, full_transactions=True)
    for tx in block.transactions:
        if tx['to'] == beacon_deposit_contract:
            print(f"ETH Deposit Detected in Transaction: {tx['hash'].hex()}")
            print(f"Sender: {tx['from']}, Amount: {web3.from_wei(tx['value'], 'ether')} ETH")

latest_block = web3.eth.block_number
print(f"Latest Block Number: {latest_block}")

block = web3.eth.get_block(latest_block, full_transactions=True)
print(f"Block {latest_block} Details: {block}")


def track_deposits():
    last_checked_block = web3.eth.block_number

    while True:
        latest_block = web3.eth.block_number

        if latest_block > last_checked_block:
            for block_number in range(last_checked_block + 1, latest_block + 1):
                block = web3.eth.get_block(block_number, full_transactions=True)
                for tx in block.transactions:
                    if tx['to'] == beacon_deposit_contract:
                        print(f"ETH Deposit Detected in Block {block_number}: {tx['hash'].hex()}")
                        print(f"Sender: {tx['from']}, Amount: {web3.from_wei(tx['value'], 'ether')} ETH")
            last_checked_block = latest_block

        time.sleep(10) 

track_deposits()

deposits = []

def save_deposit(tx, block):
    deposit = {
        'blockNumber': block['number'],
        'blockTimestamp': block['timestamp'],
        'fee': web3.from_wei(tx['gasPrice'] * tx['gas'], 'ether'),
        'hash': tx['hash'].hex(),
        'sender': tx['from'],
        'amount': web3.from_wei(tx['value'], 'ether')
    }
    deposits.append(deposit)
    print(f"Deposit saved: {deposit}")

logging.basicConfig(level=logging.INFO)

def track_deposits():
    last_checked_block = web3.eth.block_number

    while True:
        try:
            latest_block = web3.eth.block_number

            if latest_block > last_checked_block:
                for block_number in range(last_checked_block + 1, latest_block + 1):
                    block = web3.eth.get_block(block_number, full_transactions=True)
                    for tx in block.transactions:
                        if tx['to'] == beacon_deposit_contract:
                            save_deposit(tx, block)
                last_checked_block = latest_block
        except Exception as e:
            logging.error(f"Error fetching block data: {e}")

        time.sleep(10)

logging.basicConfig(
    filename='deposit_tracker.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TELEGRAM_TOKEN = '7xxxxxxx17:AxxxxxxxxxxMHI-rX4xxxxxxxxxxxx5qfY'
CHAT_ID = '13xxxxxx6'

# Initialize the bot
bot = Bot(token=TELEGRAM_TOKEN)

def send_telegram_message(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")
    # bot.sendMessage(chat_id=CHAT_ID, text=message)

def save_deposit(tx, block):
    deposit = {
        'blockNumber': block['number'],
        'blockTimestamp': block['timestamp'],
        'fee': web3.from_wei(tx['gasPrice'] * tx['gas'], 'ether'),
        'hash': tx['hash'].hex(),
        'sender': tx['from'],
        'amount': web3.from_wei(tx['value'], 'ether')
    }
    logging.info(f"Deposit saved: {deposit}")

    # Send Telegram alert
    message = (f"New ETH Deposit Detected!\n"
               f"Block Number: {deposit['blockNumber']}\n"
               f"Timestamp: {deposit['blockTimestamp']}\n"
               f"Sender: {deposit['sender']}\n"
               f"Amount: {deposit['amount']} ETH\n"
               f"Transaction Hash: {deposit['hash']}")
    send_telegram_message(message)