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
    .mid {
        color:rgba(255,140,0);
    }
    .alt {
        color:rgba(255,69,0)
    }
    .low {
        color:rgba(255,215,0)
    }
</style>
""", unsafe_allow_html=True)

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

datas =[]
status = [] 
tipos_problemas = []
urgencias=[]
if options == []:
    deu_certo,problemas = uts.get_problemas()
    if deu_certo: 
        for problema in problemas['problemas']:
            datas.append(problema['data_inicio'])
            if 'status' in problema:
                status.append(problema['status'])
            tipos_problemas.append(problema['problema_tipo'])
            urgencias.append(problema['urgencia'])
    else: 
        st.error(problemas)

else:
    for i in range (len(options)):
        deu_certo, problemas = uts.mostra_problemas_filtrado(options[i])
    if deu_certo:
        if problemas['problemas'] == []:
            st.write("Não há problemas cadastrados com essa urgência")
        else:
            for problema in problemas['problemas']:
                datas.append(problema['data_inicio'])
                if 'status' in problema:
                    status.append(problema['status'])
                tipos_problemas.append(problema['problema_tipo'])
                urgencias.append(problema['urgencia'])
    else: 
        st.error(problemas)


col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])

with col1:
    st.subheader("Problema")
    st.divider()
    for tipo_problema in tipos_problemas:
        st.write(tipo_problema)

with col2:
    st.subheader("Datas")
    st.divider()
    for data in datas:
        st.write(data)

with col3:
    st.subheader("Urgência")
    st.divider()
    for urgencia in urgencias:
        if urgencia == "Alta" or urgencia == "alta":
            st.write(f'<h6 class= alt>{urgencia} </h6>',unsafe_allow_html=True)
        if urgencia == "Mediana" or urgencia == "mediana":
            st.write(f'<h6 class= mid>{urgencia} </h6>',unsafe_allow_html=True)
        if urgencia == "Mínima" or  urgencia == "minima":
            st.write(f'<h6 class= low>{urgencia} </h6>',unsafe_allow_html=True)

with col4:
    st.subheader("Status")
    st.divider()
    for status_ in status:
        st.write(status_)

with col5:
    st.subheader("Mais")
    st.write()