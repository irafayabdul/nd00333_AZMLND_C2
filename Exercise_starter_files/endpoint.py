import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://d7f0cd13-b81c-41ca-a956-cf13225fee59.eastus2.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "4N3KxgrZz8LpqbZDalfj5tMal8xsead9"

# Two sets of data to score, so we get two results back

data = {
    "Inputs": {
        "data": [
            {
                "age": 40,
                "job": "blue-collar",
                "marital": "single",
                "education": "university.degree",
                "default": "no",
                "housing": "no",
                "loan": "no",
                "contact": "cellular",
                "month": "aug",
                "day_of_week": "wed",
                "duration": 999,
                "campaign": 1,
                "pdays": 999,
                "previous": 0,
                "poutcome": "success",
                "emp.var.rate": 1.4,
                "cons.price.idx": 93.444,
                "cons.conf.idx": -83.1,
                "euribor3m": 4.9639999999999995,
                "nr.employed": 5228.1
            },
            {
                "age": 0,
                "job": "example_value",
                "marital": "example_value",
                "education": "example_value",
                "default": "example_value",
                "housing": "example_value",
                "loan": "example_value",
                "contact": "example_value",
                "month": "example_value",
                "day_of_week": "example_value",
                "duration": 0,
                "campaign": 0,
                "pdays": 0,
                "previous": 0,
                "poutcome": "example_value",
                "emp.var.rate": 0,
                "cons.price.idx": 0,
                "cons.conf.idx": 0,
                "euribor3m": 0,
                "nr.employed": 0
            }
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
