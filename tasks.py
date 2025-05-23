from crewai import Task

class TaskFactory:
    @staticmethod
    def get_tasks(phone_agent, ia_agent, stock_agent):
        return [
            Task(
                description=(
                    "Analise o número de telefone +5549991921307. Verifique informações como localização, operadora e tipo de linha (fixa ou móvel). "
                    "Com base nessas informações, avalie o perfil provável do usuário: é residencial, corporativo ou temporário? "
                    "Discuta como essa análise pode apoiar estratégias de atendimento ao cliente ou prevenção de fraudes."
                ),
                expected_output="Relatório com análise do número e recomendações para uso em contextos de negócios ou segurança.",
                agent=phone_agent,
                output_file="output/telefone.txt"
            ),
            Task(
                description=(
                    "Pesquise uma notícia popular sobre inteligência artificial publicada no dia 21 de maio de 2025. "
                    "Resuma o conteúdo, comente sobre a relevância do tema tratado e destaque como isso pode impactar o futuro da IA."
                ),
                expected_output="Resumo e análise crítica da notícia sobre inteligência artificial.",
                agent=ia_agent,
                output_file="output/ia.txt"
            ),
            Task(
                description=(
                    "Obtenha os dados mais recentes do mercado financeiro para a ação da Tesla (TSLA). "
                    "Avalie o comportamento do preço e volume negociado e interprete possíveis tendências de curto prazo. "
                    "Comente se o momento atual representa um bom ponto de entrada ou risco elevado para investidores."
                ),
                expected_output="Análise de mercado da ação da Tesla com comentários sobre risco e oportunidade de investimento.",
                agent=stock_agent,
                output_file="output/acoes.txt"
            )
        ]
