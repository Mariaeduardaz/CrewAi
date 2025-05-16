import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="groq/llama3-70b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

class AgentFactory:
    @staticmethod
    def get_agent(tools):
        return Agent(
            role="Analista Financeiro-Geo",
            goal="Integrar dados de localização IP, validação de telefones e mercado financeiro",
            backstory="Especialista em cruzar dados geográficos com informações financeiras",
            verbose=True,
            llm=llm,
            tools=tools,
            allow_delegation=False
        )
