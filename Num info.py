import requests

def num_info(numero_tel):
    api_key = "CLE_API" 
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={numero_tel}&format=1"
    
    response = requests.get(url)
    data = response.json()
    
    if data["valid"]:
        country = data["country_name"]
        location = data["location"]
        carrier = data["carrier"]
        line_type = data["line_type"]
        
        print("Informations du numéro de téléphone:")
        print(f"Pays : {country}")
        print(f"Localisation : {location}")
        print(f"Opérateur : {carrier}")
        print(f"Type de ligne : {line_type}")
    else:
        print("Numéro de téléphone non valide.")

numero_tel = input("Entrez un numéro de téléphone : ")
num_info(numero_tel)