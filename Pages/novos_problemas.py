import streamlit as st
import api_utils as uts

st.title("Novos problemas")

options = st.multiselect(
    'Filtro de urgência',
    ['Extrema', 'Mediana', 'Mínima'])

if 'Extrema' in options:
    salvou, problemas = uts.mostra_problemas_filtrado()
    st.write(f'{problemas}')

if 'Mediana' in options:
    salvou, problemas = uts.mostra_problemas_filtrado()
    st.write(f'{problemas}')

if 'Mínima' in options:
    salvou, problemas = uts.mostra_problemas_filtrado()
    st.write(f'{problemas}')

    