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
ticker_symbol2 = st.sidebar.text_input("Nome 2", "MSFT", max_chars=10)

#BAIXAR os dados:
data1 = yf.download(ticker_symbol1, start='2021-01-01', end='2021-12-31')
data2 = yf.download(ticker_symbol2, start='2021-01-01', end='2021-12-31')

#exibir os dados (aka dataframe):
st.subheader("Historico")
st.dataframe(data)

#exibir grafico 1:
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data.index, y=data1["Close"], name="Fechamento"))
fig1.update_layout(title=f"{ticker_symbol1}", xaxis_title="DATA", yaxis_title="PREÇO")
st.plotly_chart(fig1)

#exibir grafico 2:
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data.index, y=data2["Close"], name="Fechamento"))
fig2.update_layout(title=f"{ticker_symbol2}", xaxis_title="DATA", yaxis_title="PREÇO")
st.plotly_chart(fig2)

#derrubar aplicação =  ctrl Z

# git status - pra checar como ta o arquivo
# git add nome do arquivo pra salvar
# git commit -m "comentario"
# git push origin main

#fazendo branch:  git checkout -b build/create_requirements "nome"
