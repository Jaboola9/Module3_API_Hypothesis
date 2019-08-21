def browse_quotes(origin,dest,key,deptDate,retDate=None):
    """
    Submit custom queries to the SkyScanner Browse Quote API Endpoint and returns a Requests Response object.
    """
    import requests
    
    url_api = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices'
    url = f"{url_api}/browsequotes/v1.0/US/USD/en-US/{origin}/{dest}/{deptDate}"
    
    if retDate:
        querystring = {"inboundpartialdate":retDate}
    else:
        querystring = {}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

def browse_routes(origin,dest,key,deptDate,retDate=None):
    """
    Submit custom query to the SkyScanner Browse Routes API Endpoint and returns a Requests Response object.
    """
    import requests
    
    url_api = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices'
    url = f"{url_api}/browseroutes/v1.0/US/USD/en-US/{origin}/{dest}/{deptDate}"
    
    if retDate:
        querystring = {"inboundpartialdate":retDate}
    else:
        querystring = {}
        
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

def browse_dates(origin,dest,key,deptDate='anytime',retDate=None):
    """
    Submit custom query to the SkyScanner Browse Dates API Endpoint and returns a Requests Response object.
    """
    import requests
    
    url_api = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices'
    url = f"{url_api}/browsedates/v1.0/US/USD/en-US/{origin}/{dest}/{deptDate}"

    if retDate:
        querystring = {"inboundpartialdate":retDate}
    else:
        querystring = {}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response