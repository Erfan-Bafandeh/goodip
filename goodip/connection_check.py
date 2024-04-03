from requests import get, ConnectionError

def connection_check():
    try:
        response = get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except ConnectionError:
        return False
