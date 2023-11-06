import streamlit as st 
import plotly.express as px
from api_utils import get_problemas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd


st.title("Mapa de Problemas")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: rgba(53, 219, 217,0.6);
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

def geocode_address(bairro, rua):
    geolocator = Nominatim(user_agent="geoapiExercises")
    geocode = geolocator.geocode
    
    try:
        location = geocode(f"{rua}, {bairro}, São Paulo")
        if location:
            return location.latitude, location.longitude
        # else:
        #     return None, None
    except Exception as e:
        print(f"Erro ao geocodificar {rua}, {bairro}: {e}")
    return None, None

dados_geocoded = []
dados_json = get_problemas()
for item in dados_json['problemas']:
    lat, lon = geocode_address(item['bairro'], item['rua'])
    if lat and lon:
        item['latitude'] = lat
        item['longitude'] = lon
        dados_geocoded.append(item)

dados_geocoded = [item for item in dados_json['problemas'] if item['latitude'] and item['longitude']]


dados_df = pd.DataFrame(dados_geocoded)

size_map = {"Alta": 15, "Mediana": 10, "Baixa": 5}
dados_df['urgencia_size'] = dados_df['urgencia'].map(size_map)

def create_bubble_map(dataframe):
    fig = px.scatter_mapbox(dataframe,
                            lat="latitude",
                            lon="longitude",
                            color="bairro",  # Cor baseada no bairro
                            size="urgencia_size",  # Tamanho baseado numa nova coluna 'urgencia_size'
                            color_discrete_sequence=px.colors.qualitative.Pastel,  # Esquema de cores mais suave
                            zoom=10,
                            height=869,
                            width=769)  # Altura maior do mapa
    fig.update_layout(mapbox_style="carto-positron")  # Mapa com menos informação visual
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


st.sidebar.title('Menu')
fig = create_bubble_map(dados_df)
st.plotly_chart(fig)
