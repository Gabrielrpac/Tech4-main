import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento4Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2007-01-01" and ds <= "2009-12-01"',
            query_periodo_interesse='ds >= "2008-05-01" and ds <= "2009-02-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[Crise financeira mundial(2007 Até 2009)]", divider="blue"
            )
            st.markdown(
                """
                A Grande Recessão, ocorrida entre 2007 e 2009, teve origem na crise do mercado imobiliário dos EUA. A concessão excessiva de empréstimos hipotecários de alto risco a indivíduos sem capacidade financeira desencadeou o problema. Esses empréstimos foram transformados em produtos financeiros complexos e vendidos internacionalmente. Com a queda do mercado imobiliário e a desvalorização dos imóveis, muitos mutuários não conseguiram pagar suas hipotecas, resultando em alta inadimplência. O colapso afetou grandes instituições financeiras e propagou-se globalmente, levando a uma recessão global, aumento do desemprego e impactos duradouros nas economias e na política mundial.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                Em suma, a crise financeira de 2008 afetou o preço do petróleo Brent principalmente através da redução da demanda global por energia, da volatilidade nos mercados financeiros, das políticas monetárias adotadas pelos bancos centrais e das intervenções governamentais para estabilizar a economia global. O período de interesse analisado (linha em vermelho) mostra uma variação incrível de :red[{format_number(self.variacao_negativa, '%.2f')}%], ou seja, o preço caiu de sua máxima de :green[US$ {format_number(self.max, '%.2f')}] para a mínima de :green[US$ {format_number(self.min, '%.2f')}].
            """
            )

            self.plot_graficos()
