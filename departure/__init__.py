import logging

import azure.functions as func
import requests as http
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    f = req.params.get('f')
    t = req.params.get('t')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name and not t is None or not f is None:
        url = f"http://transport.opendata.ch/v1/connections?from={f}&to={t}&limit=1"
        respond = http.get(url)
        data = respond.json()
        for connections in data['connections']:
            _from = connections['from']
            departure = _from['departure']
            date_obj = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S%z")
            departure_fancied = date_obj.strftime("%d.%m.%Y %H:%M:%S")               

        return func.HttpResponse(f"""
        Hello, {name}. Das ist eine Azure Function App als Übung. Hier wurde die API Aufgabe vom 1.4.2023 als Function App implementiert.
        Die Function App holt sich die nächste Abfahr der ÖV von f (from) nach t (to), wobei f & t anzugben sind.
        Die nächste Abfahrt von {f} nach {t} ist exakt um: {departure_fancied}
        """,
        status_code=200)
    if t is None or f is None:
        return func.HttpResponse(f"""
        Keine Parameter für Von und Nach angegeben. Bitte Paramter eingeben.
        Beispiel:
        ?name=nik&f=Rotkreuz&t=Luzern

        name = <dein name>
        f = from
        t = to
        """,
        status_code=200)
    else:
        url = f"http://transport.opendata.ch/v1/connections?from={f}&to={t}&limit=1"
        respond = http.get(url)
        data = respond.json()
        for connections in data['connections']:
            _from = connections['from']
            departure = _from['departure']
            date_obj = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S%z")
            departure_fancied = date_obj.strftime("%d.%m.%Y %H:%M:%S")   

        return func.HttpResponse(f"""
        Das ist eine Azure Function App als Übung. Hier wurde die API Aufgabe vom 1.4.2023 als Function App implementiert.
        Die Function App holt sich die nächste Abfahr der ÖV von f (from) nach t (to), webei f & t parameter sind.
        Die nächste Abfahrt von {f} nach {t} ist exakt um: {departure_fancied}
        """,
        status_code=200)

