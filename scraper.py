from bs4 import BeautifulSoup as bs
import requests as rq


def scrape_zone(region):
    url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano' \
          '&id=5351&area=nuovoCoronavirus&menu=vuoto '
    response = rq.get(url, timeout=5)
    content = bs(response.text, features="html.parser")

    if "bolzano" in region:
        region = "provincia autonoma di bolzano"
    elif "trento" in region:
        region = "provincia autonoma di trento"
    elif "friuli" in region:
        region = "friuli venezia giulia"
    elif "aosta" in region:
        region = "val d'aosta"
    elif "emilia" in region:
        region = "emilia romagna"
    else:
        region = region

    color = "white or not found"
    region = region.replace(" ", "")

    # RED Check
    red = (content.find("td", {"class": "redText"})).get_text()
    red_txt = red.replace(" ", "")
    red_list = list(red_txt.split())
    for n in red_list:
        if region == n.lower():
            color = "red"

    # ORANGE Check
    orange = (content.find("td", {"class": "orangeText"})).get_text()
    orange_txt = orange.replace(" ", "")
    orange_list = list(orange_txt.split())
    for n in orange_list:
        if region == n.lower():
            color = "orange"

    # YELLOW Check
    yellow = (content.find("td", {"class": "yellowText"})).get_text()
    yellow_txt = yellow.replace(" ", "")
    yellow_list = list(yellow_txt.split())
    for n in yellow_list:
        if region == n.lower():
            color = "yellow"

    return color
