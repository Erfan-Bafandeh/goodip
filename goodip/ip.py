from .connection_check import connection_check
from bs4 import BeautifulSoup
from requests import get
from sys import exit

class ip:
    def __init__(self):
        if connection_check() == False:
            print("please turn on your internet :|")
            exit()
        response = get("https://browserleaks.com/ip").text
        html = BeautifulSoup(response, "html.parser")
        self.ip = html.find_all("span", {"class":"flag-text wball"})[0].text
        self.country = html.find_all("tbody")[0].find_all("tr")[4].find_all("td")[1].span.text
        self.region = html.find_all("tbody")[0].find_all("tr")[5].find_all("td")[1].text
        self.city = html.find_all("tbody")[0].find_all("tr")[6].find_all("td")[1].text
        self.isp = html.find_all("tbody")[0].find_all("tr")[7].find_all("td")[1].text
        self.organization = html.find_all("tbody")[0].find_all("tr")[8].find_all("td")[1].text
        self.network = html.find_all("tbody")[0].find_all("tr")[9].find_all("td")[1].text
        self.usage_type = html.find_all("tbody")[0].find_all("tr")[10].find_all("td")[1].text
        self.timezone = html.find_all("tbody")[0].find_all("tr")[11].find_all("td")[1].text
        self.local_time = html.find_all("tbody")[0].find_all("tr")[12].find_all("td")[1].text
        self.coordinates = html.find_all("tbody")[0].find_all("tr")[13].find_all("td")[1].text
        self.os = html.find_all("tbody")[3].find_all("tr")[1].find_all("td")[1].text
