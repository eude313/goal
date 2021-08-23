import urllib.request,json


# Getting api key
secret_key = None
# Getting the news base url
popular_quote_url = None
# Getting the new_quote_url base url
new_quote_url = None

def configure_request(app):
    global  secret_key, popular_quote_url, new_quote_url
    secret_key = app.config["SECRET_KEY"]
    popular_quote_url = app.config["POPULAR_QUOTE"]
    new_quote_url = app.config["NEW_QUOTE"]