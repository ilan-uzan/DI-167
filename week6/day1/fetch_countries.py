import requests
import json

V3_URL = "https://restcountries.com/v3.1/all"
V3_PARAMS = {"fields": "name,capital,cca2,region,population"}
V2_URL = "https://restcountries.com/v2/all"

HEADERS = {"User-Agent": "countries-loader/1.0 (+https://example.com)"}

def fetch_countries():
    try:
        r = requests.get(V3_URL, params=V3_PARAMS, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print("v3 failed:", e)

    # fallback to v2
    r = requests.get(V2_URL, headers=HEADERS, timeout=30)
    if r.status_code == 200:
        return r.json()

    return []

if __name__ == "__main__":
    data = fetch_countries()
    print(f"Fetched {len(data)} items")
    with open("countries.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ Saved to countries.json")