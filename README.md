# vasttrafik
A small python module for communicating with the Västtrafik API. This module is meant to enable programmers to use the Västtrafik API without the going through the hassle that is OAuth2.

## Usage instructions
* Register an account at https://developer.vasttrafik.se/ 
* Create an application and get the key and the secret.

### Using the API
Each user should have its own scope (a number). Then each user will have its own token and you can get user statistics on the dev portal.
```import vasttrafik
auth = vasttrafik.Auth(key, secret, scope)
resepl = vasttrafik.Reseplaneraren(auth)
trafficsit = vasttrafik.TrafficSituations(auth)
```
I would recommend storing the key and secret in a separate file and not in the code. Add the file to .gitignore if you use GitHub.

```Reseplaneraren``` has the following methods:
* ```Reseplaneraren.trip(<args>)```
* ```Reseplaneraren.location_nearbyaddress(<args>)```
* ```Reseplaneraren.location_nearbystops(<args>)```
* ```Reseplaneraren.location_allstops(<args>)```
* ```Reseplaneraren.location_name(<args>)```
* ```Reseplaneraren.systeminfo(<args>)```
* ```Reseplaneraren.livemap(<args>)```
* ```Reseplaneraren.journeyDetail(<args>)```
* ```Reseplaneraren.geometry(<args>)```
* ```Reseplaneraren.departureBoard(<args>)```
* ```Reseplaneraren.arrivalBoard(<args>)```
* ```Reseplaneraren.request(url)```

All methods except for ```Reseplaneraren.request(url)``` is connected directly to the respective API methods found on the dev portal (go to the Reseplaneraren API and click on API-konsol). Use that as the documentation for what arguments can provided. The argument format is the same as on the dev portal. The ```Reseplaneraren.request(url)``` method is for when you get a ref link in another API call and you want to call it.

```TrafficSituations``` has the following methods:
* ```TrafficSituations.trafficsituations()```
* ```TrafficSituations.stoppoint(gid)```
* ```TrafficSituations.situation(gid)```
* ```TrafficSituations.line(gid)```
* ```TrafficSituations.journey(gid)```
* ```TrafficSituations.stoparea(gid)```

These methods are also connected directly to the respective API methods and the dev portal should be used as documentation.