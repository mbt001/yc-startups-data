import requests
import pandas as pd

def fetch_all_yc_companies(batches):
    all_companies = []
    for batch in batches:
        page = 1
        while True:
            url = f"https://api.ycombinator.com/v0.1/companies?batch={batch}&page={page}"
            resp = requests.get(url)
            if resp.status_code != 200:
                print(f"Failed to fetch page {page} for batch {batch}")
                break
            data = resp.json()
            companies = data.get('companies', [])
            all_companies.extend(companies)
            # Check if nextPage exists
            if data.get('nextPage'):
                page += 1
            else:
                break
    return all_companies

batches = ["W23", "S23", "W24", "S24"]  # Adjust for desired years/batches
companies = fetch_all_yc_companies(batches)

# Prepare DataFrame
df = pd.DataFrame([{
    'Name': c.get('name'),
    'Batch': c.get('batch'),
    'Industries': ', '.join(c.get('industries', [])),
    'Tags': ', '.join(c.get('tags', [])),
    'Team Size': c.get('teamSize'),
    'Location': ', '.join(c.get('locations', [])),
    'Website': c.get('website'),
    'Status': c.get('status'),
    'Description': c.get('oneLiner')
} for c in companies])

# Save to Excel
df.to_excel('yc_companies_2023_2024.xlsx', index=False)
print('Saved to yc_companies_2023_2024.xlsx')

