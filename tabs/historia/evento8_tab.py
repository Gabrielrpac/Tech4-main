import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento8Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2022-01-01" and ds <= "2023-01-01"',
            query_periodo_interesse='ds >= "2022-02-01" and ds <= "2023-01-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[Conflito Rússia-Ucrânia (2022~)]", divider="blue"
            )
            st.markdown(
                """
                O conflito entre a Rússia e a Ucrânia em 2022, também conhecido como a invasão russa da Ucrânia, começou no dia 24 de fevereiro de 2022. Este conflito teve profundas implicações geopolíticas, econômicas e humanitárias. A invasão representou uma escalada significativa das tensões que já existiam entre os dois países desde 2014, quando a Rússia anexou a Crimeia e grupos separatistas pró-russos surgiram causando conflitos no leste da Ucrânia.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                A invasão criou uma grande incerteza geopolítica, uma vez que a Rússia é um dos maiores produtores e exportadores de petróleo do mundo. A perspectiva de interrupções no fornecimento de petróleo russo elevou os preços. Os efeitos se mantiveram por volta de Julho/2022, quando o preço começou a estabilziar em patamares mais baixos. O valor máximo atingido durante o período de interesse foi de :blue[US$ {format_number(self.max, '%.2f')}] e o valor mínimo foi de :blue[US$ {format_number(self.min, '%.2f')}], com uma variação de :green[{format_number(self.variacao_positiva, '%.2f')}%].
            """
            )

            self.plot_graficos()
