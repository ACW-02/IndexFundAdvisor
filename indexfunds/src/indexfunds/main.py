#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from indexfunds.crew import IndexAdvisorCrew
# from indexfunds.test_news import NewsOnlyCrew
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
        "topic": "is the SNP500(^GSPC) good to buy in july 2023?",
        # "topic": "is the SRI-KEHATI (SRI-KEHATI.JK) good to buy in febuary 2024?",
        # "topic": "During the period of 2023-2024, is the IDX LQ45 (^JKLQ45) good to buy?",
        # "topic": " Based on the last 2 years, is the SET_SET Index (^SET.BK) good to buy now?",
        'current_year': str(datetime.now().year)
    }

    try:
        IndexAdvisorCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "is the SRI-KEHATI (SRI-KEHATI.JK) good to buy?",
        "topic": "is the IDX LQ45 (^JKLQ45) good to buy?",
        "topic": "is the Japanese Yen Currency Index (^XDN) good to buy?",
        'current_year': str(datetime.now().year)
    }
    try:
        IndexAdvisorCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IndexAdvisorCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "is the SNP500(^GSPC) good to buy?",
        'current_year': str(datetime.now().year)
    }

    try:
        IndexAdvisorCrew.crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# def run_news_only():
# 	inputs = {"index_name": "S&P 500"}
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
run()
# test()
# run_news_only()