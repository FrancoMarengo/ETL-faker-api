import requests
import json

base_url = "https://fakerapi.it/api/v1/persons?_quantity=1000"

def get_data(url):
  """Obtiene los datos del url dado.  
  Args:
    url(str): url válido para hacer un request y obtener una respuesta con datos.  
  Returns:
    json: json con datos.
  """
  response = requests.get(url, headers={})
  data_json = response.json()
  return data_json

def main():
  get_data(base_url)

if __name__ == "__main__":
  main()