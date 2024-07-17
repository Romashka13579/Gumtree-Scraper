import json

# Example 2D array of data
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert the 2D array to a JSON string
json_string = json.dumps(data)
print("JSON String:", json_string)

# Save the JSON string to a file
with open('data_2d.json', 'w') as json_file:
    json.dump(data, json_file)
    print("Data saved to data_2d.json")

# Read the JSON data back from the file
with open('data_2d.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded Data:", loaded_data)