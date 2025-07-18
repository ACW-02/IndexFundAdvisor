from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from indexfunds.tools.news_tools import IndexNewsTool  # Ensure this path is correct

@CrewBase
class NewsOnlyCrew():
	"""Minimal crew to test only the news agent"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def index_news_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['index_news_analyst'],
			tools=[IndexNewsTool()],
			verbose=1
		)
	@agent
	def index_technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['index_technical_analyst'],
			tools=[IndexNewsTool()],
			verbose=1
		)

	@task
	def index_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_news_task'],
			agent=self.index_news_analyst(),
			output_file='test_output_news.md'  # Keep this separate
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=[self.index_news_analyst()],
			tasks=[self.index_news_task()],
			process=Process.sequential,
			verbose=True,
			return_intermediate_steps=True
		)
