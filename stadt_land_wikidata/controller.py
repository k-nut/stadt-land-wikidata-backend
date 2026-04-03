import requests


def get(query):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    user_agent = 'StadtLandWikidataBackend/0.0 (https://github.com/k-nut/stadt-land-wikidata-backend; stadt-land-wikidata@k-nut.eu)'
    response = requests.get(url, headers={'User-Agent': user_agent}, params={'query': query, 'format': 'json'})
    return response.json()

def make_query(name, template, entity):
    query = template.format(name=name)
    data = get(query)
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
      ?item ?label "{name}"@de .
    }}

    """
    return make_query(name, template, "river")


def check_profession(name):
    template = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q28640 .
      ?item ?label "{name}"@de .
    }}
    """
    return make_query(name, template, "profession")


def example_river(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q4022 .
      ?item rdfs:label ?itemLabel .
      ?item wdt:P2043 ?length .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    order by desc(?length)
    limit 5"""
    query = template.format(letter=letter.lower())
    data = get(query)
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
    query = template.format(letter=letter.lower())
    data = get(query)
    results = {"examples": data['results']['bindings'], "entity": "country"}
    return results or None


def example_city(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q515 .
      ?item rdfs:label ?itemLabel .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    limit 5"""
    query = template.format(letter=letter.lower())
    data = get(query)
    results = {"examples": data['results']['bindings'], "entity": "city"}
    return results or None


def example_profession(letter):
    template = """SELECT ?item ?itemLabel ?length
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q28640 .
      ?item rdfs:label ?itemLabel .
      filter(lang(?itemLabel) = "de") .
      filter(strStarts(lcase(?itemLabel), "{letter}"))
    }}
    limit 5"""
    query = template.format(letter=letter.lower())
    data = get(query)
    results = {"examples": data['results']['bindings'], "entity": "profession"}
    return results or None
