import streamlit as st
from tabs.intro.ipea_tab import IntroIPEATab
from tabs.intro.meta_prophet import IntroMetaProphet
from tabs.intro.petroleo_brent_tab import IntroPetroleoBrentTab
from utilidades.const import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_INTRODUCAO}]")

    st.markdown(
        """
        Nesta introdução, vamos apresentar algumas informações importantes para entendimento do contexto geral do projeto e como ele foi pensado para atender a necessidade proposta.\n\n
    """
    )

    tab0, tab1, tab2 = st.tabs(
        tabs=[
            "Petróleo Brent",
            "Instituto de Pesquisa Econômica Aplicada (IPEA)",
            "Meta Prophet"
        ]
    )

    IntroPetroleoBrentTab(tab0)
    IntroIPEATab(tab1)
    IntroMetaProphet(tab2)
