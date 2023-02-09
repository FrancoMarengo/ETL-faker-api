import requests
import singer

# URL base para conectarse con la API
base_url = "https://fakerapi.it/api/v1/"

# Endpoint para hacer el request
endpoint = "persons?"

# Configuracion que permite hacer fake api para obtener un numero determinado de datos
fake_api_config = "_quantity=1000"

# URL final para hacer el request
url = base_url+endpoint+fake_api_config

# 
schema = {'properties': {
      'id': {'type': 'String'},
      'firstname': {'type': 'string'},
      'lastname': {'type': 'string'},
      'email': {'type': 'string'},
      'phone': {'type': 'string'},
      'birthday': {'type': 'string'},
      'gender': {'type': 'string'},
      'address': {
        'id': {'type': 'number'},
        'street': {'type': 'string'},
        'streetName': {'type': 'string'},
        'buildingNumber': {'type': 'string'},
        'city': {'type': 'string'},
        'zipcode': {'type': 'string'},
        'country': {'type': 'string'},
        'county_code': {'type': 'string'},
        'latitude': {'type': 'number'},
        'longitude': {'type': 'number'}
      },
      'website': {'type': 'string'},
      'image': {'type': 'string'}
    }
}

# .
singer.write_schema(stream_name='persons', schema=schema, key_properties=['id'])

def main():
    for per in requests.get(url).json()["data"]:
        singer.write_record(stream_name='persons', record=(per))

if __name__ == "__main__":
    main()
