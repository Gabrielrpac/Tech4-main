import streamlit as st
from utilidades.const import TITULO_PRINCIPAL
from utilidades.layout import output_layout
import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":green[{TITULO_PRINCIPAL}]")

st.subheader(
    ":green[PETRÓLEO BRENT - ANÁLISE HISTÓRICA E PREVISÃO DO PREÇO]",
    divider="blue",
)
st.markdown(
    """
    Este estudo tem como objetivo investigar as variações históricas dos preços do petróleo Brent e desenvolver modelos de machine learning para prever seus preços futuros. O petróleo Brent, reconhecido como uma referência internacional, é amplamente utilizado em negociações comerciais e contratos futuros no mundo todo. Entender as tendências passadas e detectar padrões nos dados históricos do preço do petróleo Brent proporciona informações valiosas para investidores, empresas e formuladores de políticas energéticas.\n\n
    Ao explorar os dados históricos do preço do petróleo Brent, realizaremos análises estatísticas para compreender melhor os padrões e tendências ao longo do tempo. Este processo incluirá a identificação de fatores que influenciam significativamente o preço do petróleo, como oferta e demanda, geopolítica e condições econômicas globais. Além disso, utilizaremos técnicas de visualização de dados para destacar padrões e correlações relevantes, o que nos permitirá desenvolver insights mais aprofundados sobre o comportamento do mercado de petróleo.\n\n
    Após a análise, são criados dois modelo de machine learning voltados para séries temporais que serão responsáveis por prever o preço futuro do barril de petróleo Brent.
"""
)

st.subheader(":green[PROPÓSITO]", divider="blue")
st.markdown(
    """
    Analisar o histórico de preços do petróleo Brent e criar modelos de machine learning que auxiliem na previsão do seu preço futuro. Durante este projeto, também é abordado a questão de *deploy* de modelos num ambiente produtivo, no caso, esta aplicação Streamlit.
"""
)


st.subheader(":green[RECURSO]", divider="blue")
st.markdown(
    """
    Primeiro, Realizamos a importação dos dados de preço do barril de petróleo Brent. Em seguida, analisamos os dados para entender como estão distribuidos.
    Com base na análise feita, criamos um modelo através do Prophet para que seja possível prever o preço futuro do barril de petróleo.
"""
)