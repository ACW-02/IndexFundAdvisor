# IndexFundAdvisor
"Intelligent Financial Advisory Chatbot: AI-Driven Investment Insights for Index Funds Using CrewAI"

Intelligent Financial Advisory Chatbot: AI-Driven Investment Insights for Index Stock Using CrewAI, an AI-powered multi-agent system designed to provide strategic investment recommendations for stock market indexes. Built using the CrewAI framework, the chatbot processes a user-specified index and autonomously gathers and synthesizes relevant information from financial news articles, macroeconomic indicator analysis, and technical chart data. Leveraging this multi-source evidence, it generates actionable strategies—BUY, KEEP, or SELL—tailored to the queried index and time frame. The system is evaluated using the RAGAS metric suite, including Context Recall, Context Precision, Response Relevancy, Faithfulness, and Noise Sensitivity, ensuring high contextual accuracy and robustness. Additionally, a FastAPI-based prototype demonstrates the model’s feasibility for real-world deployment, enabling interactive financial advisory capabilities. To assess practical investment value, AI-generated strategies undergo manual review and backtesting, with Return on Investment (ROI) calculated over varied trading durations ranging from 3 months to 2 years. The combined quantitative and qualitative evaluation reveals the model’s strengths in delivering contextually relevant and factually grounded recommendations, while identifying areas for improvement in handling noisy or conflicting data. This work highlights the potential of CrewAI-driven systems to augment investment decision-making through automated, evidence-based insights.

disini ada file src dan knowledge

cara install requirements ke vscode:
use the command pip install -r requirements. txt in your terminal.

VSCode Setup:
1. download indexfunds folder diatas
2. buka indexfund folder
3. ketik "cmd" lewat path file
4. ketik "code ." dalam cmd

Cara run crew:
1. buka file src
2. buka file indexfunds
3. buka file main.py
4. ketik di terminal "cd src"
5. ketik di terminal "python -m indexfunds.main"



