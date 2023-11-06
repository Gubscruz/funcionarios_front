import api_utils as uts
import streamlit as st 
import plotly.express as px
import unidecode

st.title("Estatísticas")
st.write("Aqui você pode visualizar as estatísticas dos problemas cadastrados no sistema. Essa página contém gráficos com informações sobre os problemas.")




problemas = uts.get_problemas()
lista_tipos = []
lista_bairros = []
lista_urgencias = []

for i in range(len(problemas['problemas'])):
    lista_tipos.append(problemas['problemas'][i]['problema_tipo'])
    lista_bairros.append(problemas['problemas'][i]['bairro'].lower())
    lista_urgencias.append(problemas['problemas'][i]['urgencia'])

for i in range(len(lista_bairros)):
    lista_bairros[i] = unidecode.unidecode(lista_bairros[i])


lista_qnt_bairros = []
for i in range(len(lista_tipos)):
    contador = 0
    string = lista_tipos[i]
    for bairro in lista_tipos:
        if bairro == string:
            contador += 1
    lista_qnt_bairros.append(contador)


fig_tipos = px.pie(lista_tipos, names=lista_tipos, title='Tipos de problemas')
st.plotly_chart(fig_tipos)

fig_urgencias = px.pie(lista_urgencias, names=lista_urgencias, title='Urgências dos problemas')
st.plotly_chart(fig_urgencias)

fig = px.bar(lista_bairros, x=lista_bairros, y= lista_qnt_bairros, title='Bairros com mais problemas')
st.plotly_chart(fig)



