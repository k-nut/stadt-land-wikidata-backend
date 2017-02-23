import requests


def check_city(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q515 .
      ?item wdt:P17 wd:Q183 .
      ?item ?label "{name}"@de .
    }}

    """

    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(name=name)
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = data['results']['bindings']
    if results:
        return results[0]['item']['value']
    return False


def check_country(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q6256 .
      ?item ?label "{name}"@de .
    }}
    """

    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(name=name)
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = data['results']['bindings']
    if results:
        return results[0]['item']['value']
    return False


def check_river(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q4022 .
      ?item wdt:P17 wd:Q183 .
      ?item ?label "{name}"@de .
    }}

    """

    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(name=name)
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = data['results']['bindings']
    if results:
        return results[0]['item']['value']
    return False
