import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

class AgentFactory:
    @staticmethod
    def get_phone_agent(tools):
        return Agent(
            role="Validador de Números",
            goal="Verificar e identificar detalhes de números de telefone.",
            backstory="Especialista em validação e origem de números telefônicos.",
            llm=llm,
            tools=[tools[0]],
            allow_delegation=False
        )

    @staticmethod
    def get_ia_agent(tools):
        return Agent(
            role="Analista de Inteligência Artificial",
            goal="Buscar e analisar uma notícia popular sobre IA.",
            backstory="Especialista em tendências e notícias recentes sobre inteligência artificial.",
            llm=llm,
            tools=[tools[1]],  # índice 1, que será o NewsApiTool agora
            allow_delegation=False
        )

    @staticmethod
    def get_stock_agent(tools):
        return Agent(
            role="Consultor de Ações",
            goal="Consultar dados de mercado de ações para empresas específicas.",
            backstory="Analista financeiro focado em ações e movimentações de mercado.",
            llm=llm,
            tools=[tools[2]],
            allow_delegation=False
        )