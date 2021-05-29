
import requests

def dat(pin,date):
    
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pin)+"&date="+date
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
    r = requests.get(url = URL, headers=headers)
    data=r.json()
    return(data)

