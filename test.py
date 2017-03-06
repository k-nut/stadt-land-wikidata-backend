from mock import patch
import responses

from stadt_land_wikidata import controller


@patch("stadt_land_wikidata.controller.make_query")
def test_check_city(mock_query):
    controller.check_city("Braunschweig")
    query = """SELECT ?item
    WHERE
    {{
      ?item wdt:P31/wdt:P279* wd:Q515 .
      ?item wdt:P17 wd:Q183 .
      ?item ?label "{name}"@de .
    }}
    """
    mock_query.assert_called_once_with("Braunschweig", query, "city")


@responses.activate
def test_make_query_correct():
    responses.add(responses.GET,
                  'https://query.wikidata.org/bigdata/namespace/wdq/sparql',
                  json={"results": {
                      "bindings": [{
                          "item": {
                              "type": "uri",
                              "value": "http://www.wikidata.org/entity/Q64"
                          }}]}},
                  status=200,
                  content_type='application/json')
    template = """SELECT ?item
      WHERE
      {{
        ?item wdt:P31/wdt:P279* wd:Q515 .
        ?item wdt:P17 wd:Q183 .
        ?item ?label "{name}"@de .
      }}
      """
    results = controller.make_query("Berlin", template, "city")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('https://query.wikidata.org/bigdata/namespace/wdq/sparql')
    assert results['correct'] == True


@responses.activate
def test_make_query_incorrect():
    responses.add(responses.GET,
                  'https://query.wikidata.org/bigdata/namespace/wdq/sparql',
                  json={"results": {"bindings": []}},
                  status=200,
                  content_type='application/json')
    template = """SELECT ?item
      WHERE
      {{
        ?item wdt:P31/wdt:P279* wd:Q515 .
        ?item wdt:P17 wd:Q183 .
        ?item ?label "{name}"@de .
      }}
      """
    results = controller.make_query("This city does not exist", template, "city")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('https://query.wikidata.org/bigdata/namespace/wdq/sparql')
    assert results['correct'] == False