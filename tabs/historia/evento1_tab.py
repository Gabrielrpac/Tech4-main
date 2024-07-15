import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento1Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "1990-01-01" and ds <= "1991-06-01"',
            query_periodo_interesse='ds >= "1990-05-01" and ds <= "1991-02-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":green[Guerra do Golfo (1990 Até 1991)]", divider="blue")
            st.markdown(
                """
                A guerra do Golfo foi um conflito armado que começou com o Iraque a invadindo Kuwait em 2 de Agosto de 1990 e durou até 28 de Fevereiro de 1991. Saddam Hussein era o ditador iraquiano na época. Imediatamente após a ocupação do Kuwait, os Estados Unidos declararam guerra à nação asiática e conseguiram ajuda de algumas outras nações como o Reino Unido, França e Arábia Saudita. Dessa forma, uma intervenção havia acontecido no país do Oriente Médio a fim de expulsar as forças iraquianas do território kuwaitiano.
            """
            )

            st.subheader(
                ":green[Variação de preço durante o evento histórico]",
                divider="blue",
            )

            st.markdown(
                f"""
                A seguir, temos gráfico da variação do preço do petróleo durante o conflito, onde analisamos o período de :green[01/07/1990] até :green[01/02/1991], e podemos observar que durante todo o conflito o preço disparou e mais que dobrou de valor, em cerca de :green[{format_number(self.variacao_positiva, '%.2f')}%], indo de :green[US$ {format_number(self.min, '%.2f')}] para cerca de :green[US$ {format_number(self.max, '%.2f')}].\n
                O preço apenas voltou a valores semelhantes à antes da Guerra do Golfo por volta do início do mês de Fevereiro de 1991.
            """
            )

            self.plot_graficos()
