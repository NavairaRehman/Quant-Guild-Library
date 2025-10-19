# from ibapi.client import EClient
# from ibapi.wrapper import EWrapper
# import threading
# import time

# class IBTestApp(EWrapper, EClient):
#     def __init__(self):
#         EClient.__init__(self, self)
#         self.connected_flag = False

#     def nextValidId(self, orderId):
#         print("✅ Connected to IBKR API")
#         self.connected_flag = True

#     def error(self, reqId, code, msg):
#         print(f"⚠️ Error {code}: {msg}")

# def run_loop(app):
#     app.run()

# # --- Main test ---
# app = IBTestApp()
# app.connect("127.0.0.1", 7497, clientId=1)  # Paper trading port = 7497

# # Run the API in a background thread
# thread = threading.Thread(target=run_loop, args=(app,), daemon=True)
# thread.start()

# # Wait for up to 5 seconds for connection confirmation
# for _ in range(50):
#     if app.connected_flag:
#         break
#     time.sleep(0.1)

# if app.connected_flag:
#     print("Connection successful!")
# else:
#     print("Failed to connect. Check TWS API settings or port.")

# app.disconnect()

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def historicalData(self, reqId, bar):
        print(f"{bar.date} | Open: {bar.open}, Close: {bar.close}")

app = TestApp()
app.connect("127.0.0.1", 7497, 1)

def run_loop(): app.run()
thread = threading.Thread(target=run_loop, daemon=True)
thread.start()

# Create a contract for SPY
contract = Contract()
contract.symbol = "SPY"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"

# Request 1 week of historical data
app.reqHistoricalData(
    reqId=1,
    contract=contract,
    endDateTime="",
    durationStr="1 W",
    barSizeSetting="1 day",
    whatToShow="MIDPOINT",
    useRTH=1,
    formatDate=1,
    keepUpToDate=False,
    chartOptions=[]
)

time.sleep(5)
app.disconnect()