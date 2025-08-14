from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from indexfunds.tools.custom_tool import IndexNewsTool, MacroeconomicIndicatorTool, IndexTechnicalTool
from indexfunds.tools.custom_tool import MacroeconomicIndicatorTool, IndexTechnicalTool
# from tools.custom_tool import IndexTechnicalTool, MacroeconomicIndicatorTool
from indexfunds.tools.news_tools import IndexNewsTool

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
			agent=self.index_news_analyst(),
			output_file='output_news_task.md'
		)

	@task
	def index_macro_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_macro_task'],
			agent=self.index_macro_analyst(),
			used_tools=True,
			output_file='output_macro_task.md'  
		)

	@task
	def index_technical_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_technical_task'],
			agent=self.index_technical_analyst(),
			used_tools=True,
			output_file='output_teknikal.md'  
		)

	@task
	def index_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_research_task'],
			agent=self.index_researcher(),
			output_file='output_research_task.md'  
		)

	@task
	def index_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_summary_task'],
			agent=self.index_summary_agent(),
			output_file='index_output_api.md'  
			# output_file='index_output_2.md'  
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Index Advisor Crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,  # enables thinking steps output
			return_intermediate_steps=True  # ensures web API can get thinking process
		)
	