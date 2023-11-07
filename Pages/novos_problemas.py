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
    ['Extrema', 'Mediana', 'Mínima'],
    default=['Extrema', 'Mediana', 'Mínima']
)

datas = []
status = [] 
tipos_problemas = []
urgencias = []
problemas_acumulados = []

if not options:
    deu_certo, problemas = uts.get_problemas()
    if deu_certo:
        problemas_acumulados.extend(problemas['problemas'])
    else:
        st.error(problemas)
else:
    for urgencia_selecionada in options:
        deu_certo, problemas = uts.mostra_problemas_filtrado(urgencia_selecionada)
        if deu_certo:
            problemas_acumulados.extend(problemas['problemas'])
        else:
            st.error(problemas)

# Agora podemos processar todos os problemas acumulados
for problema in problemas_acumulados:
    datas.append(problema['data_inicio'])
    status.append(problema.get('status', 'Não informado'))
    tipos_problemas.append(problema['problema_tipo'])
    urgencias.append(problema['urgencia'])


col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
with col1:
    st.subheader("Problema")
with col2:
    st.subheader("Datas")
with col3:
    st.subheader("Urgência")
with col4:
    st.subheader("Status")
with col5:
    st.subheader("Mais")

for problema in problemas_acumulados:
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    
    with col1:
        st.write(problema['problema_tipo'])
    with col2:
        st.write(problema['data_inicio'])
    with col3:
        urgencia = problema['urgencia']
        if urgencia.lower() == "extrema":
            col3.markdown(f'<h6 class="alt">{urgencia}</h6>', unsafe_allow_html=True)
        elif urgencia.lower() == "mediana":
            col3.markdown(f'<h6 class="mid">{urgencia}</h6>', unsafe_allow_html=True)
        elif urgencia.lower() == "mínima":
            col3.markdown(f'<h6 class="low">{urgencia}</h6>', unsafe_allow_html=True)
    with col4:
        status = problema.get('status', 'Não informado')
        index_ = 0
        if status == "Em análise":
            index_ = 0
        elif status == "Reportado":
            index_ = 1
        elif status == "Aguardando Reparo":
            index_ = 2
        novo_status = st.selectbox("Status", ["Em análise", "Reportado", "Aguardando Reparo"], index=index_, key=str(problema['_id']))
        problema['status'] = novo_status
        uts.update_problemas(problema)

