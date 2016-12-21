import requests

from bs4 import BeautifulSoup


def search(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    links = soup.find_all("a")

    # for link in links:
    #     # if "http" in link.get("href"):
    #     print("<a href='%s'>%s</a>" % (link.get("href"), link.text))

    g_data = soup.find_all("div", {"class": "info"})

    for item in g_data:
        try:
            business_name = (item.contents[0].select(".business-name")[0].text)
        except:
            pass
        try:
            street_Address = (item.contents[1].find_all(
                "span", {"itemprop": "streetAddress"})[0].text)
        except:
            pass

        try:
            address_locality = (item.contents[1].find_all(
                "span",
                {"itemprop": "addressLocality"})[0].text.replace(',', ''))
        except:
            pass
        try:
            address_Region = (item.contents[1].find_all(
                "span", {"itemprop": "addressRegion"})[0].text)
        except:
            pass

        try:
            postal_code = (item.contents[1].find_all(
                "span", {"itemprop": "postalCode"})[0].text)
        except:
            pass

        try:
            Primary = (item.contents[1].find_all(
                "div", {"itemprop": "telephone"})[0].text)
        except:
            pass
        return {
            'business-name': business_name,
            'streetAddress': street_Address,
            'addressLocality': address_locality,
            'addressRegion': address_Region,
            'postalCode': postal_code,
            'telephone': Primary,
        }
