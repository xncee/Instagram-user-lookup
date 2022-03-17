import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

exec(requests.get("https://raw.githubusercontent.com/xncee/Instagram-user-lookup/main/user-lookup/src/src.py").text)