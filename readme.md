# 🚀 Projeto CrewAI - Versão Estendida

Este projeto demonstra o uso da CrewAI para integrar múltiplas fontes de dados em um único relatório analítico.

## APIs Utilizadas

- NumVerify: Para verificação de números internacionais
- IpStack: Para rastreio de IPs públicos
- MarketStack: Para obter dados de ações de empresas listadas

**Importante:** Insira a variável de ambiente `GROQ_API_KEY` no arquivo `.env`.

## Execução do projeto

```bash
python -m venv venv # Utilize Python 3.12
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python main.py
```

O relatório será salvo em: `output/resultado_tesla_uk_google.txt`
