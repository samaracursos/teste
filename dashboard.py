import pandas as pd
import plotly.express as px
import streamlit as st

st.title('DASHCOVID - Um Painel de Informações')

st.set_page_config(
    page_title="DashCovid",
    layout="wide")

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, 
               x = 'Date_reported', 
               y = 'Cumulative_cases', 
               color = 'Country',
               title = 'Número de Casos Acumulados de COVID-19')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

df_brasil_eua = df.query('Country == "Brazil" or Country == "United States of America"')

fig2 = px.line(df_brasil_eua, 
               x = 'Date_reported', 
               y = 'Cumulative_cases', 
               color = 'Country',
               title = 'Número de Casos Acumulados de COVID-19 - Brasil x EUA')
fig2.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig2.show()

st.plotly_chart(fig2, use_container_width=True)

df_brasil_eua_india = df.query('Country == "Brazil" or Country == "United States of America" or Country == "India"')

fig3 = px.pie(df_brasil_eua_india, 
               values = 'Cumulative_cases', 
               names = 'Country',
               title = 'Número de Casos Acumulados de COVID-19 - Brasil x EUA x INDIA')
fig3.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig3.show()

st.plotly_chart(fig3, use_container_width=True)
