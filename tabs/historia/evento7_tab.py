import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento7Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2020-01-01" and ds <= "2021-01-01"',
            query_periodo_interesse='ds >= "2020-01-01" and ds <= "2020-05-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[Pandemia de COVID-19 (2020-2023)]", divider="blue"
            )
            st.markdown(
                """
                A pandemia da COVID-19 foi uma crise global de saúde pública causada pelo coronavírus SARS-CoV-2. A pandemia começou em dezembro de 2019 na cidade de Wuhan, na China, e rapidamente se espalhou para o resto do mundo, levando a uma série de medidas de contenção, impactos econômicos e sociais significativos. A COVID-19 teve e continua a ter um impacto profundo em praticamente todos os aspectos da vida moderna, destacando a importância da preparação para pandemias e a cooperação global em saúde pública.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                Logo no início da pandemia, em meados de Fevereiro/2020 e até Maio/2020, podemos observar uma queda acentuada no preço do barril de petróleo. Tal queda foi influenciada pelo lockdown imposto pelos governos de todo o mundo, com o objetivo de combater a pandemia em curso. Para exemplificar o impacto no preço, considerando o período de interesse, o preço máximo atingido (ocorrido em Fevereiro) foi de :green[US$ {format_number(self.max, '%.2f')}]. Já o preço minímo foi de :green[US$ {format_number(self.min, '%.2f')}] (atingido em Abril). Isso representa uma variação de cerca de :red[{format_number(self.variacao_negativa, '%.2f')}%].
            """
            )

            self.plot_graficos()
