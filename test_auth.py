from shopify_pipeline.client import get_access_token

try:
    token = get_access_token()

    print("Authentication successful.")
    print(f"Access token received: {bool(token)}")

except Exception as error:
    print(f"Authentication failed: {type(error).__name__}: {error}")