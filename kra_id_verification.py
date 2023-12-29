# Import requests module
import requests

# Define base URL and API key
base_url = "https://api.appruve.co/v1/verifications/ke/kra"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5hcHBydXZlLmNvIiwianRpIjoiYWY0NmQxNWQtYThlZi00ZTIzLWEzZjItNzhmNGRjNzgyYWVhIiwiYXVkIjoiMDgwY2I4YzUtMTFiMi00NTA3LWIxNzMtYzcyMDM4NjU0ZDEyIiwic3ViIjoiZTU2ZjQwZGMtM2FiMi00MmY4LTkzMWQtYWJhYjY4YWJjY2EwIiwibmJmIjowLCJzY29wZXMiOlsidmVyaWZpY2F0aW9uX3ZpZXciLCJ2ZXJpZmljYXRpb25fbGlzdCIsInZlcmlmaWNhdGlvbl9kb2N1bWVudCIsInZlcmlmaWNhdGlvbl9pZGVudGl0eSJdLCJleHAiOjE3MDYyNTIwOTAsImlhdCI6MTcwMzY2MDA5MH0.gw_dtroDqofgtsgCZJLqeW48ic_v07aMNPqZ9yq6JRw"

# Define headers with API key
headers = {"Authorization": f"Bearer {api_key}"}

# Define data with national ID number
data = {"pin": "A000000010"}

# Send POST request to the national ID endpoint
response = requests.post(base_url, headers=headers, data=data)

# Check status code and handle errors
if response.status_code == 200:
    # Parse response data as JSON
    response_data = response.json()
    print(response_data)
    # Print verification status and score
    # print(f"Verification status: {response_data['verification_status']}")
    # print(f"Verification score: {response_data['verification_score']}")

else:
    # Print error message
    print(f"Request failed with status code: {response.status_code}")

