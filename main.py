from requests  import get,status_codes
r = get("http://google.com")
print(r.status_code)
print("values: object")