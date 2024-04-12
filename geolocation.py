import requests

city = str(input("Enter location: "))

def geocode(address):
    url = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q':address, 'format':'json'}
    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, params=parameters, headers=headers)
    reply = response.json()
    print(reply[0]['lat'], reply[0]['lon'])
    print('Link: ',f'https://nominatim.openstreetmap.org/ui/search.html?q=+{reply[0]["lat"]}+{reply[0]["lon"]}')

if __name__ == '__main__':
    geocode(city)
