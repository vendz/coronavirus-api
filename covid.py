import requests
from bs4 import BeautifulSoup


def information(cname):
    totalresult = []
    country = cname
    url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(countryname=country)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div', class_="maincounter-number")
        active = soup.find_all('div', class_="number-table-main")
        for i in result:
            totalresult.append(i.find("span").text)
        for a in active:
            totalresult.append(a.text)
        x = totalresult[0].replace(",", "")
        y = totalresult[3].replace(",", "")
        active_case = int(x) - int(y)
        totalresult.append(active_case)
    else:
        totalresult.append("No Result")
    return totalresult


def all_countries():
    result = []
    url = "https://www.worldometers.info/coronavirus/#countries"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        all_country = soup.find_all('a', class_="mt_a")
        for a in all_country:
            result.append(a.text)
    else:
        result.append("No Result")
    return result


def global_info():
    totalresult = []
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div', class_="maincounter-number")
        active = soup.find_all('div', class_="number-table-main")
        for i in result:
            totalresult.append(i.find("span").text)
        for a in active:
            totalresult.append(a.text)
        x = totalresult[0].replace(",", "")
        y = totalresult[3].replace(",", "")
        active_case = int(x) - int(y)
        totalresult.append(active_case)
    else:
        totalresult.append("No Result")
    return totalresult