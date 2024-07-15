import streamlit as st
from tabs.tab import TabInterface

class IntroPetroleoBrentTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':green[PETRÓLEO BRENT]', divider='blue')
            st.markdown('''
            O petróleo Brent é um dos principais benchmarks de referência mundial para a cotação do petróleo. Este tipo de petróleo é leve e doce, características que o tornam ideal para a produção de gasolina e outros produtos refinados de alta qualidade. A cotação do Brent serve como base para os preços de aproximadamente dois terços do petróleo comercializados globalmente. A importância do petróleo Brent se deve à sua estabilidade e liquidez no mercado. É amplamente utilizado em contratos futuros e é um indicador essencial para investidores e empresas na tomada de decisões. A cotação do Brent é influenciada por diversos fatores, incluindo a oferta e demanda global, condições geopolíticas, políticas de produção dos países membros da OPEP e inovações tecnológicas na extração e refino de petróleo. Além disso, o preço do Brent tem um impacto significativo na economia global, afetando desde os custos de produção industrial até os preços dos combustíveis para consumidores finais. Compreender as dinâmicas e tendências do mercado do petróleo Brent é crucial para análises econômicas e estratégias de investimento.
            ''')
            st.divider()