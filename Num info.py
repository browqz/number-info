import requests

def num_info(numero_tel):
    api_key = "CLE_API" 
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={numero_tel}&format=1"
    
    response = requests.get(url)
    data = response.json()
    
    if data["valid"]:
        pays = data["country_name"]
        Localisation = data["location"]
        Opérateur = data["carrier"]
        type_ligne = data["line_type"]
        
        print("Informations du numéro de téléphone:")
        print(f"Pays : {pays}")
        print(f"Localisation : {Localisation}")
        print(f"Opérateur : {Opérateur}")
        print(f"Type de ligne : {type_ligne}")
    else:
        print("Numéro de téléphone non valide.")

numero_tel = input("Entrez un numéro de téléphone : ")
num_info(numero_tel)
