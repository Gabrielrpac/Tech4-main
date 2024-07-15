import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento6Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2014-01-01" and ds <= "2016-06-01"',
            query_periodo_interesse='ds >= "2014-06-01" and ds <= "2016-03-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[OPEP- Grande ritmo de produção e baixa demanda (2014-2015)]", divider="blue"
            )
            st.markdown(
                """
                Entre 2014 e 2015, o mercado de petróleo passou por um período significativo de queda nos preços, que foi impulsionado por um grande ritmo de produção e baixa demanda. Este período é frequentemente associado a várias dinâmicas econômicas e políticas globais e demonstrou a complexidade do mercado global de petróleo, onde decisões políticas, inovações tecnológicas e dinâmicas econômicas globais se entrelaçam, criando impactos significativos nos preços e na economia global.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                O próximo período de interesse analisado encontra-se entre Junho/2014 e Março/2016.  Foi uma época na qual a produção de petróleo estava em alta mas a demanda em baixa. Como todos sabemos, o mercado é regido pela lei da oferta e demanda e portanto, quando há muito de um produto disponível no mercado mas pouca demanda por ele, seu preço sofrerá uma grande desvalorização. Após atingir uma máxima de :blue[US$ {format_number(self.max, '%.2f')}], o preço do barril chegou a cair para a mínima de :blue[US$ {format_number(self.min, '%.2f')}] no período, o que representa uma variação de :red[{format_number(self.variacao_negativa, '%.2f')}%] no preço.
            """
            )

            self.plot_graficos()
