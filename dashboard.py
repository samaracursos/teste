import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, 
               x = 'Date_reported', 
               y = 'Cumulative_cases', 
               color = 'Country',
               title = 'Número de Casos Acumulados de COVID-19')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig1.show()

st.title('DASHCOVID - Um Painel de Informações')

st.plotly_chart(fig2, use_container_width=True)
