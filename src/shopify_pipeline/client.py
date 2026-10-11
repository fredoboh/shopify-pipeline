import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_access_token():
    shop = os.getenv("SHOPIFY_SHOP")
    client_id = os.getenv("SHOPIFY_CLIENT_ID")
    client_secret = os.getenv("SHOPIFY_CLIENT_SECRET")

    if not all([shop, client_id, client_secret]):
        raise ValueError("Missing Shopify configuration")

    url = f"https://{shop}/admin/oauth/access_token"

    response = requests.post(
        url,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )

    response.raise_for_status()
    return response.json()["access_token"]

