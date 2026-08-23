import requests

def get_random_fact():
    # Public API endpoint (no authentication needed)
    url = "https://catfact.ninja/fact"
    
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url, timeout=5)
        
        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            # Parse the response body into a Python dictionary
            data = response.json()
            print("--------------------------------------------------")
            print("🌐 API Request Successful!")
            print(f"Status Code: {response.status_code}")
            print(f"Fact: {data['fact']}")
            print("--------------------------------------------------")
        else:
            print(f"❌ Failed to fetch data. HTTP Status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error occurred: {e}")

if __name__ == "__main__":
    get_random_fact()