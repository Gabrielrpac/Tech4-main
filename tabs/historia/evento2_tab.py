import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento2Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2001-07-01" and ds <= "2002-02-01"',
            query_periodo_interesse='ds >= "2001-09-01" and ds <= "2001-12-11"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[Atentados terroristas nos EUA (2001)]", divider="blue"
            )
            st.markdown(
                """
                
O atentado de 11 de setembro de 2001 consistiu em uma série de ataques terroristas coordenados pela organização extremista Al-Qaeda contra os Estados Unidos. Aviões comerciais foram sequestrados e intencionalmente colididos com as Torres Gêmeas do World Trade Center em Nova York e o Pentágono em Washington, D.C. Um quarto avião caiu na Pensilvânia após os passageiros tentarem retomar o controle. Este trágico evento causou a perda de milhares de vidas e teve um impacto significativo na política global, na segurança internacional e nas estratégias antiterrorismo.
            """
            )

            st.subheader(
                ":green[Variação de preço durante o evento histórico]",
                divider="blue",
            )

            st.markdown(
                f"""
                Analisando o gráfico, é possível observar uma queda forte no preço do barril de petróleo logo após os acontecimentos. De forma geral, no período de interesse analisado, houve uma variação de cerca de :red[{format_number(self.variacao_negativa, '%.2f')}%], caindo de :blue[US$ {format_number(self.max, '%.2f')}] para :blue[US$ {format_number(self.min, '%.2f')}] no seu menor nível no péríodo. Vale ressaltar que nos meses seguintes, o preço continuou com tendência de baixa.
            """
            )

            self.plot_graficos()
