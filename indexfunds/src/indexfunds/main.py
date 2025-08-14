#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from indexfunds.crew import IndexAdvisorCrew
from indexfunds.test_news import NewsOnlyCrew
# from indexfunds.test_technical import TechnicalOnlyCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your 
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        # "topic": "is the SNP500(^GSPC) good to buy in july 2024 to october 2024?",
        "topic": "is the FTSE 100 (^FTSE) good to buy in january 2025 to june 2025?",
        # "topic": "Based on 2024 to 2025, is the Nikkei 225 (^N225) good to buy?",
        # "topic": " Based on june 2023 to june 2025, is the NASDAQ Composite (^IXIC) good to buy?",
        'current_year': str(datetime.now().year)
    }

    try:
        IndexAdvisorCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()

# def run_news_only():
# 	inputs = {"topic": "is the SNP500(^GSPC) good to buy in july 2023?"}
# 	NewsOnlyCrew().crew().kickoff(inputs=inputs)

# if __name__ == "__main__":
# 	run_news_only()

# main.py


# def run_test_technical():
# 	inputs = {"topic": "^GSPC"}
# 	TechnicalOnlyCrew().crew().kickoff(inputs=inputs)

# if __name__ == "__main__":
# 	run_test_technical()

# run_test_technical()

# test()
# run_news_only()