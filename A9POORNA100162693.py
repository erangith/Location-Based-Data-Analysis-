# Assignment 9
# Author: <Dadayakkara Dewege poorna Erangith Wijesire> 

import requests

def getDataFromApi(url):
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()
    else:
        print(f"Error Retrieving Data from {url}")
        return []
    
health_url = "https://data.novascotia.ca/resource/tmfr-3h8a.json"
education_url = "https://data.novascotia.ca/resource/iyap-ttn5.json"
corrections_url = "https://data.novascotia.ca/resource/45un-ukgv.json"

hospital_data = getDataFromApi(health_url)
school_data = getDataFromApi(education_url)
corrections_data = getDataFromApi(corrections_url)

def fetchTownData(town_name):
    town_schools = [i for i in school_data if i.get('mail_address_line_2', '').lower() == town_name.lower()]
    town_corrections = [i for i in corrections_data if i.get('city_town', '').lower() == town_name.lower()]
    town_hospitals = [i for i in hospital_data if i.get('town', '').lower() == town_name.lower()]
    
    return town_schools, town_corrections, town_hospitals

while True:
    userinput = input("Enter a town name (or type 'done' when done): ")
    
    if userinput.lower() == 'done':
        break
    
    schools, corrections, hospitals = fetchTownData(userinput)
    
    if len(schools) + len(corrections) + len(hospitals) == 0:
        print("That town has no services, or it does not exist!")
        continue
    
    print(f"Services in: {userinput.title()}")
    print("-"*50)
    
    if len(hospitals) > 0:
        print("\nHospitals:")
        print("-"*50)
        
        for h in hospitals:
            print(f"{h['facility']} {h.get('address')} ")
        
    if len(schools) > 0:
        print("\nSchools:")
        print("-"*50)
        
        for s in schools:
            print(f"{s['school_name']} {s.get('mail_address_line_1')} ")
            
        
    if len(corrections) > 0:
        
        print("\nCorrections:")
        print("-"*50)
        
        for c in corrections:
            print(f"{c['service_name']} {c.get('civic_number')} {c.get('street_name')}")