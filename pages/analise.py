import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utilidades.const import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utilidades.layout import output_layout, format_number


st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")

with st.container():
    st.header(f":green[{TITULO_ANALISE_EXPLORATORIA}]")

    st.markdown(
        """
        Depois de uma análise cuidadosa do histórico dos preços do barril de petróleo, estamos agora investigando a distribuição desses preços ao longo das décadas, desde o início da série histórica em 1987. Essa análise nos permite compreender os padrões predominantes de preços, identificar os extremos históricos e outros indicadores importantes que foram discutidos detalhadamente.
    """
    )

    st.subheader(":green[ANÁLISE DESCRITIVA]", divider="blue")

    df_descritiva = df.describe()
    medida_count = df_descritiva.loc["count"]["y"]
    medida_mean = df_descritiva.loc["mean"]["y"]
    medida_std = df_descritiva.loc["std"]["y"]
    medida_min = df_descritiva.loc["min"]["y"]
    medida_25 = df_descritiva.loc["25%"]["y"]
    medida_50 = df_descritiva.loc["50%"]["y"]
    medida_75 = df_descritiva.loc["75%"]["y"]
    medida_max = df_descritiva.loc["max"]["y"]
    df_descritiva.reset_index(inplace=True)
    df_descritiva.columns = ["Medidas", "Preço do barril de petróleo"]

    st.markdown(
        f"""
        Nesta seção, apresentamos uma análise detalhada da distribuição dos preços ao longo das décadas. Os dados consistem em :green[{format_number(medida_count)}] observações, com uma média de aproximadamente :green[{format_number(medida_mean, '%.2f')}] e um desvio padrão em torno de :green[{format_number(medida_std, '%.2f')}]. O valor mínimo observado é :green[{format_number(medida_min, '%.2f')}], enquanto o valor máximo atinge :green[{format_number(medida_max, '%.2f')}]. Os quartis indicam que 25% dos dados estão abaixo de :green[{format_number(medida_25, '%.2f')}], 50% abaixo de :green[{format_number(medida_50, '%.2f')}] (mediana) e 75% abaixo de :green[{format_number(medida_75, '%.2f')}], , oferecendo uma visão abrangente da distribuição e variabilidade dos dados.
    """
    )

    with st.container():
        _, col, _ = st.columns([3, 4, 3])

        with col:
            st.dataframe(df_descritiva, use_container_width=True, hide_index=True)

    st.markdown(
        f"""
        Adicionalmente, incluímos um boxplot para uma representação visual dos dados, além de um histograma que ilustra a distribuição dos preços, mostrando claramente que não segue uma distribuição normal.
    """
    )

    with st.container():
        col0, col1 = st.columns([3, 7])

        with col0:
            st.subheader(":green[Boxplot]", divider="blue")

            fig = go.Figure(
                layout=go.Layout(
                    xaxis=dict(title="Data"),
                    yaxis=dict(title="Preço em US$"),
                    height=600,
                ),
            )

            fig.add_trace(
                go.Box(
                    y=df.y,
                    name="Preço do barril de petróleo Brent",
                    hoverlabel=dict(align="right"),
                    boxmean=True,
                )
            )

            st.plotly_chart(fig, use_container_width=True)

        with col1:
            st.subheader(":green[Histograma]", divider="blue")

            fig = ff.create_distplot([df.y], group_labels=["Distribuição dos preços"])
            fig.update_layout(
                xaxis_title="Valor",
                yaxis_title="Densidade",
                height=600,
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
                ),
            )
            fig.data[1].line.color = "green"

            st.plotly_chart(fig, use_container_width=True)

