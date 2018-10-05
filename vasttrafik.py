# coding: utf-8
# import json
import base64
import requests

class Vasttrafik():
    def __init__(self, key, secret, scope):
        if type(key) != str:
            raise TypeError("Expected str [key]")
        if type(secret) != str:
            raise TypeError("Expected str [secret]")
        if type(scope) != int:
            raise TypeError("Expected int [scope]")

        self.credentials = base64.b64encode(str.encode(f'{key}:{secret}')).decode("utf-8")
        self.scope = scope

        self.__renew_token()


    def __renew_token(self):
        print(self.credentials)
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + self.credentials
        }
        url = f'https://api.vasttrafik.se/token?grant_type=client_credentials&scope=device_{self.scope}'
        response = requests.post(url, headers=header)

        print(response.text)
        response_dict = response.json()

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        self.token = "Bearer " + response_dict.get("access_token")


    def trip(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/trip"
        kwargs["format"] = "json"
        response = requests.get(url, headers=header, params=kwargs)

        print(response.url)
        print(response.status_code)
        print(response.text)
        if response.status_code == 401:
            self.__renew_token()
            response = requests.get(url, headers=header, params=kwargs)

        response_dict = response.json()
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        return response_dict



with open("credentials.csv", "r") as f:
    key, secret = f.read().split(",")
vt = Vasttrafik(key, secret, 0)

print(vt.trip(originId=9021014001960000, destId=9021014005470000, date=20181020, time="15:24"))