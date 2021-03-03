from ColoreRegioni import ColoreRegioni
from difflib import SequenceMatcher

colore_regioni = ColoreRegioni()
colors = colore_regioni.colori


def format_region(region):
    r_in = region
    for i in colors:
        s_1 = r_in.lower()
        s_2 = i.lower()
        print (s_2)
        similar = SequenceMatcher(a=s_1, b=s_2).ratio()
        print(similar)
        if (similar > 0.7):
            region = i
            break
    return region


def scrape_zone(region):
    region = format_region(region)
    print(region)
    if region in colors:
        return {"color": colors[region], "region": region}
    else:
        return {"color": "not_found", "region": region}

