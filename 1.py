import urllib.parse

data = {
    "m_ts": 1758859976,
    "li": "yBLWaNo3yCbGoJgrOxFDDjjk",
    "try_number": 0,
    "unrecognized_tries": 0,
    "email": "100056503155212",
    "prefill_contact_point": "100056503155212",
    "prefill_source": "browser_dropdown",
    "prefill_type": "password",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": True,
    "had_password_prefilled": True,
    "is_smart_lock": False,
    "bi_xrwh": 92004344361786634,
    "encpass": "#PWD_BROWSER:5:1758859991:AWpQAJ78nsELQ6oAmTKN60TUqyU3S+4pPGhmFdKL40ndAsgorMtdauIzLDtczxHxR4kOLhmbNJkWpCygokCpNw8PfXHkkW2FIuFOnkmliVxJMjoA4sCgle6XrNEM5RuiTcxtyzWenyCyqw==",
    "fb_dtsg": "NAfup2Me3JHXJFN2yxBY35qKn-1LtNpMqJhQzaJ3AqYbs8PMFOvFhGw:0:0",
    "jazoest": 24862,
    "lsd": "AdEVi-OFg_s",
    "_dyn": "1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE",
    "req": 1,
    "fmt": 1,
    "a": "AYrzCMozrxxEkLpLMe4Y2HjtqtsmVGwYzrN5JRYYClldhdPtYgFp1Jf_aTSnrZs9GEMJRGEqpBnp7Yr7bbjZFjK5_l3XCV2rjhwTOtu5o4lWwg",
    "_user": 0
}

urlencoded_string = urllib.parse.urlencode(data)
print(urlencoded_string)
