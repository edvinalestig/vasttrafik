# coding: utf-8
import base64
import requests

class Reseplaneraren():
    def __init__(self, key, secret, scope):
        if key == None or secret == None or scope == None:
            raise TypeError("Usage: Reseplaneraren(<key>, <secret>, <scope>)")

        if type(key) != str:
            raise TypeError("Expected str [key]")
        if type(secret) != str:
            raise TypeError("Expected str [secret]")
        if type(scope) != int:
            raise TypeError("Expected int [scope]")

        self.__credentials = base64.b64encode(str.encode(f'{key}:{secret}')).decode("utf-8")
        self.scope = scope

        self.__renew_token()


    def __renew_token(self):
        print(self.__credentials)
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + self.__credentials
        }
        url = f'https://api.vasttrafik.se/token?grant_type=client_credentials&scope=device_{self.scope}'
        response = requests.post(url, headers=header)

        print(response.text)
        response_dict = response.json()

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        self.token = "Bearer " + response_dict.get("access_token")


    def __check_response(self, response):
        if response.status_code == 401:
            self.__renew_token()

            header = {"Authorization": self.token}
            response = requests.get(response.url, headers=header)

        response_dict = response.json()
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        return response


    def trip(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/trip"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def location_nearbyaddress(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/location.nearbyaddress"
        kwargs["format"] = "json"
 
        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def location_nearbystops(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/location.nearbystops"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def location_allstops(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/location.allstops"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def location_name(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/location.name"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def systeminfo(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/systeminfo"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def livemap(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/livemap"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def journeyDetail(self, ref):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/journeyDetail"

        response = requests.get(url, headers=header, params={"ref":ref})
        response = self.__check_response(response)

        return response.json()


    def geometry(self, ref):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/geometry"

        response = requests.get(url, headers=header, params={"ref":ref})
        response = self.__check_response(response)

        return response.json()


    def departureBoard(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def arrivalBoard(self, **kwargs):
        header = {"Authorization": self.token}
        url = "https://api.vasttrafik.se/bin/rest.exe/v2/arrivalBoard"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.__check_response(response)

        return response.json()


    def request(self, url):
        header = {"Authorization": self.token}
        response = requests.get(url, headers=header)
        response = self.__check_response(response)

        return response.json()


if __name__ == "__main__":
    with open("credentials.csv", "r") as f:
        key, secret = f.read().split(",")
    vt = Reseplaneraren(key, secret, 0)

    # stop1 = vt.location_name(input="Chalmers").get("LocationList").get("StopLocation")[0].get("id")
    # stop2 = vt.location_name(input="Kampenhof").get("LocationList").get("StopLocation")[0].get("id")
    # print(vt.trip(originId=stop1, destId=stop2, date=20181020, time="15:24"))
    print(vt.token)