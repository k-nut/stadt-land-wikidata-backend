import requests


def make_query(name, template, entity):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(name=name)
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = data['results']['bindings']
    if results:
        return {'link': results[0]['item']['value'],
                'correct': True,
                'name': name,
                'entity': entity}
    return {'correct': False,
            'name': name,
            'entity': entity}


def check_city(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q515 .
      ?item wdt:P17 wd:Q183 .
      ?item ?label "{name}"@de .
    }}
    """
    return make_query(name, template, "city")


def check_country(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q6256 .
      ?item ?label "{name}"@de .
    }}
    """
    return make_query(name, template, "country")


def check_river(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q4022 .
      ?item wdt:P17 wd:Q183 .
      ?item ?label "{name}"@de .
    }}

    """
    return make_query(name, template, "river")


def example_river(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q4022 .
      ?item wdt:P17 wd:Q183 .
      ?item rdfs:label ?itemLabel .
      ?item wdt:P2043 ?length .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    order by desc(?length)
    limit 5"""
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(letter=letter.lower())
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = {"examples": data['results']['bindings'], "entity": "river"}
    return results or None


def example_country(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q6256 .
      ?item rdfs:label ?itemLabel .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    order by desc(?length)
    limit 5"""
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(letter=letter.lower())
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = {"examples": data['results']['bindings'], "entity": "country"}
    return results or None


def example_city(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q515 .
      ?item wdt:P17 wd:Q183 .
      ?item rdfs:label ?itemLabel .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    order by desc(?length)
    limit 5"""
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    query = template.format(letter=letter.lower())
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()
    results = {"examples": data['results']['bindings'], "entity": "city"}
    return results or None