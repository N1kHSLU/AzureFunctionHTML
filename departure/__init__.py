import logging

import azure.functions as func
import requests as http
from datetime import datetime
import mimetypes

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    index = f"{context.function_directory}/static/index.html"


    with open(index, 'rb') as f:
        mimetype = mimetypes.guess_type(index)
        return func.HttpResponse(f.read(), mimetype=mimetype[0])    

