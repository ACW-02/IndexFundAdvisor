from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from indexfunds.tools.custom_tool import IndexTechnicalTool

@CrewBase
class TechnicalOnlyCrew():
	"""Crew for Testing IndexTechnicalTool Only"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def index_technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['index_technical_analyst'],
			tools=[IndexTechnicalTool()],
			verbose=1
		)

	@task
	def index_technical_task(self) -> Task:
		return Task(
			config=self.tasks_config['index_technical_task'],
			agent=self.index_technical_analyst(),
			used_tools=True,
			output_file='output_teknikal.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates a crew with only the IndexTechnicalTool agent"""
		return Crew(
			agents=[self.index_technical_analyst()],
			tasks=[self.index_technical_task()],
			process=Process.sequential,
			verbose=True,
			return_intermediate_steps=True
		)
