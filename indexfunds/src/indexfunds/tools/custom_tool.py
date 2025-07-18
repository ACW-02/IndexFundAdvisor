from crewai.tools import BaseTool
import yfinance as yf
import pandas as pd
from fredapi import Fred
# from newsapi import NewsApiClient
# from datetime import datetime,timedelta
# from dotenv import load_dotenv 
# from crewai_tools.tools import ScrapeWebsiteTool
# import requests
# import os   

# - evaluasi scenario per time frame
# - custom toolsnya bermasalah di news dan technical
# - find a way to save and load model to FastAPI
# - custom tool yang macro economy (sus) (harusnya bener karena beberapa index terpengaruh oleh 1 negara)

#newsapi key = f409f399e97e429ca9d22a0b805cc633

# -----------------------------------------------------------------------------


class IndexTechnicalTool(BaseTool):
    name: str = "IndexTechnicalTool"
    description: str = "Fetches recent technical indicators (SMA, RSI) for a given stock index using yfinance."

    def _run(self, ticker: str) -> str:
        try:
            df = yf.download(ticker, period="3mo", interval="1d", auto_adjust=True)
            if df.empty:
                return f"❌ No historical price data found for {ticker}. Check if the ticker is correct."

            if len(df) < 20:
                return f"⚠️ Only {len(df)} data points found for {ticker}. Not enough to compute 20-day SMA or RSI(14)."

            # Calculate SMA
            df["SMA_20"] = df["Close"].rolling(window=20).mean()

            # Calculate RSI
            delta = df["Close"].diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            avg_gain = gain.rolling(window=14).mean()
            avg_loss = loss.rolling(window=14).mean()
            rs = avg_gain / avg_loss
            df["RSI_14"] = 100 - (100 / (1 + rs))

            # Select latest scalar values using `.iloc[-1].item()`
            close_price = df["Close"].iloc[-1].item()
            sma_20 = df["SMA_20"].iloc[-1]
            rsi_14 = df["RSI_14"].iloc[-1]

            response = f"📈 Technical Overview for {ticker}:\n\n"
            response += f"- Current Price: {round(close_price, 2)}\n"
            response += f"- 20-Day SMA: {round(sma_20, 2) if pd.notnull(sma_20) else 'N/A'}\n"
            response += f"- RSI (14): {round(rsi_14, 2) if pd.notnull(rsi_14) else 'N/A'}"

            return response

        except Exception as e:
            return f"❌ Error fetching technical data for {ticker}: {str(e)}"
        
        
class MacroeconomicIndicatorTool(BaseTool):
    name: str = "MacroeconomicIndicatorTool"
    description: str = "Retrieves macroeconomic indicators such as GDP, inflation, unemployment, and interest rates using the FRED API."

    def _run(self, topic: str) -> str:
        # Define the API key directly inside the function
        api_key = "3a40f1089a3adf330f0b9c5f1aff24c6"
        fred = Fred(api_key=api_key)

        indicators = {
            'GDP': 'GDP',
            'Unemployment Rate': 'UNRATE',
            'Inflation (CPI)': 'CPIAUCSL',
            'Fed Funds Rate': 'FEDFUNDS',
            '10-Year Treasury': 'GS10'
        }

        try:
            report = f"📊 Macroeconomic Overview for {topic}:\n\n"
            for name, code in indicators.items():
                data = fred.get_series(code).dropna()
                latest_date = data.index[-1].strftime("%Y-%m-%d")
                latest_value = round(data.iloc[-1], 2)
                report += f"- **{name}** ({code}): {latest_value} (as of {latest_date})\n"
            
            return report

        except Exception as e:
            return f"Failed to fetch macroeconomic data: {str(e)}"
