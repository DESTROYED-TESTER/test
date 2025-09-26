import requests, json

resp = requests.get(
    "https://password-enc-api-instagram-facebook.p.rapidapi.com/api/pass_enc/",
    headers={
        "x-rapidapi-key":"5b5179b509msh1ba72c98ba4d120p1e1335jsn6eb28abafc48",
        "x-rapidapi-host":"password-enc-api-instagram-facebook.p.rapidapi.com"
    },
    params={"p":"Password123 ","v":"5","m":"fbweb"},
    timeout=10
).json()

# 1) print whole response for debugging
print("FULL RESPONSE:", json.dumps(resp, indent=2))

# 2) try common keys and print first non-empty value, else fallback
def extract_pass(obj):
    # if it's a dict, check common keys
    if isinstance(obj, dict):
        for key in ("pass","password","enc","encpass","result"):
            val = obj.get(key)
            if val not in (None, "", []):
                return val
        # fallback: first non-empty value in dict
        for v in obj.values():
            if v not in (None, "", []):
                return v
    # if it's a list, try first non-empty element
    if isinstance(obj, list) and obj:
        for item in obj:
            if item not in (None, "", []):
                return item
    return ""  # nothing found -> empty string

value = extract_pass(resp)
print(value)   # will print the encpass (or empty string if none)
