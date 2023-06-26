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
st.sidebar.title("titulo da barrinha")
ticker_symbol = st.sidebar.text_input("Texto", "AAPL", max_chars = 10)

#BAIXAR os dados:
data = yf.download(ticker_symbol, start = "2023-01-01", end = "2023-06-26")

#exibir os dados (aka dataframe):
st.subheader("Historico")
st.dataframe(data)

#exibir graficos:
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data["Close"], name = "Fechamento"))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "DATA", yaxis_title = "PREÇO")
st.plotly_chart(fig)

#derrubar aplicação =  ctrl Z

