from geopy.geocoders import Nominatim


# teste usando o geopy, coders pra achar latitude e longitude pro bubblemap 
geolocator = Nominatim(user_agent="teste")

geocode = lambda query, **kw: geolocator.geocode("%s Sao Paulo" % query, **kw)

rua = 'Doutor Joao Batista Vasques'
bairro = 'Vila Augusta'

result = geocode(f'{rua},{bairro}',language="pt-BR")

print(result.latitude,result.longitude)

location = geolocator.reverse(f'{result.latitude},{result.longitude}')

print(location.address)