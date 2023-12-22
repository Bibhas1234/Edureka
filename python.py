
import requests
import logging

def extract_endpoints(swagger_url):
    logging.info(f"Fetching Swagger JSON from {swagger_url}")
    try:
        response = requests.get(swagger_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        swagger_json = response.json()

        endpoints = []
        for path in swagger_json.get("paths", {}):
            endpoints.append(path)

        logging.info(f"Extracted endpoints: {endpoints}")
        return endpoints
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Swagger JSON: {e}")
        return None

if __name__ == "__main__":
    swagger_url = "http://petstore.swagger.io"  # Replace with your Swagger JSON URL
    endpoints = extract_endpoints(swagger_url)

    if endpoints:
        print("List of endpoints:")
        for endpoint in endpoints:
            print(endpoint)
    else:
        print("Failed to extract endpoints.")
