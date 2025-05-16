from crewai.tools import BaseTool
import requests
import time

class NumVerifyTool(BaseTool):
    name: str = "Validador de Número"
    description: str = "Valida números de telefone e retorna informações como país e operadora."

    def _run(self, number: str = "+5511987654321") -> str:
        response = requests.get(
            f"http://apilayer.net/api/validate?access_key=9af9a375a1c594a0746b6747121e6efe&number={number}&country_code=&format=1"
        )
        return str(response.json())

class IpStackTool(BaseTool):
    name: str = "Localizador de IP"
    description: str = "Retorna informações sobre um endereço IP, como país e cidade."

    def _run(self, ip: str = "187.75.194.108") -> str:
        response = requests.get(
            f"http://api.ipstack.com/{ip}?access_key=96d3b66af2bf4f16f7f4bb7c26679eb5"
        )
        return str(response.json())

class MarketStackTool(BaseTool):
    name: str = "Consulta de Ações"
    description: str = "Retorna dados de mercado de ações para uma empresa específica."

    def _run(self, symbol: str = "AAPL") -> str:
        response = requests.get(
            f"http://api.marketstack.com/v1/eod?access_key=0b999b553c14f62b7463008c7ae4d70f&symbols={symbol}"
        )
        return str(response.json())