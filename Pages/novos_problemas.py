import streamlit as st
import api_utils as uts

st.title("Novos problemas")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: rgba(120, 219, 217,0.6);
    }
    [data-testid="stSidebarNav"]::before {
        font-weight : 600;
        content: "Menu";
        margin-left: 20px;
        font: Helvica Bold;
        margin-top: 20px;
        font-size: 30px;
        position: relative;
        top: 100px;
        }
</style>
""", unsafe_allow_html=True)

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

    