
"""

@author: cgarn

"""

import requests

# Define API base URL 
api_base_url = "https://example.com/api"  # Use the appropriate API base URL

# Load configuration (simulated with an API call)
config_file = "config_file_name.config"  # Replace with your configuration file name
config_url = f"{api_base_url}/configuration"
config_response = requests.post(config_url, json={"config_file": config_file})

# Establish connection (simulated with an API call)
connection_url = f"{api_base_url}/connection"
connection_response = requests.post(connection_url, json={"config": config_file})

# Set up service (directly use API)
service_url = f"{api_base_url}/service"

# Inputs for the data
input_1 = 'DATA001'  # Data reference
input_2 = 'PROPERTY1'  # Property code
# repeat as necessary 
  
# Create handles via API for the data, property, and specification using POST
data_url = f"{api_base_url}/data"
data_response = requests.post(data_url, json={"input_1": input_1})

property_url = f"{api_base_url}/property"
property_response = requests.post(property_url, json={"input_2": input_2})
# repeat as necessary

# Retrieve the result value via API using GET
result_value_url = f"{api_base_url}/result_value"
result_value_response = requests.get(result_value_url, params={
    "data": input_1,      # use input_1 instead of data
    "property": input_2,   # use input_2 instead of property
    
})

# OPTIONAL - Check if the GET request was successful
if result_value_response.status_code == 200:
    # Process the JSON response
    result_value_data = result_value_response.json()
    print("Result Value Data:", result_value_data)
else:
    print(f"Error retrieving result value: {result_value_response.status_code} - {result_value_response.text}")

# END
