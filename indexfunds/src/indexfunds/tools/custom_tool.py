from crewai.tools import BaseTool
from crewai_tools.tools import ScrapeWebsiteTool
from fredapi import Fred
from dotenv import load_dotenv 
import requests
import os

class IndexNewsTool(BaseTool):
    name: str = "IndexNewsTool"
    description: str = "Scrapes and summarizes recent financial news from Yahoo Finance for a given index."

    def _run(self, index_name: str) -> str:
        news_tool = ScrapeWebsiteTool(website_url="https://finance.yahoo.com")
        try:
            scraped_data = news_tool.run(index_name)
            return f"News headlines extracted for {index_name}: {scraped_data}"
        except Exception as e:
            return f"Failed to scrape Yahoo Finance news for {index_name}: {str(e)}"

class IndexTechnicalTool(BaseTool):
    name: str = "IndexTechnicalTool"
    description: str = "Scrapes technical chart data for a given index from Yahoo Finance."

    def _run(self, index_name: str) -> str:
        chart_tool = ScrapeWebsiteTool(website_url="https://finance.yahoo.com")
        try:
            scraped_data = chart_tool.run(index_name)
            return f"Technical chart trends extracted for {index_name}: {scraped_data}"
        except Exception as e:
            return f"Failed to scrape Yahoo Finance charts for {index_name}: {str(e)}"
        

# This tool would fetch macroeconomic data for a given country from FRED
# For example, if the input is "United States", it would fetch GDP, inflation, unemployment rates, etc.
# This is a placeholder tool, replace with actual FRED API calls & key

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
