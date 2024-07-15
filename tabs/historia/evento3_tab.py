import streamlit as st
from tabs.historia.evento_tab import EventoTab
from utilidades.layout import format_number


class HistoriaEvento3Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2003-01-01" and ds <= "2007-01-01"',
            query_periodo_interesse='ds >= "2003-05-01" and ds <= "2006-09-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":green[Guerra do Iraque (2003-2011)]", divider="blue")
            st.markdown(
                """
                O conflito no Iraque, também conhecido como a Segunda Guerra do Golfo, teve início em março de 2003 com a invasão do país por uma coalizão liderada pelos Estados Unidos. O principal objetivo era destituir Saddam Hussein, sob a alegação de que ele possuía armas de destruição em massa e apoiava atividades terroristas. Com a queda do regime de Hussein, o conflito transformou-se em uma prolongada e complexa guerra de guerrilha, resultando em inúmeras perdas de vidas e deixando um legado de instabilidade no Oriente Médio. O término oficial da guerra foi declarado em dezembro de 2011, quando as últimas tropas americanas se retiraram do país.
            """
            )

            st.subheader(
                ":green[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                Podemos notar que a Guerra do Iraque teve um impacto significativo no preço do barril de petróleo. Desde o seu início em 2003, até a metade 2006 podemos observar um aumento expressivo de :blue[US$ {format_number(self.min, '%.2f')}] para :blue[US$ {format_number(self.max, '%.2f')}], o que representa um aumento de :green[{format_number(self.variacao_positiva, '%.2f')}%] no período.
            """
            )

            self.plot_graficos()