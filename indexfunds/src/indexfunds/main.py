#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from indexfunds.crew import IndexAdvisorCrew

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
        "topic": "is the SRI-KEHATI (SRI-KEHATI.JK) good to buy?",
        #"topic": "is the IDX LQ45 (^JKLQ45) good to buy?",
        #"topic": "is the SET_SET Index (^SET.BK) good to buy?",
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
        "topic": "is the SRI-KEHATI (SRI-KEHATI.JK) good to buy?",
        "current_year": str(datetime.now().year)
    }

    try:
        IndexAdvisorCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

run()