import streamlit as st
from tabs.modelo.prophet_tab import ModeloProphetTab
from utilidades.const import TITULO_MODELO, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_MODELO}]")

    st.markdown(
        """
        Prever o preço do barril de petróleo Brent é um desafio crucial devido à sua importância na economia global. O petróleo Brent é usado como referência internacional para determinar os preços de compra e venda em todo o mundo. A ferramenta Prophet é valiosa porque simplifica o processo de previsão de preços, ajudando a entender tendências passadas e sazonalidades que influenciam os preços do petróleo. Isso é vital para empresas, governos e investidores que dependem de previsões precisas para tomar decisões estratégicas, como planejar investimentos, gerenciar riscos financeiros e ajustar políticas econômicas.
    """
    )

    tab0 = st.tabs(tabs=["Prophet"])

    ModeloProphetTab(tab0)
