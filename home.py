import streamlit as st

st.title("Bem vindo!")
st.subheader("Aqui você consegue ver os problemas urbanos relatados pelos cidadãos")

st.write('Abaixo uma explicação breve de cada uma das opções:')


tab1, tab2, tab3 = st.tabs(["Novos Problemas", "Mapa de Problemas", "Estatísticas"])

with tab1:
    st.write("Nesta opção você pode visualizar os problemas cadastrados no sistema. Além disso, você pode filtrar os problemas por ID e urgência.")
    st.write("Acesse o menu lateral e clique em 'Novos Problemas'.")

with tab2:
    st.write("Nesta opção você pode visualizar os problemas cadastrados no sistema de forma geográfica.")
    st.write("Acesse o menu lateral e clique em 'Mapa de Problemas'.")

with tab3:
    st.write("Nesta opção você pode visualizar as estatísticas dos problemas cadastrados no sistema. Essa página contém gráficos e tabelas com informações sobre os problemas.")
    st.write("Acesse o menu lateral e clique em 'Estatísticas'.")