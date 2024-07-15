import streamlit as st
from tabs.tab import TabInterface


class IntroIPEATab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[INSTITUTO DE PESQUISA ECONÔMICA APLICADA (IPEA)]", divider="blue"
            )
            st.markdown(
                """
                O Instituto de Pesquisa Econômica Aplicada (IPEA) é uma instituição vinculada ao Ministério da Economia do Brasil, especializada na produção de estudos e pesquisas em economia e políticas públicas. Fundado em 1964, desempenha um papel fundamental na formulação e avaliação de políticas governamentais, oferecendo análises baseadas em evidências para promover o desenvolvimento socioeconômico do país.\n\n
                O IPEA abrange áreas como macroeconomia, mercado de trabalho, saúde, educação, meio ambiente e segurança pública, sendo reconhecido nacional e internacionalmente como uma fonte confiável de informações para decisores políticos, acadêmicos e a sociedade em geral.\n\n
                No decorrer deste projeto, consultamos inicialmente os dados do IPEA, onde extraimos e utilizamos a base de dados importada diretamente da página da instituição.
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            st.divider()