from crewai.tools import BaseTool
import requests
import time

class NumVerifyTool(BaseTool):
    name: str = "Validador de Número"
    description: str = "Valida números de telefone e retorna informações como país e operadora."

    def _run(self, number: str = "+5549991921307") -> str:
        response = requests.get(
            f"http://apilayer.net/api/validate?access_key=5a88cad60f9af373b7956c75bf2edcc1&number={number}&country_code=&format=1"
        )
        return str(response.json())

class NewsApiTool(BaseTool):
    name: str = "Notícias sobre IA"
    description: str = "Busca uma notícia popular sobre inteligência artificial."

    def _run(self, _: str = "") -> str:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q": "inteligência artificial",
                "from": "2025-05-21",
                "to": "2025-05-21",
                "sortBy": "popularity",
                "pageSize": 1,
                "apiKey": "3c11dbcb45a1426f9d14f1b4298b03e9"
            }
        )
        data = response.json()
        if data.get("articles"):
            article = data["articles"][0]
            return f"Título: {article['title']}\nDescrição: {article['description']}\nURL: {article['url']}"
        return "Nenhuma notícia encontrada sobre inteligência artificial."


class MarketStackTool(BaseTool):
    name: str = "Consulta de Ações"
    description: str = "Retorna dados de mercado de ações para uma empresa específica."

    def _run(self, symbol: str = "TSLA") -> str:
        response = requests.get(
            f"http://api.marketstack.com/v1/eod?access_key=a2dd96156ae00e4e779c77c4f0f95d31&symbols={symbol}&limit=1"
        )
        return str(response.json())