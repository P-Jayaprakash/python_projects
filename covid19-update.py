import requests
from win10toast import ToastNotifier
import json
import time
def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'confirmed cases:{data["cases"]} \nDeaths :{data["deaths"]} \nRecovered :{data["recovered"]}'

    
    while True:
        toast=ToastNotifier()
        toast.show_toast("covid-19 updates",text,duration=20)
        time.sleep(1)

update()        
        
