import requests


endpoint = "http://127.0.0.1:8000/api/predict/"

data = {
    'HighBP':0, 
    'HighChol':0, 
    'BMI':22, 
    'Smoke':0, 
    'Fruit':1, 
    'Genhlth':4, 
    'MentHlth':1, 
    'PhysHlth':1, 
    'DiffWalk':0, 
    'Sex':1, 
    'Age':3,
}
get_response = requests.post(endpoint, json=data )
# print(get_response.headers)
print(get_response.text)

