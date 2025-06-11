from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from indexfunds.tools.custom_tool import IndexNewsTool, MacroeconomicIndicatorTool, IndexTechnicalTool


@CrewBase
class IndexAdvisorCrew():
	"""Index Advisor Crew"""
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
	def index_macro_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['index_macro_analyst'],
			tools=[MacroeconomicIndicatorTool()],
			verbose=1
		)

	@agent
	def index_technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['index_technical_analyst'],
			tools=[IndexTechnicalTool()],
			verbose=1
		)

	@agent
	def index_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['index_researcher'],
			verbose=1
		)

	@agent
	def index_summary_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['index_summary_agent'],
			verbose=1
		)

	@task
	def index_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_news_task'],
			agent=self.index_news_analyst()
		)

	@task
	def index_macro_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_macro_task'],
			agent=self.index_macro_analyst()
		)

	@task
	def index_technical_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_technical_task'],
			agent=self.index_technical_analyst()
		)

	@task
	def index_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_research_task'],
			agent=self.index_researcher()
		)

	@task
	def index_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_summary_task'],
			agent=self.index_summary_agent(),
			output_file='index_output1.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Index Advisor Crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=1,
		)
