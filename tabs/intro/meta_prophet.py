import streamlit as st
from tabs.tab import TabInterface


class IntroMetaProphet(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[META PROPHET]", divider="blue"
            )
            st.markdown(
                """
                O "Prophet da Meta" pode se referir ao software "Meta's Prophet" desenvolvido pela Meta (anteriormente conhecida como Facebook). Prophet é uma ferramenta de previsão de código aberto projetada para análise de séries temporais. Foi lançada pelo Facebook em 2017 e é amplamente utilizada para previsões automatizadas e análises em áreas como economia, finanças, marketing e operações.\n\n
                O Prophet foi desenvolvido para facilitar a criação de modelos de previsão precisos com apenas alguns parâmetros ajustáveis, o que o torna acessível mesmo para usuários com menos experiência em ciência de dados. Ele é conhecido por sua capacidade de lidar com sazonalidade, tendências e feriados de forma eficaz, além de ser robusto em relação a dados ausentes e outliers.\n\n
                Essa ferramenta se tornou popular entre analistas de dados e cientistas que precisam de previsões precisas e rápidas com base em dados históricos de séries temporais.
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            st.divider()