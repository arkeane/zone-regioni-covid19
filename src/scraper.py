from bs4 import BeautifulSoup as Bs
import requests as rq


# check if provided string is a region
def is_a_region(region):
    if "bolzano" in region:
        region = "pabolzano"
    elif "trento" in region:
        region = "patrento"
    elif "friuli" in region:
        region = "friuliveneziagiulia"
    elif "aosta" in region:
        region = "valleaosta"
    elif "emilia" in region:
        region = "emiliaromagna"
    else:
        region = region

    regions = ["valleaosta", "piemonte", "lombardia", "veneto", "friuliveneziagiulia", "pabolzano",
               "patrento", "liguria", "emiliaromagna", "toscana", "marche", "umbria", "lazio",
               "abruzzo", "molise", "campania", "basilicata", "calabria", "puglia", "sicilia", "sardegna"]

    for n in regions:
        if region == n:
            return region

    region = "not_a_region"
    return region


def scrape_zone(region):
    url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano' \
          '&id=5351&area=nuovoCoronavirus&menu=vuoto '
    response = rq.get(url, timeout=5)
    content = Bs(response.text, features="html.parser")

    region = region.replace(" ", "")

    region = is_a_region(region)
    if region == "not_a_region":
        color = "not_found"
        return color

    color = "white"

    # RED Check
    red = (content.find("div", {"style": "text-align:center;background-color:#f7e4e5;color:#000;padding:10px;border: "
                                         "1px solid #dd222a;"})).get_text()
    red_txt = red.replace(" ", "")
    red_txt = red_txt.lower()
    if region in red_txt:
        color = "red"

    orange = (content.find("div", {"style": "text-align:center;background-color:#ffecd7;color:#000;padding:10px"
                                            ";border: 1px solid #e78314;"})).get_text()
    orange_txt = orange.replace(" ", "")
    orange_txt = orange_txt.lower()
    if region in orange_txt:
        color = "orange"

    yellow = (content.find("div", {"style": "text-align:center;background-color:#fff7bd;color:#000;padding:10px"
                                            ";border: 1px solid #f8c300;"})).get_text()
    yellow_txt = yellow.replace(" ", "")
    yellow_txt = yellow_txt.lower()
    if region in yellow_txt:
        color = "yellow"

    return color
