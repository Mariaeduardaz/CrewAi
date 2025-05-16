from crewai import Crew
from tools import NumVerifyTool, IpStackTool, MarketStackTool
from agents import AgentFactory
from tasks import TaskFactory

print("🔧 Inicializando...")

# Instanciar ferramentas
tools = [NumVerifyTool(), IpStackTool(), MarketStackTool()]

# Criar agente com as ferramentas
analista = AgentFactory.get_agent(tools)

# Criar tarefas
tarefas = TaskFactory.get_tasks(analista)

# Criar equipe e executar
crew = Crew(agents=[analista], tasks=tarefas, verbose=True)
print("🚀 Executando tarefa...")
resultado = crew.kickoff()

print("\n✅ Resultado Final:")
print(resultado)