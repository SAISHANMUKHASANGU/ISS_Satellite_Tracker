import requests
from datetime import datetime
import smtplib

my_email="abc@Yourmailprovider.com"
password="nkfnsdlkfnslkdnflk"


my_lat=12.908201
my_lng=77.558269

parameters={
    'lat':my_lat,
    'lng':my_lng,
    'formatted':0
}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data=response.json()

longitude=float(data["iss_position"]["longitude"])
latitude=float(data["iss_position"]["latitude"])


now=datetime.now()
now.hour

if my_lat==latitude and my_lng==longitude:
    if now>sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="20981a4248@raghuenggcollege.in",
                                msg=f"Subject:Look Up\n\nThe ISS satellite is on your top")

    else:
        print("yes")

else:
    print("no")

