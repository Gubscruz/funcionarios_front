import streamlit as st
import api_utils as uts

st.title("Novos problemas")

options = st.multiselect(
    'Filtro de urgência',
    ['Extrema', 'Mediana', 'Mínima'])

# if 'Extrema' in options:
#     filtro = {}
#     salvou, problemas = uts.mostra_problemas_filtrado()
#     st.write(f'{problemas}')

# if 'Mediana' in options:
#     salvou, problemas = uts.mostra_problemas_filtrado()
#     st.write(f'{problemas}')

# if 'Mínima' in options:
#     salvou, problemas = uts.mostra_problemas_filtrado()
#     st.write(f'{problemas}')

if options == []:
    problemas = uts.get_problemas()
    st.write(f'{problemas}')
else:
    for i in range (len(options)):
        salvou, problemas = uts.mostra_problemas_filtrado(options[i])
    if salvou:
        if problemas['problemas'] == []:
            st.write("Não há problemas cadastrados com essa urgência")
        else:
            st.write(f'{problemas}')
