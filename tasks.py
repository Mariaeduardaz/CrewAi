from crewai import Task

class TaskFactory:
    @staticmethod
    def get_tasks(agent):
        return [
            Task(
                description="""
Use suas ferramentas para buscar:
1. Informações sobre o número de telefone +447911123456 (Reino Unido)
2. Localização e dados do IP 8.8.8.8 (Google)
3. Dados da empresa TSLA (Tesla Inc.) no mercado financeiro

Analise esses dados e gere um relatório completo, estruturado com título, subtítulos e conclusões relevantes.
""",
                expected_output="Relatório técnico com os dados de telefone, IP e ações da Tesla interpretados e estruturados.",
                agent=agent,
                output_file="output/resultado_tesla_uk_google.txt"
            )
        ]
