

import requests

from API.First_API import response

parameters={"lat":45.0,"lon":-122.3}

response=requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
print(response.status_code)
print(response.json())