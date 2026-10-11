import os

import requests
from dotenv import load_dotenv

from shopify_pipeline.client import get_access_token

load_dotenv()

shop = os.getenv("SHOPIFY_SHOP")
token = get_access_token()

url = f"https://{shop}/admin/api/2026-10/graphql.json"

query = """
{
    products(first: 5) {
        edges {
            node {
                id
                title
                status
                createdAt
            }
        }
        pageInfo {
            hasNextPage
            endCursor
        }
    }
}
"""

response = requests.post(
    url,
    json={"query": query},
    headers={
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
    },
    timeout=30,
)

response.raise_for_status()

result = response.json()

if "errors" in result:
    raise RuntimeError(result["errors"])

products = result["data"]["products"]["edges"]

for product in products:
    print(product["node"])