# Implied Volatility Trading Dashboard

This project provides a Python-based desktop dashboard to visualize and analyze implied volatility (IV) data using the Interactive Brokers (IB) API.

---

## Requirements
- Python 3.10 or higher  
- Anaconda or virtual environment recommended  
- Interactive Brokers Trader Workstation (TWS) or IB Gateway must be running  
- An IBKR Paper or Live account  

---

## Setup

1. Clone the repository

   ```bash
   git clone <repo-url>
   cd "Quant-Guild-Library/2025 Video Lectures/41. How to Build a Volatility Trading Dashboard in Python with Interactive Brokers"
   ```

2. Create the environment

   ```bash
   conda env create -f environment.yaml
   conda activate volatility-dashboard-env
   ```

3. Start the Interactive Brokers trading workspace  
   - Launch Trader Workstation (TWS) or IB Gateway  
   - Go to:  
     `Edit → Global Configuration → API → Settings`  
   - Check Enable ActiveX and Socket Clients  
   - Note the Port number (default: 7497)  
   - Ensure Trusted IPs includes 127.0.0.1  

---

## Running the Dashboard

1. Activate the environment:

   ```bash
   conda activate volatility-dashboard-env
   ```

2. Run the dashboard:

   ```bash
   python dashboard.py
   ```

3. In the dashboard:  
   - Click Connect to link with TWS  
   - Enter a stock symbol (e.g., SPY) and duration (e.g., 2 Y)  
   - Click Query IV Data  
   - After data loads, click Analyze Implied Vol  

---

## Notes
- Make sure TWS is logged in and running before connecting.  
- If you face connection errors, verify your host (127.0.0.1) and port (7497).  
- The dashboard may take several seconds to load data depending on IB’s response time.  

---