import streamlit as st
import pandas as pd
import geopandas as gpd
import geobr
import matplotlib.pyplot as plt

st.title('Tópicos Especiais em Informática')
st.caption('Cidades')

st.write('Atividade utilizando a ferramenta Streamlit')

gdf_estados = geobr.read_state()
gdf_muni = geobr.read_municipality()

estados = gdf_estados.sort_values('abbrev_state')['abbrev_state']
estado = st.selectbox('Estado: ', estados)
st.write(f'Estado escolhido: {estado}')

idx = gdf_muni['abbrev_state'] == estado
muni_est = gdf_muni[idx]

cidades = muni_est.sort_values('name_muni')['name_muni']
cidade = st.multiselect('Sua cidade: ', cidades)
st.write(f'Cidade escolhida: {cidade}')


idx = muni_est['name_muni'].isin(cidade)

mapa, ax = plt.subplots()
muni_est.plot(ax=ax, color='w', edgecolor='k')
muni_est[idx].plot(ax=ax,color="r",legend = True)
st.pyplot(mapa)
