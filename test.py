# import requests

# proxies = {
# "http": "http://scraperapi:8d54d2a2ffe681e1c0582e4e22b52ac8@proxy-server.scraperapi.com:8001"
# }
# r = requests.get('http://httpbin.org/ip', proxies=proxies, verify=False)
# print(r.text)


from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS
import requests

# Create gateway object and initialise in AWS
gateway = ApiGateway("https://checkip.amazonaws.com")
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount("https://checkip.amazonaws.com", gateway)

# Send request (IP will be randomised)
response = session.get("https://checkip.amazonaws.com", params={"theme": "light"})
print(response.text.rstrip())

# Delete gateways
gateway.shutdown()

