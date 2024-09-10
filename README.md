# Ethereum Deposit Tracker

## Overview

The Ethereum Deposit Tracker is a Python application designed to monitor and record ETH deposits on the Beacon Deposit Contract. It connects to the Ethereum blockchain, tracks deposit transactions, logs the details, and can optionally send notifications via Telegram and visualize data using Grafana.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Error Handling](#error-handling)
7. [Troubleshooting](#troubleshooting)

## Features

- Connects to Ethereum RPC using Alchemy.
- Monitors Beacon Deposit Contract for ETH deposits.
- Logs deposit details including amount, sender address, and timestamp.
- Optionally sends notifications via Telegram.
- (Optional) Visualizes deposit data using Grafana.

## Prerequisites

- Python 3.7+
- `web3` library
- `python-telegram-bot` library (for Telegram notifications)
- Access to Alchemy or another Ethereum RPC provider


## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ahana-dubey/ethereum-deposit-tracker.git
   cd ethereum-deposit-tracker
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


## Configuration

1. **Set Up Environment Variables:**

   Create a `.env` file in the project directory with the following content:

   ```
   TELEGRAM_TOKEN=your-telegram-bot-token
   CHAT_ID=your-chat-id
   ALCHEMY_API_KEY=your-alchemy-api-key
   BEACON_DEPOSIT_CONTRACT=0x00000000219ab540356cBB839Cbe05303d7705Fa
   ```

2. **Example `.env` File:**

   ```
   TELEGRAM_TOKEN=123456789:ABCdefGHIjklMNOpQRstuvWXYz
   CHAT_ID=123456789
   ALCHEMY_API_KEY=your-alchemy-api-key
   BEACON_DEPOSIT_CONTRACT=0x00000000219ab540356cBB839Cbe05303d7705Fa
   ```

## Usage

1. **Run the Tracker:**

   ```bash
   python tracker.py
   ```


## Optional Features

1. **Telegram Notifications:**

   If you want to receive notifications for new deposits:

   - Ensure you have set up your Telegram bot and chat ID as described in the [Telegram Notifications](#telegram-notifications) section.
   - The script will send a notification to your Telegram chat when a new deposit is detected.

2. **Grafana Dashboard:**

   - Set up a Grafana dashboard to visualize deposit data by configuring a data source and creating graphs or tables.

## Documentation

- **Script Details:**

  - `tracker.py`: Main script to connect to Ethereum, track deposits, and log data.
  - `logging_config.py`: Configures logging settings.

- **API Endpoints:**

  - `GET /getUpdates`: Fetches updates from Telegram to find chat ID.
  - `POST /sendMessage`: Sends messages via the Telegram bot.

## Error Handling

- **Network Errors:**

  Ensure you have a stable internet connection and that the RPC endpoint is accessible.

- **API Errors:**

  Check the log file for detailed error messages if the bot fails to send notifications or if the RPC connection encounters issues.

- **Incorrect Configuration:**

  Verify that all environment variables are set correctly and that the API keys and chat IDs are accurate.

## Troubleshooting

1. **Bot Not Sending Messages:**

   - Verify the bot token and chat ID.
   - Check network connectivity and Telegram API limits.

2. **No Deposit Data Recorded:**

   - Ensure the Beacon Deposit Contract address is correct.
   - Check for any issues with the Ethereum RPC connection.

