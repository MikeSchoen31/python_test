# US 3-Star News Notifier

This small application fetches the daily high impact ("3 étoiles") economic news for the United States using the [TradingEconomics API](https://tradingeconomics.com/api/), and displays them in a window. The application is intended to be launched automatically at Windows logon.

## Requirements

- Python 3.8+
- `requests` library

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script manually:

```bash
python fetch_news.py
```

A small window will appear listing today's high impact US news events.

## Start at Windows logon

To start the application when you sign into Windows:

1. Create a batch file `run_news.bat` with the following content (adjust the Python path if needed):

    ```bat
    @echo off
    python "C:\path\to\project\fetch_news.py"
    ```

2. Press `Win + R`, type `shell:startup` and press Enter. Copy the batch file into the folder that opens. The script will now run automatically whenever you sign in.

