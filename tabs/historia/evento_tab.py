from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go
import streamlit as st


class EventoTab(TabInterface):
    def __init__(self, query_periodo_analisado, query_periodo_interesse):
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.periodo_analisado = self.df.query(query_periodo_analisado)
        self.periodo_interesse = self.df.query(query_periodo_interesse)
        self.min, self.max, self.variacao_positiva, self.variacao_negativa = self.calcular_variacao()

    def maiorData(self):
        
        maior_preco = self.periodo_analisado['y'].max()

        menor_preco = self.periodo_analisado['y'].min()

        data_menor_preco = self.periodo_analisado [self.periodo_analisado['y'] == menor_preco]['ds'].iloc[0]
        data_maior_preco = self.periodo_analisado [self.periodo_analisado['y'] == maior_preco]['ds'].iloc[0]
        return maior_preco, data_maior_preco, menor_preco, data_menor_preco

    def calcular_variacao(self):
        min = self.periodo_interesse["y"].min()
        max = self.periodo_interesse["y"].max()
        variacao_positiva = ((max * 100) / min) - 100
        variacao_negativa = ((min * 100) / max) - 100

        return min, max, variacao_positiva, variacao_negativa

    def plot_graficos(self):
        fig = go.Figure(
            layout=go.Layout(
                xaxis=dict(title="Data", tickformat="%b/%Y"),
                yaxis=dict(title="Preço em US$"),
            ),
        )
        
        fig.add_trace(
            go.Scatter(
                x=self.periodo_analisado.ds,
                y=self.periodo_analisado.y,
                mode="lines",
                name="Preço do barril de petróleo",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=self.periodo_interesse.ds,
                y=self.periodo_interesse.y,
                mode="lines",
                name="Período de interesse influenciado pelo evento",
                line=dict(color="green", width=2),
            )
        )

        maiorPreco, dataMaiorPreco, menorPreco, dataMenorPreco = self.maiorData()

        fig.add_trace(
            go.Scatter(
                x=[dataMaiorPreco],
                y=[maiorPreco],
                mode="markers",
                text=1,
                marker=dict(color="purple", size=10),
                name="Valor Maximo",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[dataMenorPreco],
                y=[menorPreco],
                mode="markers",
                text=1,
                marker=dict(color='pink', size=10, symbol='circle', ),
                name="Valor Minimo",
            )
        )

        with st.container():
            _, col1, _ = st.columns([1, 8, 1])

            with col1:
                st.plotly_chart(fig, use_container_width=True)
