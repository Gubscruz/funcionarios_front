import streamlit as st

st.title("Mais informações")

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
    st.subheader("")

