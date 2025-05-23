from crewai import Crew
from tools import NumVerifyTool, NewsApiTool, MarketStackTool
from agents import AgentFactory
from tasks import TaskFactory

print("🔧 Inicializando...")

tools = [NumVerifyTool(), NewsApiTool(), MarketStackTool()]

phone_agent = AgentFactory.get_phone_agent(tools)
ia_agent = AgentFactory.get_ia_agent(tools)
stock_agent = AgentFactory.get_stock_agent(tools)

tasks = TaskFactory.get_tasks(phone_agent, ia_agent, stock_agent)

crew = Crew(
    agents=[phone_agent, ia_agent, stock_agent],
    tasks=tasks,
    verbose=True,
    max_iterations=1
)


print("🚀 Executando tarefas...")
resultado = crew.kickoff()

print("\n✅ Resultados das tarefas em output/")
