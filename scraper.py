from bs4 import BeautifulSoup as bs
import requests as rq


def is_a_region(region):
    if "bolzano" in region:
        region = "provinciaautonomadibolzano"
    elif "trento" in region:
        region = "provinciaautonomaditrento"
    elif "friuli" in region:
        region = "friuliveneziagiulia"
    elif "aosta" in region:
        region = "vald'aosta"
    elif "emilia" in region:
        region = "emiliaromagna"
    else:
        region = region

    regions = ["vald'aosta", "piemonte", "lombardia", "veneto", "friuli venezia giulia", "provinciaautonomadibolzano", "provinciaautonomaditrento",
               "liguria", "emiliaromagna", "toscana", "marche", "umbria", "lazio", "abruzzo", "molise", "campania", "basilicata", "calabria", "puglia",
               "sicilia", "sardegna"]

    for n in regions:
        if region == n:
            return region

    region = "not_a_region"
    return region


def scrape_zone(region):
    url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano' \
          '&id=5351&area=nuovoCoronavirus&menu=vuoto '
    response = rq.get(url, timeout=5)
    content = bs(response.text, features="html.parser")

    region = region.replace(" ", "")

    region = is_a_region(region)
    if region == "not_a_region":
        color = "not_found"
        return color

    color = "white"


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
