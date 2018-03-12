import requests

#create the query
query = {'ingredient': 'pizza'}

#send a GET request to locally run flask server
r = requests.get('http://localhost:5000/search', params=query)

#print the gotten json
print(r.json())
