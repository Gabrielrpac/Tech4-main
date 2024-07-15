import streamlit as st
from utilidades.const import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_REFERENCIAS}]")
    
    st.markdown(
        """ 
        01. https://ptfbs.com/glossary/brent-180#:~:text=Hist%C3%B3ria%20do%20Brent,provou%20ser%20de%20alta%20qualidade. Acesso em 01/07/2024
        02. http://www.ipeadata.gov.br/Default.aspx  Acesso em 01/07/2024
        03. https://facebook.github.io/prophet/docs/diagnostics.html Acesso em  10/07/2024
        04. https://docs.streamlit.io/ Acesso em  10/07/2024
        05. https://facebook.github.io/prophet/docs/diagnostics.html Acesso em  10/07/2024
        06. https://plotly.com/python/ Acesso em  10/07/2024
        07. https://brasilescola.uol.com.br/historiag/guerra-golfo.htm Acesso em  20/06/2024
        08. https://www.bbc.com/portuguese/internacional-55351015 Acesso em  26/06/2024
        09. https://brasilescola.uol.com.br/guerras/guerra-iraque.htm Acesso em  26/06/2024
        10. https://www.politize.com.br/crise-financeira-de-2008/ Acesso em  26/06/2024
        11. https://brasilescola.uol.com.br/geografia/primavera-Arabe.htm Acesso em  26/06/2024
        12. https://g1.globo.com/economia/mercados/noticia/2016/01/por-que-o-preco-do-petroleo-caiu-tanto-veja-perguntas-e-respostas.html Acesso em  26/06/2024
        13. https://www.cnnbrasil.com.br/saude/covid-em-2022-queda-de-mortes-aumento-de-casos-autotestes-e-descobertas/ Acesso em  26/06/2024
        14. https://brasilescola.uol.com.br/geografia/por-que-a-russia-invadiu-a-ucrania-em-2022.htm#:~:text=A%20invas%C3%A3o%20da%20Ucr%C3%A2nia%20pela,da%20Ucr%C3%A2nia%20promovida%20pela%20R%C3%BAssia. Acesso em  26/06/2024
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
    )
