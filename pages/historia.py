import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from tabs.historia.evento1_tab import HistoriaEvento1Tab
from tabs.historia.evento2_tab import HistoriaEvento2Tab
from tabs.historia.evento3_tab import HistoriaEvento3Tab
from tabs.historia.evento4_tab import HistoriaEvento4Tab
from tabs.historia.evento5_tab import HistoriaEvento5Tab
from tabs.historia.evento6_tab import HistoriaEvento6Tab
from tabs.historia.evento7_tab import HistoriaEvento7Tab
from tabs.historia.evento8_tab import HistoriaEvento8Tab
from utilidades.const import TITULO_HISTORIA, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


def plot_grafico_evolucao_preco_petroleo():
    def add_ponto_interesse(fig, ponto, text_index, label):
        fig.add_trace(
            go.Scatter(
                x=[ponto.ds.values[0]],
                y=[ponto.y.values[0]],
                mode="markers",
                text=1,
                marker=dict(color="red", size=10, line=dict(color="white", width=1)),
                name=label,
            )
        )
        fig.add_annotation(
            x=ponto.ds.values[0],
            y=ponto.y.values[0] + 4,
            text=text_index,
            showarrow=False,
            font=dict(color="white", size=10),
            bgcolor="red",
            borderwidth=1,
            bordercolor="white",
        )

    df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=df.ds, y=df.y, mode="lines", name="Preço do barril de petróleo")
    )
    add_ponto_interesse(
        fig, df.query('ds == "1990-08-02"'), 
            1, "1. Guerra do Golfo (1990-1991)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2001-09-11"'),
        2,
        "2. Atentados 11 de Setembro (2001)",
    )
    add_ponto_interesse(
        fig, df.query('ds == "2003-03-20"'), 3, "3. Guerra do Iraque (2003-2011)"
    )
    add_ponto_interesse(
        fig, df.query('ds == "2007-08-01"'), 4, "4. Crise financeira global (2007-2009)"
    )
    add_ponto_interesse(
        fig, df.query('ds == "2010-12-20"'), 5, "5. Primavera Árabe (2010-2012)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2014-11-28"'),
        6,
        "6. OPEP - Grande produção e baixa demanda (2014-2015)",
    )
    add_ponto_interesse(
        fig, df.query('ds == "2020-01-30"'), 7, "7. Pandemia de COVID-19 (2020-2022)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2022-02-24"'),
        8,
        "8. Conflito Rússia-Ucrânia (2022-presente)",
    )
    fig.update_layout(
        title="Evolução do preço do barril de petróleo Brent ao longo das decádas (1987 até hoje)",
        xaxis_title="Data",
        yaxis_title="Preço em US$",
        height=640,
    )

    st.plotly_chart(fig, use_container_width=True)


with st.container():

    with open("assets/historia.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.header(f":green[{TITULO_HISTORIA}]")
    st.markdown(
        """
        Ao longo dos anos, diversos eventos significativos, como guerras e revoluções, influenciaram profundamente o contexto geopolítico global de suas respectivas épocas. Esses acontecimentos desempenharam um papel crucial nas oscilações dos preços do petróleo, uma commodity fundamental na economia mundial.\n\n
        
        A seguir, serão apresentados alguns dos principais eventos que influenciaram diretamente
        
        * Guerra do Golfo (1990-1991)
        * Atentados terroristas nos EUA (2001)
        * Guerra do Iraque (2003-2011)
        * Crise financeira global (2007-2009)
        * Primavera Árabe (2010-2012)
        * OPEP - Grande ritmo de produção e baixa demanda (2014-2015)
        * Pandemia de COVID-19 (2020-2022)
        * Conflito Rússia-Ucrânia (2022~)
        
        Esses eventos não apenas alteraram o equilíbrio geopolítico global, mas também tiveram impactos diretos nos mercados de petróleo, influenciando seus preços e volatilidade ao longo dos anos.
    """
    )

    plot_grafico_evolucao_preco_petroleo()

    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        tabs=[
            "Guerra do Golfo (1990-1991)",
            "Atentados terroristas nos EUA (2001)",
            "Guerra do Iraque (2003-2011)",
            "Crise financeira global (2007-2009)",
            "Primavera Árabe (2010-2012)",
            "OPEP - Grande ritmo de produção e baixa demanda (2014-2015)",
            "Pandemia de COVID-19 (2020-2022)",
            "Conflito Rússia-Ucrânia (2022~)",
        ]
    )

    HistoriaEvento1Tab(tab0)
    HistoriaEvento2Tab(tab1)
    HistoriaEvento3Tab(tab2)
    HistoriaEvento4Tab(tab3)
    HistoriaEvento5Tab(tab4)
    HistoriaEvento6Tab(tab5)
    HistoriaEvento7Tab(tab6)
    HistoriaEvento8Tab(tab7)