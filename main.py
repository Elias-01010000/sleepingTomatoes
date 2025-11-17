import requests
response = requests.get("https://www.google.com")
print(response)
print(response.url)
print(response.text)

