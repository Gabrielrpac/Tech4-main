import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento5Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2010-01-01" and ds <= "2012-01-01"',
            query_periodo_interesse='ds >= "2010-09-01" and ds <= "2011-06-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":green[Primavera Árabe (2010-2012)]", divider="blue")
            st.markdown(
                """
                A Primavera Árabe foi uma série de protestos, revoltas e revoluções que ocorreram em vários países árabes a partir de dezembro de 2010. Os eventos começaram na Tunísia e rapidamente se espalharam para outros países, incluindo Egito, Líbia, Síria, Iêmen, Bahrein e outros. As causas principais da Primavera Árabe incluíram descontentamento com regimes autoritários, corrupção, falta de liberdades civis, e altas taxas de desemprego.\n\n A Primavera Árabe teve um impacto considerável no mercado de petróleo, causando aumentos nos preços e uma maior volatilidade devido à instabilidade política e interrupções na produção em países chave da região.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                O período de interesse analisado à seguir abrange não apenas a Primavera Árabe, mas também os eventos que surgiram a partir dela, como a Guerra Civil na Líbia e o Conflito na Síria. Esses eventos combinados contribuíram para a elevação dos preços do barril de petróleo. De setembro de 2010 até junho de 2011, o preço aumentou aproximadamente :green[{format_number(self.variacao_positiva, '%.2f')}%], tendo sua mínima em :green[US$ {format_number(self.min, '%.2f')}] e saltando para a máxima de :green[US$ {format_number(self.max, '%.2f')}].
            """
            )

            self.plot_graficos()
