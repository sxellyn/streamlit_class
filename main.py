#pip install esses pacotes abaixo no terminal:

import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

#comando pra rodar o app na maquina virtual:
#streamlit run /workspaces/nomedorepositorio/nomedoarquivo.py --server.enableCORS false --server.enableXsrfProtection false

#comando pra rodar o app na maquina local:
#streamlit run nomedoapp

# TITULO DO APP:
st.title("APPZINHO")

#barra lateral com opções:
st.sidebar.title("IRF")
ticker_symbol1 = st.sidebar.text_input("Nome 1", "AAPL", max_chars=10)
ticker_symbol2 = st.sidebar.text_input("Nome 2", "AAPL", max_chars=10)

#BAIXAR os dados:
data = yf.download(['AAPL', 'MSFT'], start='2021-01-01', end='2021-12-31')

#exibir os dados (aka dataframe):
st.subheader("Historico")
st.dataframe(data)

#exibir grafico 1:
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data["Close"], name = "Fechamento"))
fig.update_layout(title = f"{ticker_symbol1}", xaxis_title = "DATA", yaxis_title = "PREÇO")
st.plotly_chart(fig)

#exibir grafico 2:
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data["Close"], name = "Fechamento"))
fig.update_layout(title = f"{ticker_symbol2}", xaxis_title = "DATA", yaxis_title = "PREÇO")
st.plotly_chart(fig)

#derrubar aplicação =  ctrl Z

# git status - pra checar como ta o arquivo
# git add nome do arquivo pra salvar
# git commit -m "comentario"
# git push origin main

#fazendo branch:  git checkout -b build/create_requirements "nome"
