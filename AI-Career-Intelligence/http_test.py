import requests

response = requests.get("https://httpbin.org/status/404")

print(response.status_code)

if response.status_code == 200:
    print("Reuest succesful")
else:
    print("Request failed")
