import random

# Define base components
supports_fresco = "SupportsFresco=1"
modular = "modular=2"
dalvik_version = "Dalvik/2.1.0"
os_version = "Android 10"
device = "Redmi Note 7 Pro"
miui_versions = ["V12.5.1.0.QFHINXM", "V12.5.2.0.QFHINXM", "V12.5.3.0.QFHINXM"]
fban = "FBAN/EMA"
fbbv = "FBBV/645271943"
fbav = "FBAV/426.0.0.5.108"
fbdv = "FBDV/Redmi Note 7 Pro"
fbs_version = "FBSV/10"
fbcx = "FBCX/OkHttp3"
density = ["density=2.75", "density=2.50", "density=3.00"]

# Function to generate user agents
def generate_user_agent():
    return (
        f"{supports_fresco} "
        f"{modular} "
        f"{dalvik_version} "
        f"(Linux; U; {os_version}; {device} MIUI/{random.choice(miui_versions)}) "
        f"[{fbaan};{fbbv};{fbav};{fbdv};{fbs_version};{fbcx};"
        f"FBDM{{{random.choice(density)}}}]"
    )

# Generate 100 user agents
user_agents = [generate_user_agent() for _ in range(100)]

# Print the generated user agents
for ua in user_agents:
    print(ua)
